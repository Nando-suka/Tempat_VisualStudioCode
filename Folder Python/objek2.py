class Bank:
    def __init__(self,nasabah,saldo_bank,suku_bunga):
        self.nasabah = nasabah
        self.saldo_bank = float(saldo_bank)
        self.suku_bunga = float(suku_bunga)


Nasabah1 = Bank("Fernando",1500210,20.0)

# class anjing
class Dog:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def run(self):
        print("Dog running . . .")

ozzy = Dog("Ozzy", 2)
skippy = Dog("Skippy", 12)
filou = Dog("Filou", 8)
ozzy.doginfo()
ozzy.bark()
ozzy.run()