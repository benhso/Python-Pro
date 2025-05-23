meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Bir şakaya karşılık cevap",
    "SHEESH": "Onaylamamak",
    "CREEPY": "Korkunç",
    "AGGRO": "Agresifleşmek/sinirlenmek"
}


word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


if word in meme_dict: # veya meme_dict.keys() kullanabiliriz, ama direkt sözlük kontrolü daha kısadır
    # Kelime eşleşiyorsa
    print(meme_dict[word]) # Kelimenin anlamını yazdır
else:
    # Kelime eşleşmiyorsa
    print("Üzgünüm, bu kelime sözlüğümüzde yok.") # Kullanıcıya bilgi ver


for _ in range(5): # 5 kelime sormak için
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ").upper() # .upper() ile girişi otomatik büyük harfe çeviriyoruz
if word in meme_dict:
    print("Anlamı: {meme_dict[word]}")
else:
    print("Üzgünüm, bu kelime sözlüğümüzde yok.")


print("Merhaba! Meme sözlüğüne hoş geldiniz.")
print("Anlamını merak ettiğiniz bir kelime yazın (büyük/küçük harf fark etmez) veya çıkmak için 'ÇIKIŞ' yazın.")

while True: # Kullanıcı çıkış yapana kadar döngü devam eder
    word = input("Kelimeyi yazın: ").upper() # Kullanıcının girişini büyük harfe çevir

    if word == "ÇIKIŞ":
        print("Güle güle!")
        break # Döngüden çık

    if word in meme_dict:
        print("'{word}' kelimesinin anlamı: {meme_dict[word]}")
    else:
        print("Üzgünüm, bu kelime sözlüğümüzde yok. Başka bir kelime deneyin.")
