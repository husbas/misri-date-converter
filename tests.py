import unittest
from converter import convert
from datetime import datetime
class TestConverter(unittest.TestCase):
    def test_converts(self):
        self.assertEqual(convert(datetime(1984,12,30)),"07/04/1405")
        self.assertEqual(convert(datetime(1983,11,10)),"05/02/1404")
        self.assertEqual(convert(datetime(1980,7,22)),"10/09/1400")
        self.assertEqual(convert(datetime(1953,5,19)),"06/09/1372")
        self.assertEqual(convert(datetime(2010,5,15)),"02/06/1431")


if __name__ == '__main__':
    unittest.main()

# def main():
#     d = input("Enter date to convert (dd/mm/yyyy): ")
#     m = convert(datetime.strptime(d, "%d/%m/%Y"))
#     print(m)

# if __name__ == "__main__":
#     main()
