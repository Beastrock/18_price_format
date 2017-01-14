import argparse
import re


def get_args():
    parser = argparse.ArgumentParser(description="price-formatter function")
    parser.add_argument("--price", "-p", required=False,
                        help="input string, integer or float type price value")
    return parser.parse_args()


def format_price(price):
    precision = 2
    price_format_template = r"\d+([.,])?\d*$"
    price_with_non_zero_float_part_template = r"\d+[.,]0{0,1}[^0]\d*$"
    if not isinstance(price, (str, int, float)):
        raise TypeError("Invalid price type. Enter string, int or float.")
    if re.match(price_format_template, str(price)) is None:
        raise ValueError("Invalid price value format.")
    price = str(price)
    int_part = int(re.split("[,.]", price)[0])
    formatted_int_part = str(format(int_part, ',.00f').replace(',', ' '))
    if re.match(price_with_non_zero_float_part_template, price) is not None:
        float_part = re.split("[,\.]", price)[1]
        if len(float_part) >= 2:
            formatted_float_part = float_part[:precision]
        else:
            formatted_float_part = "{}0".format(float_part)
        price = "{}.{}".format(formatted_int_part, formatted_float_part)
        return price
    else:
        price = formatted_int_part
        return price


if __name__ == "__main__":
    args = get_args()
    print(format_price(22000333.40))
