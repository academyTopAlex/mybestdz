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


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)
print(stack.first_item())
stack.push(999)
print(stack.first_item())
