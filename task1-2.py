nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

# nested_list = [
#     ['d', 'e', 'f', 'h', False],
#     [],
#     [1, 2, None],
# ]

# Реализация итератора
class MyIter:
    def __init__(self, in_list):
        self.list = in_list
        self.cursor = 0
        self.length = len(in_list)
        self.sub_cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.cursor < self.length:
            if self.sub_cursor < len(self.list[self.cursor]):
                result = self.list[self.cursor][self.sub_cursor]
                self.sub_cursor += 1
                return result
            self.cursor += 1
            self.sub_cursor = 0
        raise StopIteration


# Реализация генератора
def my_gen(in_list):
    for elems in in_list:
        for elem in elems:
            yield elem


if __name__ == '__main__':
    print("Каждый элемент списка списков на отдельной строке:")
    print("==================================================")
    for elem in MyIter(nested_list):
        print(elem)
    print()

    print("Все элементы в одной строке:")
    print("==================================================")
    print([elem for elem in MyIter(nested_list)])
    print()

    print("Элементы через генератор:")
    print("=========================")
    for item in my_gen(nested_list):
        print(item)
    print()
    