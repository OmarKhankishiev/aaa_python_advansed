from datetime import datetime
import sys


def my_write(string_text: str) -> None:
    if string_text != "\n":
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]: ")
        moded_text = timestamp + string_text
    else:
        moded_text = string_text
    original_write(moded_text)


if __name__ == "__main__":
    original_write = sys.stdout.write
    print("Change method")
    sys.stdout.write = my_write
    print("1, 2, 3")
    sys.stdout.write = original_write
    print("Change it back")
    print("1, 2, 3")
