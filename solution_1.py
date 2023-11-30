import keyword
from typing import Any, Dict


class ColorizeMixin:
    """
    Миксин-класс, предоставляющий функционал окрашивания текста
    для его представления.
    """

    repr_color_code: int = 33

    def __init_subclass__(cls, **kwargs) -> None:
        """
        Инициализация подкласса и установка кода цвета по умолчанию,
        если не предоставлен.
        """
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "repr_color_code"):
            cls.repr_color_code = ColorizeMixin.repr_color_code

    def colored_repr(self, text: str) -> str:
        """
        Добавление цвета к заданному тексту на основе кода цвета.
        """
        return f"\033[{self.repr_color_code}m{text}\033[0m"


class Advert(ColorizeMixin):
    """
    Класс, представляющий рекламное объявление
    с цветным текстовым представлением.
    """

    def __init__(self, mapping: Dict[str, Any], is_root: bool = True) -> None:
        """
        Инициализация экземпляра Advert с предоставленным отображением.
        """
        if is_root and "title" not in mapping:
            raise ValueError("Необходим заголовок (title)")
        self._price: int = 0
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += "_"
            if isinstance(value, dict):
                value = Advert(value, is_root=False)
            self.__setattr__(key, value)

    def __getattr__(self, item: str) -> Any:
        """
        Получение значения атрибута или возврат 0, если его нет.
        """
        return self.__dict__.get(item, 0)

    def __setattr__(self, key: str, value: Any) -> None:
        """
        Установка значения атрибута, обработка особых случаев для "price."
        """
        if key == "price":
            if value < 0:
                raise ValueError("Цена должна быть >= 0")
            self._price = value
        else:
            super().__setattr__(key, value)

    @property
    def price(self) -> int:
        """
        Получение свойства цены.
        """
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        """
        Установка свойства цены, обеспечение неположительности.
        """
        if value < 0:
            raise ValueError("Цена должна быть >= 0")
        self._price = value

    def __str__(self) -> str:
        """
        Возврат цветного представления Advert.
        """
        return self.colored_repr(f"{self.title} | {self.price} ₽")


if __name__ == "__main__":
    iphone_advert = Advert(
        {
            "title": "iPhone X",
            "price": 100,
            "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"],
            },
        }
    )
    print(iphone_advert)
    print(iphone_advert.price)
    print(iphone_advert.location.address)

    doge = Advert({"title": "Вельш-корги", "price": 1000, "class": "dogs"})
    print(doge.class_)
    print(doge)
