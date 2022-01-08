class StackClass:
    # инициализация объекта
    def __init__(self):
        self.elems = [[],[],[],[],[]]

    # для добавления элементов в одну стопку
    def push_in(self, el):
        for j in range(len(self.elems)):
            if len(self.elems[j]) < 5:
                self.elems[j].append(el)
                break

    # для добавления стопок ([])
    def push_in_1(self, el):
        self.elems.append(el)

    # удаление элементов
    def pop_out(self):
        return self.elems.pop()

    # получение значения
    def get_val(self):
        return self.elems[len(self.elems) - 1]

    # получение размера
    def stack_size(self):
        return len(self.elems)

if __name__ == '__main__':
    stack_1 = StackClass()

    for i in range(25):
        stack_1.push_in(i + 1)

    stack_1.push_in_1([])
    stack_1.push_in_1([])

    print(stack_1.elems)