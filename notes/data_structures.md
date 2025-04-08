## Базовые структуры данных

[Посмотреть код](../code/data_structures.py)

#### Массивы (Lists в Python)
Упорядоченная коллекция элементов с доступом по индексу. В Python списки динамические (их размер можно менять)

Хранение последовательностей данных, матрицы, буферы

```python
my_list = [10, 20, 30]
print(my_list[1])  # 20 (доступ за O(1))
```

#### Связные списки (Linked Lists)
Элементы (узлы) хранят значение и ссылку на следующий/предыдущий элементы
Типы: Односвязные (только next), двусвязный (next и prev)


##### Односвязный список
Цепочка объектов, где каждый элемент знает только о следующем. В памяти узлы разбросаны, но связаны через next. Это не питоновский список, а отдельная структура данных
```python
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
```
Применение: Задачи, где часто происходит вставка/удаление (например, реализация очереди) <br/>
**Сложность:** 
<br/>O(n) — для добавления в конец и поиска элемента, потому что нужно пройти весь список
<br/>O(1) — Добавление в начало (prepend)

**Визуализация**
```
head → [10 | next → [20 | next → [30 | next → None]]]
```
Хранение в памяти:
```
head → 0x1000 (data=10, next=0x2000)
               → 0x2000 (data=20, next=0x3000)
                              → 0x3000 (data=30, next=None)
```
