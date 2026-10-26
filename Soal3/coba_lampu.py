from lampu import Lampu

# Buat dua objek
lp1 = Lampu("L1")
lp2 = Lampu("L2")

# Nyalakan lp1 dan atur kecerahan jadi 60
lp1.nyalakan()
lp1.atur(60)

# Cetak objek (memakai __str__) dan jumlah lampu
print(lp1)
print(lp2)
print("jumlah lampu: ",Lampu.jumlah_lampu)