# OOP/ООП
from time import sleep
from typing import Union


class Cat:
    def __init__(self, age: float, name: str = "Тефтелька"):
        self.__name = name
        self.__age = age

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

    def __str__(self):
        return str(self.__stack)

    def __len__(self):
        return 5

    def push(self, data: Union[int, str]):
        self.__stack.append(data)

    def pop(self):
        return self.__stack.pop()
