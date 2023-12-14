from datetime import datetime
import sys
from typing import Any, Callable, TypeVar


F = TypeVar("F", bound=Callable[..., Any])


def timed_output(function: F) -> F:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        original_write = sys.stdout.write

        def my_write(string_text: str) -> None:
            if string_text != "\n":
                timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]: ")
                modded_text = timestamp + string_text
            else:
                modded_text = string_text
            original_write(modded_text)

        sys.stdout.write = my_write
        try:
            result = function(*args, **kwargs)
        finally:
            sys.stdout.write = original_write
        return result

    return wrapper


@timed_output
def print_greeting(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    print_greeting("Nikita")
