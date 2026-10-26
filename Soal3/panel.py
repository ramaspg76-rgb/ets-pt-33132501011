from lampu import Lampu


class PanelLampu:
    """
    Panel yang MENYUSUN (komposisi) dua objek Lampu sebagai atributnya.

    Atribut:
        lampu_merah (Lampu): Objek Lampu dengan nama "merah".
        lampu_hijau (Lampu): Objek Lampu dengan nama "hijau".
    """

    def __init__(self):
        """
        Constructor: membuat panel beserta dua lampu di dalamnya.

        Input : tidak ada
        Output: tidak ada
        """
        self.lampu_merah = Lampu("merah")
        self.lampu_hijau = Lampu("hijau")

    def nyalakan_semua(self):
        """
        Menyalakan kedua lampu pada panel.

        Efek: lampu_merah dan lampu_hijau menjadi aktif (kecerahan 100).
        """
        self.lampu_merah.nyalakan()
        self.lampu_hijau.nyalakan()

    def tampilkan(self):
        """
        Menampilkan kondisi kedua lampu pada panel.

        Output: dua baris teks (hasil __str__ tiap Lampu).
        """
        print(self.lampu_merah)
        print(self.lampu_hijau)


if __name__ == "__main__":
    # Buat satu panel
    panel = PanelLampu()

    # Nyalakan semua lampu
    panel.nyalakan_semua()

    # Atur lampu_hijau menjadi 30
    panel.lampu_hijau.atur(30)

    # Tampilkan
    panel.tampilkan()