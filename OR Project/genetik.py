import random
class Bag:
    esyalar = ["telefon", "yüzük", "vazo", "tablet", "laptop", "bilezik", "forma", "ütü", "tost makinesi", "ansiklopedi"]
    fiyatlar = [170, 90, 50, 100, 200, 120, 350, 70, 90, 30]
    agirlik = [1, 0.2, 1.5, 1.3, 2, 2.3, 0.6, 2.8, 4, 3.5]
    maxBag = 7.5


    def __init__(self):
        self.cantaninIci = [random.randint(0, 1) for _ in range(10)]
        self.cantaninAgirligi, self.cantaninDegeri = self.agirliklariTopla()


    def agirliklariTopla(self):
        toplamDeger = sum(self.cantaninIci[i] * Bag.agirlik[i] for i in range(10))

        toplamFiyat = sum(self.cantaninIci[i] * Bag.fiyatlar[i] for i in range(10))

        return toplamDeger, toplamFiyat


    def duzelt(self):
        while self.cantaninAgirligi > Bag.maxBag:
            index = random.randint(0, len(self.cantaninIci) - 1)

            if self.cantaninIci[index] == 1:

                self.cantaninIci[index] = 0
                self.cantaninAgirligi -= Bag.agirlik[index]
                self.cantaninDegeri -= Bag.fiyatlar[index]


    @staticmethod
    def kontrolEt(populasyon):
        for canta in populasyon:
            if canta.cantaninAgirligi > Bag.maxBag:
                canta.duzelt()


    @staticmethod
    def printInfo(cantalar):
        for i, canta in enumerate(cantalar):
            if canta is None:
                break
            print(f"{i}.değerdeyim. değeri eşittir: {canta.cantaninDegeri} agirlik eşittir: {canta.cantaninAgirligi}")

    @staticmethod
    def populasyonOrtalama(populasyon):
        return sum(canta.cantaninDegeri for canta in populasyon) / len(populasyon)


    @staticmethod
    def yeniPopulasyon(populasyon):
        return [canta for canta in populasyon if Bag.populasyonOrtalama(populasyon) <= canta.cantaninDegeri]


    @staticmethod
    def enYuksekDeger(populasyon):
        return max(canta.cantaninDegeri for canta in populasyon)


    @staticmethod
    def caprazlama(populasyon):
        cantalariSecmeUstSinir = len(populasyon)
        olasilik = random.randint(0, 100)
        sayac = len(populasyon)

        while sayac < 100:
            deger1 = random.randint(0, cantalariSecmeUstSinir - 1)
            deger2 = random.randint(0, cantalariSecmeUstSinir - 1)
            child = Bag()
            child.cantaninIci = [populasyon[deger1].cantaninIci[i]
                                 if random.choice([True, False])
                                 else populasyon[deger2].cantaninIci[i] for i in range(10)]
            if olasilik > 85:
                Bag.mutasyon(child)
            child.cantaninAgirligi, child.cantaninDegeri = child.agirliklariTopla()
            populasyon.append(child)
            sayac += 1

        Bag.kontrolEt(populasyon)


    @staticmethod
    def indexlerList(degerSayisi):
        liste1 = list(range(10))
        liste2indexi = 0
        indexler = []

        for _ in range(degerSayisi):
            index = random.randint(0, len(liste1) - 1)
            if liste1[index] != -1:
                liste2indexi += 1
                indexler.append(liste1[index])
                liste1[index] = -1
            else:
                continue
        return indexler


    @staticmethod
    def mutasyon(canta):
        mutasyonSayisi = random.randint(1, 4)
        indexler = Bag.indexlerList(mutasyonSayisi)

        for index in indexler:
            canta.cantaninIci[index] = 1 if canta.cantaninIci[index] == 0 else 0


def main():
    b1 = [Bag() for _ in range(100)]

    for i in range(100):
        b1 = Bag.yeniPopulasyon(b1)
        Bag.caprazlama(b1)
        print("ortalama = {a}".format(a = Bag.populasyonOrtalama(b1)))
        print("en yüksek değeri = {b}".format(b = Bag.enYuksekDeger(b1)))

if __name__ == "__main__":
    main()
