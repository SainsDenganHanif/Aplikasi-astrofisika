import modul.Modul_Bintang
import modul.Modul_Global

while True:
    M = input("Masukkan massa bintang (0.08 M☉ < M < 200M☉) : ")
    if modul.Modul_Global.Validasi_Input(M,0.08,200) == True:
        M = float(M)
        break

Bintang =  modul.Modul_Bintang.Model_gabungan(M) #Hitung sekali biar efisien

L = Bintang.get("L")
T = Bintang.get("T")
R = Bintang.get("R")
Tms = Bintang.get("Tms")

print(f"Bintang ini memiliki massa {M:,.2f} M☉")
print(f"Bintang ini memiliki Kecerahan {L:,.3f} L☉")
print(f"Bintang ini memiliki suhu {T:,.0f} K")
print(f"Bintang ini memiliki Jari-jari {R:,.3f} R☉")
print(f"Bintang ini akan menjadi bintang deret utama selama {10.9*M/L:,.2f} Miliar tahun")