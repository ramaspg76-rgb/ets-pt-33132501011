def baca_log(nama_file):
    valid = []
    ditolak = []
    with open(nama_file, "r", encoding="utf-8") as f:
        for nomor, line in enumerate(f, start=1):
            if nomor == 1:
                continue
            isi = line.rstrip("\n")
            bagian = isi.split(",")
            if len(bagian) != 2:
                ditolak.append({"baris": nomor, "isi": isi, "alasan": "jumlah kolom bukan 2"})
                continue
            waktu = bagian[0].strip()
            debit_str = bagian[1].strip()
            try:
                debit = float(debit_str)
            except ValueError:
                ditolak.append({"baris": nomor, "isi": isi, "alasan": "debit bukan angka"})
                continue
            if not (5 <= debit <= 25):
                ditolak.append({"baris": nomor, "isi": isi, "alasan": f"debit {debit} di luar rentang 5-25"})
                continue
            valid.append({"baris": nomor, "waktu": waktu, "debit": debit})
    return valid, ditolak


valid, ditolak = baca_log("log_debit.csv")
print("Jumlah data valid   :", len(valid))
print("Jumlah data ditolak :", len(ditolak))
print("\nData ditolak:")
for d in ditolak:
    print(f"- Baris {d['baris']} | isi: {d['isi']} | alasan: {d['alasan']}")
rata = sum(d["debit"] for d in valid)/len(valid) if valid else 0
print(f"\nRata-rata data valid: {rata:.2f}")