import re

PIN_PATTERN = re.compile(r"(?<!\d)[1-9]\d{5}(?!\d)")


def extract_pin_codes(text):
    return PIN_PATTERN.findall(text)


if __name__ == "__main__":
    data = """Pune - 411001
Mumbai - 400001
Delhi - 110001
Invalid PIN 41100"""

    print("Input:")
    print(data)
    print()

    pins = extract_pin_codes(data)

    print("Valid PIN codes:")
    for pin in pins:
        print(pin)