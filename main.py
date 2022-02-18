class Stack:

    def __init__(self, stack=None):
        if stack is None:
            stack = []
        self.stack = stack

    def is_empty(self):  # проверка стека на пустоту. Метод возвращает True или False.
        if self.stack:
            return False
        else:
            return True

    def push(self, element):  # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        self.stack.append(element)

    def pop(self):  # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        self.stack.pop(-1)

    def peek(self):  # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        return self.stack[-1]

    def size(self):  # возвращает количество элементов в стеке.
        return len(self.stack)


def bracket_balance_check():
    string = input('Введите скобки: ')
    open_brackets = ['(', '[', '{']
    closed_brackets = [')', ']', '}']
    check = Stack()
    for bracket in string:
        if bracket in open_brackets:
            check.push(bracket)
        elif bracket in closed_brackets:
            if check.size() == 0 or open_brackets[closed_brackets.index(bracket)] != check.peek():
                return 'Несбалансировано'
            check.pop()
    if check.size() != 0:
        return 'Несбалансировано'
    else:
        return 'Сбалансировано'


if __name__ == '__main__':
    print(bracket_balance_check())
