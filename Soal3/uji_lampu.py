from lampu import Lampu

# 1. Buat objek
lampu = Lampu("L1")
print("=== State Awal ===")
print("aktif      :", lampu.aktif)
print("kecerdasan :", lampu.kecerdasan)  # kecerahan

# 2. Nyalakan
lampu.nyalakan()
print("\n=== Setelah nyalakan() ===")
print("aktif      :", lampu.aktif)
print("kecerdasan :", lampu.kecerdasan)

# 3. Tiga nilai berturut-turut
for i in range(1, 4):
    nilai = float(input(f"\nMasukkan nilai kecerahan ke-{i}: "))
    lampu.atur(nilai)
    print(f"=== Setelah atur({nilai}) ===")
    print("aktif      :", lampu.aktif)
    print("kecerdasan :", lampu.kecerdasan)

# 4. Matikan
lampu.matikan()
print("\n=== Setelah matikan() ===")
print("aktif      :", lampu.aktif)
print("kecerdasan :", lampu.kecerdasan)