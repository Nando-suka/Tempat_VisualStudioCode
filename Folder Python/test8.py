# Pengantar Unit Testing dalam Python
import unittest

class TestStringMethods (unittest.TestCase):

    # Test Case Pertama
    def test_strip (self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')


    # Test Case Kedua
    def test_isalnum(self):
        self.assertTrue('cod1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())

    # test Case Ketiga
    def text_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)

        with self.assertRaises(ValueError):
            s.index('decode')

if __name__ == '__main__':
    unittest.main()
""" 
# Kelas TestStringMethods adalah sebuah kelas yang merupakan turunan (subclass) dari
class unitest. TestCase sehingga proses tes daaoat dduilangsungkan tanpa
banyak implementasi lain
 """

# Pada setiap metode yang dilakukan dari pihak penyelenggara maupun pihak panitia
# Tuntutan dari klien harus segera diselesaikan secara optimal dan penuh dengan rasa
# Tanggung jawab dari setiap orang yang memiliki kewajiban untuk memenuhhi hal tersevut

