class Color:
    END: str = "\033[0"
    START: str = "\033[1;38;2"
    MOD: str = "m"

    def __init__(
        self, red: int = 100, green: int = 149, blue: int = 237
    ) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    @classmethod
    def _init_limited(cls, red: int, green: int, blue: int):
        return cls(min(red, 255), min(green, 255), min(blue, 255))

    def __eq__(self, other):
        if isinstance(other, Color):
            return (
                self.red == other.red
                and self.green == other.green
                and self.green == other.green
                and self.blue == other.blue
            )
        return NotImplemented

    def __str__(self):
        return (
            f"{self.START};{self.red};{self.green};{self.blue}"
            f"{self.MOD}●{self.END}{self.MOD}"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Color):
            return Color._init_limited(
                self.red + other.red,
                self.green + other.green,
                self.blue + other.blue,
            )
        return NotImplemented

    def __key(self):
        return (self.red, self.green, self.blue)

    def __hash__(self):
        return hash(self.__key())

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            other = max(0, min(other, 1))
            return Color._init_limited(
                int(self.red * other),
                int(self.green * other),
                int(self.blue * other),
            )
        return NotImplemented


if __name__ == "__main__":
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(f"Task_1:\nred: {red}\n")
    print(
        f"Task_2:\n"
        f"red == green: {red == green}\n"
        f"red == Color(255, 0, 0): {red == Color(255, 0, 0)}\n"
    )
    print(f"Task_3:\nred + green: {red + green}\n")
    print(f"Task_4:\norange, green, red: {set(color_list)}\n")
    print(f"Task_5:\nlight red: {0.5 * red}")
