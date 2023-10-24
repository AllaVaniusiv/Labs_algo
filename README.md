# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконала: Ванюсів Алла Сергіївна (Група ІР-23)

### Лабораторна робота №1 (Варіант 2 Рівень 2)

'''

Масив вважається монотонним, якщо всі його елементи розташовані в зростаючому або спадаючому порядку.

Завдання: Напишіть функцію, яка перевіряє, чи є заданий масив монотонним. Функція повинна повертати логічне значення True, якщо масив є монотонним, і False, якщо масив не є монотонним.

Приклад вхідних даних і результатів:

1. Для масиву `[1, 2, 3, 4, 5]` функція повертає True, оскільки всі елементи зростають монотонно.
2. Для масиву `[5, 4, 3, 2, 1]` функція повертає True, оскільки всі елементи спадають монотонно.
3. Для масиву `[1, 2, 2, 3, 2, 4]` функція повертає False, оскільки масив не є строго монотонним.

Зверніть увагу, що масив із однаковими значеннями наступного елемента вважається монотонним.

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` .

'''

***
### Лабораторна робота №2 (Варіант 2 Рівень 2)

'''
Джоні працює менеджером в будівельній компанії. Сьогодні він отримав завдання зафарбувати N рекламних щитів,  довжина яких складає {A0, A1, A2, A3 ... AN-1}. В компанії Джоні доступно К малярів,  а також час, за який будь-який з малярів замальовує 1 метр погонний щита. Оскліьки замовлення надвичайно важливе, Джонні має виконати цю роботу якомога швидше. Слід врахувати, що малювати один щит може лише один маляр - який почав роботу з ним

Правила  

1. 2 малярі не можуть розділити щит, щоб малювати його одночасно, або частково. Тобто, не ситуація коли щит почав пофарбувати одн маляр, а завершив інший - неможлива.
2. Маляр фарбує лише суміжні щити. Що означає, ситуація коли маляр А фарбує щити 1 і 3, але пропускає щит 2 -  неможлива

Input

K - кількість малярів
Т - час, за який маляр замальовує 1 погонний метр щита (в хвилинах)
L - масив (цілочисельний) довжин щитів, які необхідно замалювати (в метрах)

Приклад
10
5
10 15 10 5 10 15 20 20 15 20

Результат
100 хвилин

Очевидно, що максимальна тривалість замальовування щитів в прикладі (коли кількість щитів рівна кількості малярів) відповідає часу малювання найдовшого щита

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити роботу вашої функції на прикладах, наведених вище

'''

***
### Лабораторна робота №3 (Варіант 2 Рівень 2)

'''
Для бінарного дерева знайдіть суму всіх глибин усіх вузлів. Глибина вузла - це кількість ребер, які потрібно пройти від кореня дерева, щоб досягти цього вузла.

Ваше завдання полягає в написанні функції, яка обчислює та повертає суми глибин для всіх вузлів у бінарному дереві

**Приклад:** Розглянемо таке бінарне дерево:

```
    1
   / \
  2   3
 / \
4   5
```

Глибина вузла `1` -`0`, глибина вузла `2` та `3`  становить `1`, а глибина вузлів `4` та `5` - `2`. Сума глибин всіх вузлів дорівнює `0 + 1 + 1 + 2 + 2 = 6`.

Функція отримує на вхід корінь бінарного дерева, який має наступний вигляд:

```
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

```

 Ваша функція має мати такий вигляд:
 
```
def sum_of_depths(root: TreeNode) -> int:
    # ваш код
```

Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу `TreeNode` наступним чином:

```
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
```

'''

