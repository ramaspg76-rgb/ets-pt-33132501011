from debit import hitung_rata_rata, cari_terendah, cek_status

# --- Pemanggilan fungsi dengan data tetap ---
print("hitung_rata_rata([10, 20, 30])       =", hitung_rata_rata([10, 20, 30]))
print("cari_terendah([12.5, 14.0, 11.0])    =", cari_terendah([12.5, 14.0, 11.0]))

# --- Membaca satu nilai debit dari pengguna ---
nilai = float(input("Masukkan nilai debit: "))
print("cek_status(", nilai, ")              =", cek_status(nilai))