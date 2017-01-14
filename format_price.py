import argparse
import re


def get_args():
    parser = argparse.ArgumentParser(description="price-formatter function")
    parser.add_argument("--price", "-p", required=True,
                        help="input string, integer or float type price value")
    return parser.parse_args()


def format_price(price):
    precision = 2
    price_format_template = r"\d+([.,])?\d*$"
    if not isinstance(price, (str, int, float)):
        raise TypeError("Invalid price type. Enter string, int or float.")
    if re.match(price_format_template, str(price)) is None:
        raise ValueError("Invalid price value format.")
    price = str(price).replace(",", ".")
    int_part = int(price.split(".")[0])
    formatted_int_part = str(format(int_part, ",.0f").replace(",", " "))
    if float(price).is_integer():
        price = formatted_int_part
        return price
    else:
        float_part = price.split(".")[1]
        if len(float_part) >= precision:
            formatted_float_part = float_part[:precision]
        else:
            formatted_float_part = "{}{}".format(float_part, "0" * (precision - 1))
        price = "{}.{}".format(formatted_int_part, formatted_float_part)
        return price


if __name__ == "__main__":
    args = get_args()
    print(format_price(args.price))
