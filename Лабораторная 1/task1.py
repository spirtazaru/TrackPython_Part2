import doctest


class Furniture:
    def __init__(self, material: str, weight: float, price: float):
        """
        Создание и подготовка к работе объекта "Мебель"

        :param material: Материал мебели
        :param weight: Вес мебели
        :param price: Цена мебели

        Примеры:
        >>> furniture = Furniture("wood", 15.5, 12000)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        if not material:
            raise ValueError("Материал не может быть пустым")
        self.material = material

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        self.weight = weight

        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        if price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self.price = price

    def move(self, distance: float) -> None:
        """
        Перемещение мебели.

        :param distance: Расстояние перемещения
        :return: None

        Примеры:
        >>> furniture = Furniture("wood", 15.5, 12000)
        >>> furniture.move(3)
        """
        ...

    def calculate_delivery_cost(self) -> float:
        """
        Расчет стоимости доставки мебели.

        :return: Стоимость доставки

        Примеры:
        >>> furniture = Furniture("wood", 15.5, 12000)
        >>> furniture.calculate_delivery_cost()
        """
        ...


class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param height: Высота дерева
        :param age: Возраст дерева

        Примеры:
        >>> tree = Tree("Oak", 3.2, 10)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть типа str")
        if not species:
            raise ValueError("Вид дерева не может быть пустым")
        self.species = species

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным числом")
        self.age = age

    def grow(self, years: int) -> None:
        """
        Рост дерева.

        :param years: Количество лет роста
        :return: None

        Примеры:
        >>> tree = Tree("Oak", 3.2, 10)
        >>> tree.grow(5)
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть типа int")
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным числом")
        ...

    def shed_leaves(self) -> bool:
        """
        Проверка сбрасывает ли дерево листья.

        :return: Сбрасывает ли дерево листья

        Примеры:
        >>> tree = Tree("Oak", 3.2, 10)
        >>> tree.shed_leaves()
        """
        ...


class VKontakte:
    def __init__(self, users_count: int, is_available: bool, year_created: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть ВКонтакте"

        :param users_count: Количество пользователей
        :param is_available: Доступность социальной сети
        :param year_created: Год создания

        Примеры:
        >>> vk = VKontakte(1000000, True, 2006)
        """
        if not isinstance(users_count, int):
            raise TypeError("Количество пользователей должно быть типа int")
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным числом")
        self.users_count = users_count

        if not isinstance(is_available, bool):
            raise TypeError("Доступность должна быть типа bool")
        self.is_available = is_available

        if not isinstance(year_created, int):
            raise TypeError("Год создания должен быть типа int")
        if year_created <= 0:
            raise ValueError("Год создания должен быть положительным числом")
        self.year_created = year_created

    def register_user(self, username: str) -> None:
        """
        Регистрация нового пользователя.

        :param username: Имя пользователя
        :return: None

        Примеры:
        >>> vk = VKontakte(1000000, True, 2006)
        >>> vk.register_user("ivan123")
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        if not username:
            raise ValueError("Имя пользователя не может быть пустым")
        ...

    def publish_post(self, text: str) -> None:
        """
        Публикация записи в социальной сети.

        :param text: Текст публикации
        :return: None

        Примеры:
        >>> vk = VKontakte(1000000, True, 2006)
        >>> vk.publish_post("Привет, мир!")
        """
        if not isinstance(text, str):
            raise TypeError("Текст публикации должен быть типа str")
        if not text:
            raise ValueError("Текст публикации не может быть пустым")
        ...


if __name__ == "__main__":
    doctest.testmod()
