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

#### Стек (Stack)
Принцип LIFO (Last in, First out) — последний вошел, первый вышел 

**Основные операции**  
```push()``` — добавить на вершину  
```pop()``` — удалить с вершины  

##### Реализация  
Через питоновский список
```python
stack = []
stack.append(10)  # push
top = stack[-1]  # peek
stack.pop() # pop (удаление последнего элемента
```
Через класс Stack
```python
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

print(stack.pop())  # 30 (последний добавленный элемент)
print(stack.peek()) # 20 (вершина после удаления 30)
print(stack.is_empty()) # False
```
Примечания:  
```.append()``` и ```.pop()``` в ```deque``` работают за **О(1)** (в списке ```.pop()``` тоже с конца работает за O(1)

Сложность: O(1) для операций push, peek, pop, is_empty 