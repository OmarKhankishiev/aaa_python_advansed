class EmojiMixin:
    def __str__(self):
        poketypes = {
            "grass": "🌿", "fire": "🔥", "water": "🌊", "electric": "⚡"
        }
        return f"{self.name}/{poketypes[self.poketype]}"


class BasePokemon:
    def __init__(self, name, poketype):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f"{self.name}/{self.poketype}"


class Pokemon(EmojiMixin, BasePokemon):
    pass


if __name__ == "__main__":
    bulbasaur = BasePokemon(name="Bulbasaur", poketype="grass")
    pikachu = Pokemon(name="Pikachu", poketype="electric")
    some_water_pokemon = Pokemon(name='WaLtEr', poketype='water')

    print(bulbasaur)
    print(pikachu)
    print(some_water_pokemon)
