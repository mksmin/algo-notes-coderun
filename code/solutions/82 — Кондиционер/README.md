## 82. Кондиционер

**Уровень:** Лёгкая  
**Статус:** Решена
**Задача:**
В офисе, где работает программист Пётр, установили кондиционер нового типа. Этот кондиционер отличается особой простотой
в управлении. У кондиционера есть всего лишь два управляемых параметра: желаемая температура и режим работы.

Кондиционер может работать в четырёх режимах:
`«freeze»` — охлаждение. В этом режиме кондиционер может только уменьшать температуру. Если температура в комнате и так
не
больше желаемой, то он выключается.
`«heat»` — нагрев. В этом режиме кондиционер может только увеличивать температуру. Если температура в комнате и так не
меньше желаемой, то он выключается.
`«auto»` — автоматический режим. В этом режиме кондиционер может как увеличивать, так и уменьшать температуру в комнате
до
желаемой.
`«fan»` — вентиляция. В этом режиме кондиционер осуществляет только вентиляцию воздуха и не изменяет температуру в
комнате.

Кондиционер достаточно мощный, поэтому при настройке на правильный режим работы он за час доводит температуру в комнате
до желаемой.

Требуется написать программу, которая по заданной температуре в комнате t_room, установленным на кондиционере желаемой
t_cond температуре и режиму работы определяет температуру, которая установится в комнате через час.

### Формат ввода

Первая строка входного файла содержит два целых числа troom, и tcond, разделенных ровно одним пробелом
(`—50 <= t_room <= 50, —50 <= t_cond <= 50`).

Вторая строка содержит одно слово, записанное строчными буквами латинского алфавита — режим работы кондиционера.

### Формат вывода

Выходной файл должен содержать одно целое число — температуру, которая установится в комнате через час.

### Примечание

В первом примере кондиционер находится в режиме нагрева. Через час он нагреет комнату до желаемой температуры в 20
градусов.

Во втором примере кондиционер находится в режиме охлаждения. Поскольку температура в комнате ниже, чем желаемая,
кондиционер самостоятельно выключается и температура в комнате не поменяется.

### Ограничения

- **Ограничение времени:** 1 с
- **Ограничение памяти:** 64 МБ

#### Пример 1

```
Ввод
10 20
heat

Вывод
20
```  

#### Пример 2

```
Ввод
10 20
freeze

Вывод
10
```  