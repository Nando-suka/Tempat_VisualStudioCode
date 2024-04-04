#program untuk cek tahun kabisat`
number_of_year = int(input("Masukkan tahun yang di inginkan? "))
year_input = []
for i in range(0, number_of_year):
  year_input.append(int(input("Masukkan tahun = ")))
  if (number_of_year / 100):
     print(f'Termasuk century year' + number_of_year)
     if (number_of_year / 400):
        print(f'Termasuk tahun kabisat' + number_of_year)
#Jika tahun dapat dibagi 100 maka termasuk century year
#century year dapat dibagi 400 maka tahun tersebut adalah tahun kabisat
for i in year_input:
    if (year_input / 400):
     print("Bukan Century Year")
     res = 'Kabisat'
     print(res)
#Jika tahun tidak dapat dibagi 400 maka bukan century year
#bukan century year jika dapat dibagi 4 maka tahun tersebut adalah tahun kabisat
    #.......
    res ='Kabisat'
#jika kedua syarat diatas tidak memenuhi maka tahun tersebut bukan tahun kabisat
else:
   res = 'bukan kabisat'
   print(res)
#......