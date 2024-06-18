# OOP/ООП
from time import sleep
from typing import Union


class Cat:
    def __init__(self, age: float, name: str = "Тефтелька"):
        self.__name = name
        self.__age = age

    def set_age(self, new_age):
        if new_age > 20 or new_age < 0 or not isinstance(new_age, int):
            raise Exception()
        self.__age = new_age

    def get_age(self):
        return self.__age

    def sleep(self, time_sleep: int):
        print(f"Котик {self.__name} спит {time_sleep}s")
        sleep(time_sleep)

    def eat(self):
        print("Котик ест!")

    def __heart(self):
        print("сердечко")

    def __str__(self) -> str:
        return f"name: {self.__name}, age: {self.__age}"


# cat1 = Cat(name="Сосиска", age=2)

class Stack:
    def __init__(self):
        self.__stack: list = []

    def __str__(self) -> str:
        result = '-' * 10 + "\n"
        for item in self.__stack[::-1]:
            result += str(item) + "\n"
        result += "-" * 10 + "\n\n"
        return result

    def __len__(self):
        return len(self.__stack)

    def push(self, data: Union[int, str]):
        self.__stack.append(data)

    def pop(self):
        return self.__stack.pop()

    def first_item(self):
        # x = self.pop()
        # self.push(x)
        # return x
        return self.__stack[-1]


class Fraction:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"{self.__x}/{self.__y}"

    def get_x(self):
        return self.__x

    def set_x(self, x: int):
        if not isinstance(x, int):
            raise Exception("Только цифры")
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if not isinstance(y, int):
            raise Exception("Только цифры")
        self.__y = y

    def __add__(self, item: "Fraction"):
        new_f = Fraction(x=self.__x + item.get_x(),
                         y=self.__y + item.get_y())
        return new_f

    def plus(self, item: "Fraction"):
        new_f = Fraction(x=self.__x + item.get_x(),
                         y=self.__y + item.get_y())
        return new_f

f1 = Fraction(x=1,
              y=2)
f2 = Fraction(x=3,
              y=4)
f3 = Fraction(5, 10)

print(f1 + f2 + f3)
