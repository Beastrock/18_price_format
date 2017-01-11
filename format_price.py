import argparse
import re
import locale


def get_args():
    parser = argparse.ArgumentParser(description="price-formatter function")
    parser.add_argument("--price", "-p", required=True,
                        help="input string, integer or float type price value")
    return parser.parse_args()


def format_price(price):
    price_format_template = r"\d+,?.?\d*$"
    if not isinstance(price, (str, int, float)):
        raise TypeError("Invalid price type. Enter string, int or float.")
    if re.match(price_format_template, str(price)) is None:
        raise ValueError("Invalid price value format.")
    else:
        price = str(price).replace(",", ".")
    loc = locale.getlocale()
    locale.setlocale(locale.LC_ALL, 'English_United States.1252')
    price = locale.format_string("%d", float(price), grouping=True).replace(",", " ")
    locale.setlocale(locale.LC_ALL, loc)
    return price


if __name__ == "__main__":
    args = get_args()
    print(format_price(args.price))
