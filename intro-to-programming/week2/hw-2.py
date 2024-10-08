tarih = input("Tarih:")
üniversite_adı = input("Üniversite Adı:")
fakülte_adı = input("Fakülte Adı:")
bölüm_adı = input("Bölüm Adı:")
öğrenci_no = input("Öğrenci No:")
öğretim_yılı = input("Öğretim Yılı:")
yarıyıl = input("Yarıyıl:")
ad = input("Ad:")
soyad = input("Soyad:")
tc_kimlik_no = input("TC Kimlik No:")
adres = input("Adres:")
tel = input("Tel:")
ekler = input("Ekler:")

result = f"""                                                     tarih: {tarih}
T.C.
{üniversite_adı} ÜNİVERSİTESİ
{fakülte_adı} Fakültesi Dekanlığına
Fakülteniz {bölüm_adı} Bölümü {öğrenci_no} numaralı öğrencisiyim. Ekte sunduğum
belgede belirtilen mazeretim gereğince {öğretim_yılı} Eğitim-Öğretim Yılı {yarıyıl}
yarıyılında öğrenime ara izni (kayıt dondurma) istiyorum.

    Bilgilerinizi ve gereğini arz ederim.

    İmza

Ad-Soyadı       : {ad} {soyad}
T.C. Kimlik No. : {tc_kimlik_no}
Adres           : {adres}
Tel.            : {tel}
Ekler           : {ekler}
"""

print(result)
