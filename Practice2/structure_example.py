from AlgorithmsCourse.Practice1.abstract_object import AbstractObject
from AlgorithmsCourse.Practice3.abstractstructure import AbstractStructureExtended
from collections.abc import Iterable

class StructureExample(AbstractStructureExtended):
    """Класс реализации структуры на основе list с базовыми методами."""

    def init(self, *args: AbstractObject | Iterable[AbstractObject]):
        """Инициализация отдельными значениями или структурой (list, tuple, ...)"""
        self._list: list[AbstractObject] = []
        self.iter_index = 0

        if args:
            if isinstance(args[0], AbstractObject):
                for element in args:
                    self._list.append(element)
            elif isinstance(args[0], Iterable):
                self._list.extend(args[0])

    def len(self) -> int:
        return len(self._list)

    def repr(self) -> str:
        return str(self._list)

    def getitem(self, key):
        try:
            return self._list[key]
        except IndexError:
            raise IndexError("getitem: index out of range")

    def setitem(self, key, value):
        try:
            self._list[key] = value
        except IndexError:
            raise IndexError("setitem: index out of range")

    def append(self, value: AbstractObject) -> None:
        self._list.append(value)

    def insert(self, index: int, value: AbstractObject) -> None:
        self._list.insert(index, value)

    def index(self, value: AbstractObject, start: int = 0, stop: int = -1) -> int:
        if stop == -1:
            stop = len(self._list)
        for i in range(start, stop):
            if self._list[i] == value:
                return i
        raise ValueError("index: value not found")

    def remove(self, value: AbstractObject) -> None:
        try:
            self._list.remove(value)
        except ValueError:
            raise ValueError("remove: value not exists")

    # Методы расширенного интерфейса
    def clear(self) -> None:
        self._list.clear()

    def extend(self, values: Iterable[AbstractObject]) -> None:
        self._list.extend(values)

    def pop(self, index: int = -1) -> AbstractObject:
        try:
            return self._list.pop(index)
        except IndexError:
            raise IndexError("pop: index out of range")

    def copy(self) -> list[AbstractObject]:
        return self._list.copy()

    def reverse(self) -> None:
        self._list.reverse()

    def count(self, value: AbstractObject) -> int:
        return self._list.count(value)

    # Итератор
    def iter(self) -> Iterable:
        self.iter_index = 0
        return self

    def next(self) -> AbstractObject:
        if self.iter_index >= len(self._list):
            raise StopIteration("No more elements")
        result = self._list[self.iter_index]
        self.iter_index += 1
        return result

    def delitem(self, key) -> None:
        try:
            del self._list[key]
        except IndexError:
            raise IndexError("delitem: index out of range")


class ArrayParts(AbstractStructureExtended):
    """Массив с резервированными местами и базовой реализацией методов."""

    def init(self, *args: AbstractObject | Iterable[AbstractObject]):
        self.array = [None] * 10
        self.__size = 0
        self.__reserved = 10

        if args:
            if isinstance(args[0], Iterable):
                if len(args[0]) >= self.__reserved:
                    self.__size_extending(len(args[0]))
                for el in args[0]:
                    self.append(el)
            else:
                for el in args:
                    self.append(el)

    @property
    def size(self):
        return self.__size

    @property
    def reserved(self):
        return self.__reserved

    def __size_extending(self, max_size=-1) -> None:
        new_size = self.__reserved * 2
        if max_size > 0:
            new_size = max(new_size, max_size)
        new_array = [None] * new_size
        for i in range(self.__size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.__reserved = new_size

    def len(self) -> int:
        return self.__size

    def repr(self) -> str:
        return str([self.array[i] for i in range(self.__size)])

    def getitem(self, item):
        if isinstance(item, int):
            if item < 0 or item >= self.__size:
                raise IndexError("getitem: index out of range")
            return self.array[item]
        elif isinstance(item, slice):
            return [self.array[i] for i in range(*item.indices(self.__size))]
        else:
            raise TypeError("getitem: invalid type")

    def setitem(self, key, value):
        if 0 <= key < self.__size:
            self.array[key] = value
        else:
            raise IndexError("setitem: index out of range")

    def append(self, value: AbstractObject) -> None:
        if self.size >= self.reserved:
            self.__size_extending()
        self.array[self.__size] = value
        self.__size += 1

    def insert(self, index: int, value: AbstractObject) -> None:
        if not (0 <= index <= self.__size):
            raise IndexError("insert: index out of range")
        if self.size >= self.reserved:
            self.__size_extending()
        for i in range(self.__size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.__size += 1

    def index(self, value: AbstractObject, start=0, stop=-1) -> int:
        if stop == -1 or stop > self.__size:
            stop = self.__size
        for i in range(start, stop):
            if self.array[i] == value:
                return i
        raise ValueError("index: value not found")

    def remove(self, value: AbstractObject) -> None:
        idx = self.index(value)
        for i in range(idx, self.__size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.__size - 1] = None
        self.__size -= 1

    def clear(self) -> None:
        self.array = [None] * self.__reserved
        self.__size = 0

    def extend(self, values: Iterable[AbstractObject]) -> None:
        for val in values:
            self.append(val)

    def pop(self, index: int = -1) -> AbstractObject:
        if index == -1:
            index = self.__size - 1
        value = self.array[index]
        self.remove(value)
        return value

    def copy(self) -> list[AbstractObject]:
        return [self.array[i] for i in range(self.__size)]

    def reverse(self) -> None:
        for i in range(self.__size // 2):
            self.array[i], self.array[self.size - 1 - i] = self.array[self.size - 1 - i], self.array[i]

    def count(self, value: AbstractObject) -> int:
        cnt = 0
        for i in range(self.__size):
            if self.array[i] == value:
                cnt += 1
        return cnt

    if name == "main":
        from AlgorithmsCourse.Practice2.generator import Generator

        g = Generator()
        objs = [g.generate_single() for _ in range(5)]

        # Проверка StructureExample
        se = StructureExample()
        se.init(*objs)
        print("StructureExample начальный:", se.repr())
        se.append(g.generate_single())
        print("После append:", se.repr())
        se.remove(se.getitem(0))
        print("После remove:", se.repr())

        # Проверка ArrayParts
        ap = ArrayParts(*objs)
        print("ArrayParts начальный:", ap)
        ap.append(g.generate_single())
        print("После append:", ap)
        ap.insert(2, g.generate_single())
        print("После insert:", ap)
        ap.remove(ap.getitem(0))
        print("После remove:", ap)