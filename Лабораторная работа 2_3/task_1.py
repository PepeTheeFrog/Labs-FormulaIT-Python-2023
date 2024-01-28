class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name: str = name
        self._author: str = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages: int = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise ValueError("Количество страниц должно быть целым числом.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = pages

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration: float = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, (float, int)):
            raise ValueError("Продолжительность должна быть числом.")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(duration)

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"