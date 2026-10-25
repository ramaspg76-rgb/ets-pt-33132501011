data_debit = [12.5, 14.0, 13.5, 15.0, 11.0]


def hitung_rata_rata(data):
    """
    Menghitung rata-rata dari sekumpulan nilai debit.

    Input:
        data (list of int/float): Daftar nilai debit. Tidak boleh kosong.

    Output:
        float: Rata-rata nilai debit, dihitung dari jumlah seluruh
               elemen dibagi banyaknya elemen (len(data)).
    """
    total = 0
    for i in range(len(data)):
        total = total + data[i]
    return total / len(data)


def cari_terendah(data):
    """
    Mencari nilai debit terendah dari sekumpulan nilai debit.

    Input:
        data (list of int/float): Daftar nilai debit. Tidak boleh kosong.

    Output:
        int/float: Nilai terkecil dari data, yaitu hasil perbandingan
                   elemen pertama dengan setiap elemen berikutnya.
    """
    terendah = data[0]
    for nilai in data:
        if nilai < terendah:
            terendah = nilai
    return terendah


def cek_status(debit):
    """
    Menentukan status kategori debit berdasarkan ambang batas.

    Input:
        debit (int/float): Satu nilai debit yang akan diperiksa.

    Output:
        str: Status kategori debit, salah satu dari:
             - "RENDAH" jika debit < 10
             - "NORMAL" jika 10 <= debit <= 20  (10 dan 20 termasuk NORMAL)
             - "TINGGI" jika debit > 20
    """
    if debit < 10:
        return "RENDAH"
    elif debit <= 20:
        return "NORMAL"
    else:
        return "TINGGI"


if __name__ == "__main__":
    rata = hitung_rata_rata(data_debit)
    print("Rata-rata :", rata)
    print("Terendah  :", cari_terendah(data_debit))
    print("Status    :", cek_status(rata))