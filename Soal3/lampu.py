class Lampu:
    """
    Kelas untuk merepresentasikan sebuah lampu.

    Atribut kelas:
        jumlah_lampu (int): Banyaknya objek Lampu yang sudah dibuat.
                            Awal = 0, bertambah 1 tiap objek dibuat.

    Atribut instance:
        nama (str)      : Nama lampu.
        aktif (bool)    : Status lampu. Awal = False.
        kecerdasan (int): Tingkat kecerdasan/kecerahan. Awal = 0.
    """

    jumlah_lampu = 0

    def __init__(self, nama):
        self.nama = nama
        self.aktif = False
        self.kecerdasan = 0
        Lampu.jumlah_lampu += 1

    def nyalakan(self):
        self.aktif = True
        self.kecerdasan = 100

    def matikan(self):
        self.aktif = False
        self.kecerdasan = 0

    def atur(self, nilai):
        if self.aktif and 0 <= nilai <= 100:
            self.kecerdasan = nilai

    def __str__(self):
        """
        Representasi teks objek Lampu.
        Format: "Lampu <nama>: aktif = <aktif>, kecerahan = <kecerdasan>"
        """
        return f"Lampu {self.nama}: aktif = {self.aktif}, kecerahan = {self.kecerdasan}"