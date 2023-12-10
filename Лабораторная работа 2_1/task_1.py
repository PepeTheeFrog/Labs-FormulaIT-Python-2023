import doctest
from typing import Union


class Backlight:
    def __init__(self, status: bool, color: Union[str, type(None)]):
        """
        Создание и подготовка к работе объекта "Подсветка"

        :param status: Состояние подсвтеки (включена(True) / выключена(False))
        :param color: Цвет подсветки

        Примеры:
        >>> backlight = Backlight(True, 'Зеленый') # инициализация экземпляра класса
        """
        if not isinstance(status, bool):
            raise TypeError('Состояние подствеки должно быть типа bool')
        self.is_turn_on = status

        if not isinstance(color, (str, type(None))):
            raise TypeError('Цвет подстветки должен быть типа str или NoneType')
        self.color = color

    def change_color(self, new_color: Union[str, type(None)]) -> None:
        """
        Изменение цвета подсветки.

        :param new_color: Новый цвет

        Примеры:
        >>> backlight = Backlight(True, 'Зеленый')
        >>> backlight.change_color('Синий')
        """
        if not isinstance(new_color, (str, type(None))):
            raise TypeError('Новый цвет должен быть типа str или NoneType')
        ...

    def is_sleep_mode_on(self) -> bool:
        """
        Функция, которая проверяет, включен ли режим сна у подсветки (Подсветка включена без цвета).

        :return: Включен ли режим сна

        Примеры:
        >>> backlight = Backlight(True, 'Зеленый')
        >>> backlight.is_sleep_mode_on()
        """
        ...


class Laptop:
    def __init__(self, status: bool, battery_percentage: Union[int, float], running_application: Union[str, type(None)]):
        """
        Создание и подготовка к работе объекта "Ноутбук"

        :param status: Состояние ноутбука (включен (True) / выключен (False))
        :param battery_percentage: Процент заряда
        :param running_application: Запущенное приложение

        Примеры:
        >>> Macbook = Laptop(True, 50, 'PyCharm') # инициализация экземпляра класса
        """
        if not isinstance(status, bool):
            raise TypeError('Состояние ноутбука должно быть типа bool')
        self.status = status

        if not isinstance(battery_percentage, (int, float)):
            raise TypeError('Процент заряда должен быть типа int или float')
        if battery_percentage < 0:
            raise ValueError('Процент заряда не может быть отрицательным числом')
        self.battery_percentage = battery_percentage

        if not isinstance(running_application, (str, type(None))):
            raise TypeError('Запущенное приложение должно быть типа str или NoneType')
        self.running_program = running_application

    def is_laptop_discharged(self) -> bool:
        """
        Функция, которая проверяет, разряжен ли ноутбук

        :return: Разряжен ли ноутбук

        Примеры:
        >>> Macbook = Laptop(True, 50, 'PyCharm')
        >>> Macbook.is_laptop_discharged()
        """
        ...

    def run_new_application(self, new_application: str) -> None:
        """
        Запуск нового приложения.

        :param new_application: Название нового приложения

        Примеры:
        >>> Macbook = Laptop(True, 50, 'PyCharm')
        >>> Macbook.run_new_application('Safari')
        """
        if not isinstance(new_application, str):
            raise TypeError('Название нового приложение должно быть типа str')
        ...


class InstagramAccount:
    def __init__(self, username: str, followers: int):
        """
        Создание и подготовка к работе объекта "Аккаунт в Instagram"

        :param username: Имя пользователя
        :param followers: Количество подписчиков

        Примеры:
        >>> instagram_account = InstagramAccount('sir_lyubchenko', 259) # инициализация экземпляра класса
        """
        if not isinstance(username, str):
            raise TypeError('Имя пользователя должно быть типа str')
        self.username = username

        if not isinstance(followers, int):
            raise TypeError('Количество подписчиков должно быть типа int')
        if followers < 0:
            raise ValueError('Количество подписчиков не может быть отрицательным числом')
        self.followers = followers

    def change_username(self, new_username: str) -> None:
        """
        Смена имени пользователя.

        :param new_username: Новое имя пользователя
        :raise ValueError: Если новое имя пользователя совпадает с изначальными,
        то возвращает ошибку

        Примеры:
        >>> instagram_account = InstagramAccount('sir_lyubchenko', 259)
        >>> instagram_account.change_username('SergeyLyubchenko')
        """
        if not isinstance(new_username, str):
            raise TypeError('Новое имя пользователя должно быть типа str')
        ...

    def cheat_followers(self, additional_followers: int) -> None:
        """
        Накрутка (увелечение количества) подписчиков.

        :param additional_followers: Количество подписчиков, необходимое накрутить

        Примеры:
        >>> instagram_account = InstagramAccount('sir_lyubchenko', 259)
        >>> instagram_account.cheat_followers(41)
        """
        if not isinstance(additional_followers, int):
            raise TypeError('Количество подписчиков, необходимое накрутить, должно быть типа int')
        if additional_followers < 0:
            raise ValueError('Количество подписчиков, необходимое накрутить, не может быть отрицательным числом')
        ...

    def decrease_followers(self, unfollowers: int) -> None:
        """
        Уменьшение количества подписчиков.

        :param unfollowers: Количество подписчиков, необходимое скрутить (убрать из числа подписчиков)
        :raise ValueError: Если количество скручиваемых превышает изначальное количество подписчиков,
        то возвращается ошибка.

        :return: Количество реально скрученных подписчиков

        Примеры:
        >>> instagram_account = InstagramAccount('sir_lyubchenko', 259)
        >>> instagram_account.decrease_followers(59)
        """
        if not isinstance(unfollowers, int):
            raise TypeError('Количество подписчиков, необходимое скрутить, должно быть типа int')
        if unfollowers < 0:
            raise ValueError('Количество подписчиков, необходимое скрутить, не может быть отрицательным числом')
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
