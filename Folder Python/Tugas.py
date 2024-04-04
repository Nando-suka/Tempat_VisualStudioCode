bintang = "*"

for i in range (0,5):
    #print(bintang)
    if i >= 0:
     for p in range (i):
        print(bintang, end=' ')
    print(bintang)

print()

i = 5
state = [5,4,3,2,1,0]
for i in state:
   if i <= 5:
      for p in range (i):
         print(bintang,end=' ')
   print(bintang)

print()

buah = ["Apel", "Jambu", "Mangga"]
for x in buah:
   print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 

angka = [5,10,15]
amka = [5,5,5]

# Menggunakan operasi decrement i = i - 1
i = 20
while i > 10:
   print(i)
   i-=1

class klubBola:
   
   def __init__ (self,klub,negara):
      self.klub = klub
      self.negara = negara
   
   def __str__ (self):
      return f"{self.klub} {self.negara}"


Klub1 = klubBola("Chelsea","Inggris")
Klub2 = klubBola("Real Madrid","Spanyol")
Klub3 = klubBola("Juventus","Italia")

print(Klub1)

class 