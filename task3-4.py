from iteration_utilities import deepflatten

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', ['f'], 'h', False],
    [1, 2, None],
]


# Реализация итератора через сторонние библиотеки
class MyIter:
    def __init__(self, in_list):
        self.list_ = list(deepflatten(in_list))
        self.cursor = -1
        self.length = len(self.list_)

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.length:
            raise StopIteration
        return self.list_[self.cursor]


# Реализация стандартного итератора
class MyIter2:
    def __init__(self, in_list):
        def create_list(ll: list):
            if len(ll) == 0:
                return ll
            if isinstance(ll[0], list):
                return create_list(ll[0]) + create_list(ll[1:])
            return ll[:1] + create_list(ll[1:])

        self.list_ = create_list(in_list)
        self.cursor = -1
        self.length = len(self.list_)

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.length:
            raise StopIteration
        return self.list_[self.cursor]


# Реализация генератора с любым уровнем вложенности
def gen_list_levels(in_list):
    for elem in in_list:
        if isinstance(elem, list):
            yield from gen_list_levels(elem)
        else:
            yield elem


if __name__ == '__main__':
    print("1-й вариант итератора")
    print("Каждый элемент списка списков на отдельной строке:")
    print("==================================================")
    for elem in MyIter(nested_list):
        print(elem)
    print()

    print("Все элементы в одной строке:")
    print("==================================================")
    print([elem for elem in MyIter(nested_list)])
    print()


    print("2-й вариант итератора")
    print("Каждый элемент списка списков на отдельной строке:")
    print("==================================================")
    for elem in MyIter2(nested_list):
        print(elem)
    print()

    print("Все элементы в одной строке:")
    print("==================================================")
    print([elem for elem in MyIter2(nested_list)])
    print()


    print("Элементы через генератор:")
    print("=========================")
    for item in gen_list_levels(nested_list):
        print(item)
    print()


