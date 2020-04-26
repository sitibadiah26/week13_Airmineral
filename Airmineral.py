class Airmineral:

    def __init__(self, urutan, hargabeli, banyakpembelian, hargajual, laku):
        self.urutan=urutan
        self.hargabeli=hargabeli
        self.banyakpembelian=banyakpembelian
        self.hargajual=hargajual
        self.laku=laku

    def tampilkan_macam(self):
        if self.urutan==1:
            print("AQUINDO")
        elif self.urutan==2:
            print("CLEO")
        elif self.urutan==3:
            print("CLUB")
        elif self.urutan==4:
            print("LE MINERAL")
        elif self.urutan==5:
            print("AQUA")
        else:
            print("Air Mineral tidak tersedia")
            
    def biaya_beli(self):
        if self.urutan==1:
            bayar=self.hargabeli*self.banyakpembelian
            print("Harga satu botol AQUINDO adalah", self.hargabeli)
            print("Karena beli sebanyak", self.banyakpembelian)
            print("maka harus membayar", bayar)
        elif self.urutan==2:
            bayar=self.hargabeli*self.banyakpembelian
            print("Harga satu botol CLEO adalah", self.hargabeli,)
            print("Karena beli sebanyak", self.banyakpembelian)
            print("maka harus membayar", bayar)
        elif self.urutan==3:
            bayar=self.hargabeli*self.banyakpembelian
            print("Harga satu botol CLUB adalah", self.hargabeli)
            print("Karena beli sebanyak", self.banyakpembelian)
            print("maka harus membayar", bayar)
        elif self.urutan==4:
            bayar=self.hargabeli*self.banyakpembelian
            print("Harga satu botol LE MINERAL adalah", self.hargabeli)
            print("Karena beli sebanyak", self.banyakpembelian)
            print("maka harus membayar", bayar)
        elif self.urutan==5:
            bayar=self.hargabeli*self.banyakpembelian
            print("Harga satu botol AQUA adalah", self.hargabeli)
            print("Karena beli sebanyak", self.banyakpembelian)
            print("maka harus membayar", bayar)
        else:
            print("Jajanan tidak tersedia")

    def perkiraan_untung(self):
        if self.urutan==1:
            untung=self.hargajual-self.hargabeli
            semua=(self.hargajual-self.hargabeli)*self.banyakpembelian
            print("Setiap botol AQUINDO dibeli dengan harga", self.hargabeli)
            print("dijual dengan harga", self.hargajual)
            print("dengan demikian keuntungan perbotolnya adalah", untung)
        elif self.urutan==2:
            untung=self.hargajual-self.hargabeli
            print("Setiap botol CLEO dibeli dengan harga", self.hargabeli)
            print("dan dijual dengan harga", self.hargajual)
            print("dengan demikian keuntungan perbotolnya adalah", untung)
        elif self.urutan==3:
            untung=self.hargajual-self.hargabeli
            print("Setiap botol CLUB dibeli dengan harga", self.hargabeli)
            print("dan dijual dengan harga", self.hargajual)
            print("dengan demikian keuntungan perbotolnya adalah", untung)
        elif self.urutan==4:
            untung=self.hargajual-self.hargabeli
            print("Setiap botol LE MINERAL dibeli dengan harga", self.hargabeli)
            print("dan dijual dengan harga", self.hargajual)
            print("dengan demikian keuntungan perbotolnya adalah", untung)
        elif self.urutan==5:
            untung=self.hargajual-self.hargabeli
            print("Setiap botol AQUA dibeli dengan harga", self.hargabeli)
            print("dan dijual dengan harga", self.hargajual)
            print("dengan demikian keuntungan perbotolnya adalah", untung)
        else:
            print("Keuntungan tidak tersedia")

    def untung_asli(self):
        if self.urutan==1:
            sebenarnya=self.laku*(self.hargajual-self.hargabeli)
            print("Karena AQUINDO laku sebanyak", self.laku)
            print("maka keuntungannya adalah", sebenarnya)
        elif self.urutan==2:
            sebenarnya=self.laku*(self.hargajual-self.hargabeli)
            print("Karena CLEO laku sebanyak", self.laku)
            print("maka keuntungannya adalah", sebenarnya)
        elif self.urutan==3:
            sebenarnya=self.laku*(self.hargajual-self.hargabeli)
            print("Karena CLUB laku sebanyak", self.laku)
            print("maka keuntungannya adalah", sebenarnya)
        elif self.urutan==4:
            sebenarnya=self.laku*(self.hargajual-self.hargabeli)
            print("Karena LE MINERAL laku sebanyak", self.laku)
            print("maka keuntungannya adalah", sebenarnya)
        elif self.urutan==5:
            sebenarnya=self.laku*(self.hargajual-self.hargabeli)
            print("Karena AQUA laku sebanyak", self.laku)
            print("maka keuntungannya adalah", sebenarnya)
        else:
            print("Air Mineral tidak tersedia")
