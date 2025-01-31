package main

import "fmt"

func main() {
	fmt.Println("Nama Saya Fernando")

	// Menggunakan fungsi append
	var fruits = []string{"apel", "anggur", "pir"}
	var cfruits = append(fruits, "rambutan")

	fmt.Println(fruits)
	fmt.Println(cfruits)

	var nama string = "Fernando"

	if nama != "Fernando" {
		fmt.Println("Tidak Jelas")
	} else {
		fmt.Println("Ya itu nama nya.")
	}

	// Menggunakan variabel temporary pada percabangan

	var point = 8840.0

	if percent := point / 100; percent >= 100 {
		fmt.Printf("%.1f%s perfect \n", percent, "%" )
	} else if percent >= 70 {
		fmt.Printf("%.1%s good \n", percent, "%")
 	} else {
		fmt.Printf("%.1f%s  not bad\n", percent, "%")
	}

	fmt.Println()
	var pointDua = 6
	switch pointDua {
	case 8:
		fmt.Println("Perfect")
	case 7, 6, 5, 4:
		fmt.Println("Awesome")
	default:
		fmt.Println("Not Bad")
	}

	var pointTiga = 10
	switch pointTiga {
	case 8:
		fmt.Println("Sempurna")
	case 7, 6, 5, 4:
		fmt.Println("Baik")
	default:
		{
			fmt.Println("Tidak Buruk")
			fmt.Println("Kamu dapat melakukan nya lebih baik lagi")
		}
	}

	var pointEmpat = 7

	switch {
	case pointEmpat == 8:
		fmt.Println("Sempurna")
	case (pointEmpat < 8) && (pointEmpat > 3):
		fmt.Println("Bagus")
	default:
		{
			fmt.Println("Tidak Buruk")
			fmt.Println("Kamu perlu lebih baik lagi")
		}
	}

	var harga = 10000

	switch {
	case harga > 20000:
		fmt.Println("Mahal Amat")
	case (harga > 0 && harga < 20000):
		fmt.Println("Standar")
	default:
		fmt.Println("Input tidak normal") 
	}

	var pointLima = 6

	switch {
	case pointLima == 8:
		fmt.Println("Sempurna")
	case (pointLima < 8) && (pointLima > 3):
		fmt.Println("Bagus")
		fallthrough
	case pointLima < 5:
		fmt.Println("Kamu butuh perbaikan")
	default:
		{
			fmt.Println("Tidak buruk")
			fmt.Println("Kamu butuh belajar lebih giat lagi")
		}
	}
	
	// Seleksi kondisi bersarang
	var pointEnam = 10

	if pointEnam > 7 {
		switch pointEnam {
		case 10:
			fmt.Println("Sempurna!")
		default:
			fmt.Println("Bagus!")
		}
	} else {
		if pointEnam == 5 {
			fmt.Println("Tidak Buruk")
		} else if pointEnam == 3 {
			fmt.Println("Terus Mencoba")
		} else {
			fmt.Println("Kamu dapat melakukannya")
			if pointEnam == 0 {
				fmt.Println("Coba lebih keras")
			}
		}
	}

	var daerah string = "Kalideres"
	var daerahDua string = "Bulakteko"

	if daerah == "Kalideres" {
		fmt.Printf("Kamu berada di daerah Kalideres\n")
		switch {
		case daerahDua == "Kampung Bali":
			fmt.Println("Saya berada di Kampung Bali")
		case daerahDua == "Kodam":
			fmt.Println("Saya berada di Kodam")
		case daerahDua == "Bulakteko":
			fmt.Println("Saya berada di Bulakteko")
		default:
			{
				fmt.Println("Tidak hadir")
				fmt.Println("Kamu Tersesat")
			}
		}
	} else {
		fmt.Println("Kamu tidak tau berada di mana.\n")
	}

	// Perulangan
	for i := 0; i < 5; i++ {
		fmt.Println("Angka", i)
	}

	for i := 10; i > 5; i-- {
		fmt.Println("Angka", i)
	}

	var j = 0

	for j < 4 {
		fmt.Println("Angka", j)
		j++
	}

	var j1 = 0

	for {
		fmt.Println("Angka", j1)
		j1++

		if j1 == 3 {
			break
		}
	}

	var xs = "123"

	for i, v := range xs {
		fmt.Println("Index=", i, "Values=", v)

	}

	var xsa = "456"
	var xsb = "122"

	for i, v := range xsb {
		fmt.Println("Index:", i, "Nilai:", v)
	}
	for i, v := range xsa {
		fmt.Println("Index=", i, "Values=", v)
	}

	var ys = [5]int{100, 200, 300, 400, 500}
	for _, v := range ys {
		fmt.Println("Values=", v)
	}

	var ysa = [5]int8{28, 38, 48, 58, 68}
	for index, v := range ysa {
		fmt.Println("Indeks=", index, "Nilai=", v)
	}

	var zs = ys[0:2]
	for _, v := range zs {
		fmt.Println("Values=", v)
	}

	var kvs = map[byte]int{'a': 0, 'b': 1, 'c': 2}
	for k, v := range kvs {
		fmt.Println("Kunci", k, "value", v)
	}

	var kvb = map[byte]int{'c': 100, 'd': 101, 'e': 102}
	for k, v := range kvb {
		fmt.Println("Kunci:", k, "Nilai:", v)
	}

	var kvc = map[int]string{1: "Tuhan Yesus", 2: "Fernando", 3: "Chelsea FC", 4: "So Okuno"}
	for _, v := range kvc {
		fmt.Println("Daftar =", v)
	}

	for range kvs {
		fmt.Println("Done")
	}

	for i := range 5 {
		fmt.Println(i)
	}

	for k := range 20 {
		fmt.Println(k)
	}

	for i := 1; i <= 10; i++ {
		if i % 2 == 1 {
			continue
		}

		if i > 8 {
			break
		}

		fmt.Println("Angka", i)
	}

	for i := 1; i <= 20; i++ {
		if (i >= 10 && i <= 13) {
			continue
		}

		fmt.Println("Angka", i)
	}

	for i := 0; i < 5; i++ {
		for j := i; j < 5; j++ {
			fmt.Print(j, " ")
		}

		fmt.Println()
	}

}