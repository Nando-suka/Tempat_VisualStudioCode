# Pengantar Unit Testing dalann Python
import unittest

def koneksi_ke_db():
    print('[terhubung ke db]')

def putus_koneksi_ke_db(db):
    print("[tidak terhubung ke db {}]".format(db))

class User:
    username = ""
    aktif = False

    def __init__ (self, db, username):
        self.username = username

    def set_aktif (self):
        self.aktif = True

class TestUser(unittest.TestCase):

    # Test Case 1
    def test_user_default_not_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "dicoding")
        self.assertFalse(dicoding.aktif) # tidak aktif secara default
        putus_koneksi_ke_db(db)

    # Test Case 2
    def test_user_is_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "dicoding")
        dicoding.set_aktif()
        putus_koneksi_ke_db(db)

if __name__ == "__main__":
    unittest.main()