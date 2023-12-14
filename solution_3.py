import sys
from typing import Any, Callable, TypeVar


F = TypeVar('F', bound=Callable[..., Any])


def redirect_output(filepath: str) -> Callable[[F], F]:
    def decorator(function: F) -> F:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            orig_stdout = sys.stdout
            with open(filepath, 'w') as f:
                sys.stdout = f
                try:
                    result = function(*args, **kwargs)
                finally:
                    sys.stdout = orig_stdout
            return result

        return wrapper

    return decorator


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == "__main__":
    calculate()
