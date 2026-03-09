class Technic:
    """
    Базовый класс, описывающий технику.

    Атрибуты:
        name (str): название техники
        type_technic (str): тип техники
        cost (float): стоимость техники
        manufacturer (str): производитель
    """

    def __init__(self, name: str, type_technic: str, cost: float, manufacturer: str):
        """
        Конструктор класса Technic.

        :param name: название техники
        :param type_technic: тип техники
        :param cost: цена техники
        :param manufacturer: производитель
        """
        self.name = name
        self.type_technic = type_technic
        self.cost = cost
        self.manufacturer = manufacturer

    @property
    def name(self) -> str:
        """Возвращает название техники."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Устанавливает название техники.

        :param value: название техники
        """
        if not isinstance(value, str):
            raise TypeError("Имя должно быть типа str")
        value = value.strip()
        if not value:
            raise ValueError("Имя не может быть пустым значением")
        self._name = value

    @property
    def type_technic(self) -> str:
        """Возвращает тип техники."""
        return self._type_technic

    @type_technic.setter
    def type_technic(self, value: str) -> None:
        """
        Устанавливает тип техники.

        :param value: тип техники
        """
        if not isinstance(value, str):
            raise TypeError("Тип техники должен быть типа str")
        value = value.strip()
        if not value:
            raise ValueError("Тип техники не может быть пустым значением")
        self._type_technic = value

    @property
    def cost(self) -> float:
        """Возвращает стоимость техники."""
        return self._cost

    @cost.setter
    def cost(self, value: float) -> None:
        """
        Устанавливает стоимость техники.

        :param value: стоимость
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        if value < 0:
            raise ValueError("Цена не может быть меньше 0")
        self._cost = float(value)

    @property
    def manufacturer(self) -> str:
        """Возвращает производителя техники."""
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str) -> None:
        """
        Устанавливает производителя техники.

        :param value: производитель
        """
        if not isinstance(value, str):
            raise TypeError("Производитель должен быть типа str")
        value = value.strip()
        if not value:
            raise ValueError("Название производителя не может быть пустым")
        self._manufacturer = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return (
            f"Техника - {self.name}. Тип - {self.type_technic}. "
            f"Цена - {self.cost}. Производитель - {self.manufacturer}."
        )

    def __repr__(self) -> str:
        """
        Возвращает техническое представление объекта.
        """
        return (
            f"{self.__class__.__name__}(name={self.name!r}, type_technic={self.type_technic!r}, "
            f"cost={self.cost!r}, manufacturer={self.manufacturer!r})"
        )


class Telephone(Technic):
    """
    Класс телефона, наследующий класс Technic.

    Дополнительные атрибуты:
        memory (int): объём памяти телефона (ГБ)
        screen_size (float): размер экрана телефона
    """

    def __init__(
        self,
        name: str,
        type_technic: str,
        cost: float,
        manufacturer: str,
        memory: int,
        screen_size: float,
    ):
        """
        Конструктор класса Telephone.

        :param name: название телефона
        :param type_technic: тип техники
        :param cost: цена телефона
        :param manufacturer: производитель
        :param memory: объём памяти
        :param screen_size: размер экрана
        """
        super().__init__(name, type_technic, cost, manufacturer)
        self.memory = memory
        self.screen_size = screen_size

    @property
    def memory(self) -> int:
        """Возвращает объём памяти телефона."""
        return self._memory

    @memory.setter
    def memory(self, value: int) -> None:
        """
        Устанавливает объём памяти телефона.

        :param value: объём памяти в ГБ
        """
        if not isinstance(value, int):
            raise TypeError("Память должна быть типа int")
        if value <= 0:
            raise ValueError("Количество памяти не может быть меньше или равно 0")
        self._memory = value

    @property
    def screen_size(self) -> float:
        """Возвращает размер экрана телефона."""
        return self._screen_size

    @screen_size.setter
    def screen_size(self, value: float) -> None:
        """
        Устанавливает размер экрана телефона.

        :param value: размер экрана
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Размер экрана должен быть типа int или float")
        if value <= 0:
            raise ValueError("Размер экрана не может быть меньше или равно 0")
        self._screen_size = float(value)

    def __str__(self) -> str:
        """
        Возвращает строковое представление телефона.
        """
        base = super().__str__()
        return f"{base} Память - {self.memory} ГБ. Размер экрана - {self.screen_size}."

    def __repr__(self) -> str:
        """
        Возвращает техническое представление телефона.
        """
        return (
            f"{self.__class__.__name__}(name={self.name!r}, type_technic={self.type_technic!r}, "
            f"cost={self.cost!r}, manufacturer={self.manufacturer!r}, "
            f"memory={self.memory!r}, screen_size={self.screen_size!r})"
        )


if __name__ == "__main__":
    technic = Technic("Стиральная машина", "Бытовая техника", 35000, "LG")
    phone = Telephone("Galaxy S23", "Смартфон", 80000, "Samsung", 256, 6.7)

    print(technic)
    print(phone)