class Stack:

    def __init__(self, stack: list):
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

    def bracket_balance_check(self):
        # Скобки сбалансированы если количество открывающих равно количеству закрывающих скобок, что проверяется
        # счетчиками в словаре brackets. Также необходимо, чтобы перед каждой закрывающей скобкой была открывающая,
        # а не наоборот. Это происходит только, если ни один из счетчиков не становится ниже 0.
        brackets = {'(': 0, '{': 0, '[': 0}
        for element in self.stack:
            if element not in ['(', ')', '[', ']', '{', '}']:
                return 'Для проверки стэк должен состоять только из скобок'
            else:
                if element in brackets.keys():
                    brackets[element] += 1
                elif element == ')':
                    brackets['('] -= 1
                    if brackets['('] < 0:
                        return 'Несбалансированно'
                elif element == ']':
                    brackets['['] -= 1
                    if brackets['['] < 0:
                        return 'Несбалансированно'
                elif element == '}':
                    brackets['{'] -= 1
                    if brackets['{'] < 0:
                        return 'Несбалансированно'
        for value in brackets.values():
            if value != 0:
                return 'Несбалансированно'
        return 'Сбалансировано'


if __name__ == '__main__':
    stringed = input('Введите стэк: ')  # Преобразование строки в список для создания стэка
    listed = [char for char in stringed]
    test_stack = Stack(listed)
    print(test_stack.bracket_balance_check())
