username = input("masukkan username: ")
password = input("masukkan password: ")

username_from_db = "Fernando"
password_from_db = "41523010038"

if username == username_from_db:
    if password == password_from_db:
        print("Username dan Password cocok")
    else:
        print("Username atau Password salah")
else:
    print("User tidak terdaftar")

