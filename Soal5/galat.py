def galat_absolut(hasil, acuan):
    return abs(hasil - acuan)


def galat_relatif(hasil, acuan):
    if acuan == 0:
        raise ValueError("acuan tidak boleh 0")
    return abs(hasil - acuan) / abs(acuan) * 100


# Hasil rata-rata yang dicetak program (2 desimal)
hasil = 13.57
acuan = 13.5714
toleransi = 0.5  # persen

ga = galat_absolut(hasil, acuan)
gr = galat_relatif(hasil, acuan)
status = "LULUS" if gr <= toleransi else "TIDAK LULUS"

print(f"Hasil program : {hasil}")
print(f"Acuan         : {acuan}")
print(f"Galat absolut : {ga:.6f}")
print(f"Galat relatif : {gr:.6f}%")
print(f"Toleransi     : {toleransi}%")
print(f"Status        : {status}")