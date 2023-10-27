def buat_kamus_pengganti():
    kamus_pengganti = {}
    while True:
        huruf = input("Masukkan huruf yang ingin diganti (atau tekan Enter untuk selesai): ")
        if not huruf:
            break
        huruf_pengganti = input(f"Masukkan huruf penggantinya untuk '{huruf}': ")
        kamus_pengganti[huruf] = huruf_pengganti
    return kamus_pengganti
pengganti = buat_kamus_pengganti()

def ganti_huruf(teks, pengganti):
    hasil = ''
    for huruf in teks:
        if huruf in pengganti:
            hasil += pengganti[huruf]
        else:
            hasil += huruf
    return hasil

teks_input = input("Masukkan teks: ")
teks_hasil = ganti_huruf(teks_input, pengganti)
print("Teks setelah diganti:", teks_hasil)
