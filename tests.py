import unittest
from format_price import format_price


class TestFormatPriceFunction(unittest.TestCase):
    def test_invalid_input_type_list(self):
        with self.assertRaises(TypeError):
            format_price([1, 2, 3])

    def test_invalid_input_format_negative_numbers(self):
        with self.assertRaises(ValueError):
            format_price(-3200)

    def test_invalid_input_format_string_with_letters(self):
        with self.assertRaises(ValueError):
            format_price("3200 rub.")

    def test_invalid_input_format_string_with_double_dots(self):
        with self.assertRaises(ValueError):
            format_price("3200.000.555")

    def test_invalid_input_format_string_with_double_commas(self):
        with self.assertRaises(ValueError):
            format_price("3200,000,000")

    def test_valid_input_type_string(self):
        price = format_price("22000333")
        self.assertEqual(price, "22 000 333")

    def test_valid_input_type_integer(self):
        price = format_price(10200300)
        self.assertEqual(price, "10 200 300")

    def test_valid_input_type_float(self):
        price = format_price(10000.999)
        self.assertEqual(price, "10 000")

    def test_valid_input_format_string_with_dot(self):
        price = format_price("22000333.555")
        self.assertEqual(price, "22 000 333")

    def test_valid_input_format_string_with_comma(self):
        price = format_price("22000333,555")
        self.assertEqual(price, "22 000 333")

    def test_independence_from_precision(self):
        price1 = format_price("1000.999")
        price2 = format_price("1000.9999")
        price3 = format_price("1000.99999")
        self.assertEqual((price1, price2, price3), ("1 000", "1 000", "1 000"))


if __name__ == "__main__":
    unittest.main()
