# linked list
class Node:
    def __init__(self, data):
        self.data = data  # Данные узла (например, число или строка)
        self.next = None  # Ссылка на следующий узел в списке


class LinkedList:
    def __init__(self):
        self.head = None  # Указатель на первый элемент в списке

    def append(self, data):
        new_node = Node(data)  # Создаю новый узел
        if not self.head:      # Если список пуст,
            self.head = new_node  # то новый узел становится главным
            return

        current = self.head  # Начинаю с головы
        while current.next:  # Пока есть следующий элемент
            current = current.next  # перемещаюсь к концу списка
        current.next = new_node  # Добавляю новый узел в конец

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


# Пример использования
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.prepend(5)
print("Linked List:")
print(ll.print_list())


# Stack
from collections import deque  # Вместо списка для быстрых операций добавления/удаления (О(1))


class Stack:
    def __init__(self):
        """
        Инициализация массива
        """
        self.items = deque()

    def push(self, item):
        """
        Добавление элемента на вершину
        """
        self.items.append(item)

    def pop(self):
        """
        Удаление элемента с вершины
        """
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """
        Посмотреть какая сейчас вершина
        """
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        """
        Проверка на пустоту стека
        """
        return len(self.items) == 0

    def size(self):
        """
        Узнать размер стека
        """
        return len(self.items)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("\nStack:")

print("stack size:", stack.size())
print("stack pop:", stack.pop())  # 30 (последний добавленный элемент)
print("stack peek:", stack.peek())  # 20 (вершина после удаления 30)
print("stack empty:", stack.is_empty())
