from abc import abstractmethod, ABC


class PokemonTrainInterface(ABC):
    @abstractmethod
    def increase_exp(self, value):
        pass

    @property
    @abstractmethod
    def exp(self):
        pass


class Pokemon(PokemonTrainInterface):
    def __init__(self, name: str, poketype: str) -> None:
        self.name = name
        self.poketype = poketype
        self._exp = 1

    def __str__(self):
        return f"{self.name}/{self.poketype}"

    def increase_exp(self, value: int):
        self.exp += value

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value


if __name__ == "__main__":
    pika = Pokemon(name="Pikachu", poketype="electric")
    pika.increase_exp(4)
    assert pika.exp == 5, "Too weak"
    print(f"Your current EXP {pika.exp}")
