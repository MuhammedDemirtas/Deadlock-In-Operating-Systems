import random
import matplotlib.pyplot as plt
import time

#kaynak sayılarının girilmesini sağladık
kaynak_sayilari = int(input("Kaynak Sayısı Giriniz: "))

#işlem sayılarını belirledik
islem_sayilari = [20,30,50,80,100]

#başlangıçta her işlemin talep edebileceği max kaynak sayısı
max_kaynak_sayilari = []
for _ in range(kaynak_sayilari):
    max_kaynak_sayilari.append(random.randint(1,kaynak_sayilari))


print("Max Kaynak Sayıları: ", max_kaynak_sayilari)
print("*****")

#başlangıçta her işlemin sahip olabileceği kaynak miktarı
mevcut_kaynaklar = []
for i in range(kaynak_sayilari):
    #her bir dönüşte 1'den max_kaynak_sayilari listesinin i. elemanına kadar olan random sayıların listesidir
    mevcut_kaynaklar.append(random.randint(1,max_kaynak_sayilari[i]))


print("Mevcut Kaynaklar: ", mevcut_kaynaklar)
print("*****")

#işlem nesnesi oluşturduk
class Islem:
    def __init__(self,islem_id):
        #işlem özelliklerini belirledik
        self.islem_id = islem_id
        self.talep = []

        for i in range(kaynak_sayilari):
            self.talep.append(random.randint(1,max_kaynak_sayilari[i]))

        #işlemin tuttuğu kaynakları 0 olan bi listeden oluşturduk
        self.tutulan_kaynaklar = [0] * kaynak_sayilari

##islem_1 = Islem(1)
##print("İşlem ID: ",islem_1.islem_id)
##print("İşlemin talepleri: ", islem_1.talep)
##print("İşlemin tuttuğu kaynaklar: ",islem_1.tutulan_kaynaklar)
##print("****")

#dağılım türlerine göre, dağılımların listesini oluşturma
def rastgele_dagitim(kaynak_sayilari, dagilim_turu):
    if dagilim_turu == "uniform":
        uniform = []
        for i in range(kaynak_sayilari):
            uniform.append(random.randint(1, kaynak_sayilari))
        return uniform

    elif dagilim_turu == "normal":
        normal = []
        for i in range(kaynak_sayilari):
            ortalama = kaynak_sayilari / 2
            standart_sapma = kaynak_sayilari / 6
            normal.append(max(1, round(random.gauss(ortalama, standart_sapma))))
        return normal

    elif dagilim_turu == "custom":
        # Kullanıcının girdiği kaynak sayısına göre aralıkları belirle
        araliklar = [i + 1 for i in range(kaynak_sayilari)]
        custom = []
        for i in range(kaynak_sayilari):
            custom.append(random.choice(araliklar))
        return custom



print("Uniform dağılım: ",rastgele_dagitim(kaynak_sayilari,"uniform"))
print("Normal dağılım: ",rastgele_dagitim(kaynak_sayilari,"normal"))
print("Custom dağılım: ",rastgele_dagitim(kaynak_sayilari,"custom"))
print("*****")

##islemler = []
##for i in range(kaynak_sayilari):
##    islemler.append(Islem(i))

#deadlock durumu oluşturduk
def deadlock_olustur(islemler, dagilim_turu):
    #işlemler classıyla oluşturulan işlemler listesinden rastgele eleman çektik
    islem = random.choice(islemler)

    #dağıtım türüne göre talep oluşturduk
    talep = rastgele_dagitim(kaynak_sayilari, dagilim_turu)

    #deadlock durumu oluşturduk
    for i in range(kaynak_sayilari):
        mevcut_kaynaklar[i] -= talep[i]
        islem.tutulan_kaynaklar[i] += talep[i]


##    print(islem.tutulan_kaynaklar, talep)

##    print("Talep sayıları: ",talep)
##    print("Güncel mevcut kaynaklar: ",mevcut_kaynaklar)
##    print("İşlemin güncel tutulan kaynakları: ",islem.tutulan_kaynaklar)


##deadlock_olustur(islemler, "uniform")

#ön tahsis algoritması
def preallocation(islemler):
    for islem in islemler:
        if sum(islem.tutulan_kaynaklar) == sum(islem.talep):
            for i in range(kaynak_sayilari):
                mevcut_kaynaklar[i] += islem.tutulan_kaynaklar[i]
            islem.tutulan_kaynaklar = [0] * kaynak_sayilari

#zaman aşımı
def timeout(islemler):
    for islem in islemler:
        if sum(islem.tutulan_kaynaklar) == sum(islem.talep):
            for i in range(kaynak_sayilari):
                mevcut_kaynaklar[i] += islem.tutulan_kaynaklar[i]
            islem.tutulan_kaynaklar = [0] * kaynak_sayilari
        else:
            islem.tutulan_kaynaklar = [0] * kaynak_sayilari

#wait die algoritması
def wait_die(islemler):
    for islem in islemler:
        #işlem talepleri tamamen karşılanmışsa
        if sum(islem.tutulan_kaynaklar) == sum(islem.talep):
            for i in range(kaynak_sayilari):
                mevcut_kaynaklar[i] += islem.tutulan_kaynaklar[i]  #işlem tarafından tutulan kaynak serbest kalır
            islem.tutulan_kaynaklar = [0] * kaynak_sayilari #işlem tarafından tutulan kaynaklar sıfırlanır
        else:
            if islem_genclik_kontrolu(islem):  #işlem gençse işlem tarafından tutulan kaynakları serbest bırakır
                for i in range(kaynak_sayilari):
                    mevcut_kaynaklar[i] += islem.tutulan_kaynaklar[i]
                islem.tutulan_kaynaklar = [0] * kaynak_sayilari #işlem tarafından tutulan kaynaklar sıfırlanır

#wound wait algoritması
def wound_wait(islemler):
    for islem in islemler:
        if sum(islem.tutulan_kaynaklar) == sum(islem.talep):
            for i in range(kaynak_sayilari):
                mevcut_kaynaklar[i] += islem.tutulan_kaynaklar[i] #işlem tarafından tutulan kaynak serbest kalır
            islem.tutulan_kaynaklar = [0] * kaynak_sayilari #işlem tarafından tutulan kaynaklar sıfırlanır
        else:
            if islem_genclik_kontrolu(islem):  #işlem gençse işlem tarafından tutulan kaynakları serbest bırakır
                for i in range(kaynak_sayilari):
                    #işlem gençse işlem tarafından tutulan kaynakları yarısını serbest bırak, yarısını tutulan olarak bırak
                    mevcut_kaynaklar[i] += islem.tutulan_kaynaklar[i] // 2
                    islem.tutulan_kaynaklar[i] = islem.tutulan_kaynaklar[i] // 2

# Genç-yaşlı kontrol fonksiyonu
def islem_genclik_kontrolu(islem):

    #eğer işlem ID'si çiftse, işlemi genç; tekse, işlem yaşlı kabul ettik

    if islem.islem_id % 2 == 0:

        return True
    else:

        return False

#bankacı algoritması
def bankers(islemler):
    mevcut_kaynaklar_kopya = mevcut_kaynaklar.copy() #mevcut kaynakların kopyasını aldık
    #her bir işlem nesnesinin tuttuğu kaynakları aldık
    islemin_tuttugu_kaynaklar = []
    for islem in islemler:
        islemin_tuttugu_kaynaklar.append(islem.tutulan_kaynaklar.copy())

    for islem in islemler:
        #tüm listeleri kontrol ettik
        for i in range(kaynak_sayilari):
            if mevcut_kaynaklar_kopya[i] >= islem.talep[i] - islemin_tuttugu_kaynaklar[islem.islem_id][i]:
                for j in range(kaynak_sayilari):
                    mevcut_kaynaklar_kopya[j] += islemin_tuttugu_kaynaklar[islem.islem_id][j]
                    islemin_tuttugu_kaynaklar[islem.islem_id][j] = 0

            else:
                islem.tutulan_kaynaklar = islemin_tuttugu_kaynaklar[islem.islem_id]


#algoritmalara göre simülasyonu çalıştırıp ortalama zamanı return ettirdik
def sim_calistir(algoritma, islem_sayilari, dagilim_turu, tekrar_sayisi = 100):
    calisma_suresi = 0.0

    islemler = []
    for tekrar in range(tekrar_sayisi):

        #işlem sayıları kadar Islem nesnesi oluşturduk
        for islem_id in range(islem_sayilari):
            islemler.append(Islem(islem_id))

            #işlemler classıyla oluşturulan işlemler ve dağılımı ile deadlock oluşturduk
            deadlock_olustur(islemler,dagilim_turu)

            #algoritmanın çalışma süresini hesaplamak için çalışmaya başladığı zaman ve bittiği zamanı aldık
            baslangic_zamani = time.time()
            algoritma(islemler)
            bitis_zamani = time.time()

            #çalışma süresi ise başlangıç ve bitiş farkı olacak
            calisma_suresi += bitis_zamani - baslangic_zamani

        ortalama_calisma_suresi = calisma_suresi / tekrar_sayisi
        return ortalama_calisma_suresi

algoritmalar = [bankers, preallocation, timeout, wound_wait, wait_die]
dagitim_turleri = ['uniform', 'normal', 'custom']

plt.figure(figsize=(15, 15 * len(dagitim_turleri)))


for idx, dagitim_turu in enumerate(dagitim_turleri, 1):
    plt.subplot(len(dagitim_turleri), 1, idx)
    sonuclar = {}

    for algoritma in algoritmalar:
        calisma_zamanlari = []
        for islem_sayisi in islem_sayilari:
            ortalama_calisma_zamani = sim_calistir(algoritma, islem_sayisi, dagilim_turu=dagitim_turu)
            calisma_zamanlari.append(ortalama_calisma_zamani)
            print(f"{algoritma.__name__} - {islem_sayisi} İşlem - {dagitim_turu.capitalize()} Dağılım: Ortalama Çözüm Süresi {ortalama_calisma_zamani:.6f} saniye")

        sonuclar[f"{algoritma.__name__}"] = calisma_zamanlari
        plt.plot(islem_sayilari, calisma_zamanlari, label=f"{algoritma.__name__}")

    plt.title(f"Deadlock Çözüm Algoritmalarının Performans Karşılaştırması - {dagitim_turu.capitalize()} Dağılım")
    plt.xlabel("İşlem Sayısı")
    plt.ylabel("Ortalama Çözüm Süresi (saniye)")
    plt.legend()


plt.tight_layout()
plt.show()








