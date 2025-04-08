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

print(ll.print_list())

