if __name__ == "__main__":
    class Device:
        """Базовый класс, представляющий общее устройство."""

        def __init__(self, name: str, brand: str, price: float):
            """
            Инициализация нового объекта Device.

            :param name: Название устройства.
            :param brand: Бренд устройства.
            :param price: Цена устройства.

            Примеры:
            >>> device = Device("Смартфон", "Apple", 999.99)
            """
            if not isinstance(name, str):
                raise TypeError("Название устройства должно быть типа str")
            self.name = name

            if not isinstance(brand, str):
                raise TypeError("Бренд устройства должен быть типа str")
            self.brand = brand

            if not isinstance(price, (int, float)):
                raise TypeError("Цена устройства должна быть типа int или float")
            if price < 0:
                raise ValueError("Цена устройства не может быть отрицательным числом")
            self.price = price

            self.power_connected = False

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта Device для печати.

            :return: Строковое представление устройства для печати.

            Примеры:
            >>> device = Device("Смартфон", "Apple", 999.99)
            >>> print(device)
            """
            return f"{self.name} ({self.brand}) - ${self.price}"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта Device для отладки.

            :return: Строковое представление устройства.

            Примеры:
            >>> device = Device("Смартфон", "Apple", 999.99)
            >>> repr(device)
            """
            return f"Device(name={self.name}, brand={self.brand}, price={self.price})"

        def turn_on(self) -> None:
            """
            Включает устройство.

            Примеры:
            >>> device = Device("Смартфон", "Apple", 999.99)
            >>> device.turn_on()
            """
            ...

        def power_off(self) -> None:
            """
            Выключает устройство.

            Примеры:
            >>> device = Device("Смартфон", "Apple", 999.99)
            >>> device.power_off()
            """
            ...

        def check_battery_status(self) -> str:
            """
            Проверяет статус батареи устройства.

            :return: Статус батареи устройства.

            Примеры:
            >>> device = Device("Смартфон", "Apple", 999.99)
            >>> device.check_battery_status()
            """
            ...

        def check_power_connection(self) -> bool:
            """
            Проверяет, подключено ли устройство к сети питания.

            :return: True, если устройство подключено к сети питания, False в противном случае.

            Примеры:
            >>> device = Device("Смартфон", "Apple", 999.99)
            >>> device.check_power_connection()
            """
            ...


    class Smartphone(Device):
        """Класс, представляющий смартфон, наследующий от Device."""

        def __init__(self, name: str, brand: str, price: float, os: str, screen_size: float):
            """
            Инициализация нового объекта Smartphone.

            :param name: Название смартфона.
            :param brand: Бренд смартфона.
            :param price: Цена смартфона.
            :param os: Операционная система смартфона.
            :param screen_size: Размер экрана смартфона.

            Примеры:
            >>> smartphone = Smartphone("iPhone", "Apple", 999.99, "iOS", 6.1)
            """
            super().__init__(name, brand, price)

            if not isinstance(os, str):
                raise TypeError("Операционная система смартфона должна быть типа str")
            self.os = os

            if not isinstance(screen_size, (int, float)):
                raise TypeError("Размер экрана смартфона должен быть типа int или float")
            if screen_size <= 0:
                raise ValueError("Размер экрана смартфона должен быть положительным числом")
            self.screen_size = screen_size

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта Smartphone для отладки.

            :return: Строковое представление смартфона.

            Примеры:
            >>> smartphone = Smartphone("iPhone", "Apple", 999.99, "iOS", 6.1)
            >>> repr(smartphone)
            """
            return f"Smartphone(name={self.name}, brand={self.brand}, price={self.price}, os={self.os}, screen_size={self.screen_size})"

        def make_call(self, number: str) -> None:
            """
            Осуществляет вызов на указанный номер.

            :param number: Номер телефона для вызова.

            Примеры:
            >>> smartphone = Smartphone("iPhone", "Apple", 999.99, "iOS", 6.1)
            >>> smartphone.make_call("+00000000000")
            """
            if not isinstance(number, str):
                raise TypeError("Номер телефона должен быть типа str")
            ...

        def take_photo(self) -> None:
            """
            Делает фотографию с помощью смартфона.

            Примеры:
            >>> smartphone = Smartphone("iPhone", "Apple", 999.99, "iOS", 6.1)
            >>> smartphone.take_photo()
            """
            ...

        def check_storage_space(self) -> str:
            """
            Проверяет доступное место для хранения на смартфоне.

            :return: Доступное место для хранения.

            Примеры:
            >>> smartphone = Smartphone("iPhone", "Apple", 999.99, "iOS", 6.1)
            >>> smartphone.check_storage_space()
            """
            ...

        def send_sms(self, number: str, message: str) -> None:
            """
            Отправляет SMS-сообщение на указанный номер.

            :param number: Номер телефона, на который отправляется сообщение.
            :param message: Текст сообщения.

            Примеры:
            >>> smartphone = Smartphone("iPhone", "Apple", 999.99, "iOS", 6.1)
            >>> smartphone.send_sms("+00000000000", "Привет! Как дела?")
            """
            if not isinstance(number, str):
                raise TypeError("Номер телефона должен быть типа str")

            if not isinstance(message, str):
                raise TypeError("Текст сообщения должен быть типа str")
            ...
    pass
