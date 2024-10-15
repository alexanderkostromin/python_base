"""
Задача 1. Стек
Мы уже говорили, что в программировании нередко необходимо создавать свои собственные структуры
данных на основе уже существующих. Одним из таких “базовых” структур является стек.
Стек - это абстрактный тип данных, представляющий собой список элементов, организованных по
принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).

Простой пример: стек из книг на столе. Единственной книгой, чья обложка видна, является самая
верхняя. Чтобы получить доступ к, например, третьей снизу книге, нам нужно убрать все книги,
лежащие сверху, одну за другой.

Напишите класс, который реализует Стек и его возможности (достаточно будет добавления и удаления
элемента).

После этого напишите ещё один класс “Менеджер задач”. В менеджере задач можно выполнить команду
“новая задача”, в которую передаётся сама задача (str) и её приоритет (int). Сам менеджер работает
на основе Стэка (не наследование!).  При выводе менеджера в консоль все задачи должны быть
отсортированы по приоритету: чем меньше число, тем выше задача.

Вот пример основной программы:

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

Результат:<br>
1 отдохнуть<br>
2 поесть; сдать дз<br>
4 сделать уборку; помыть посуду<br>

Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)


class TaskManager:
    def __init__(self):
        self.stack = Stack()

    def new_task(self, task: str, priority: int):
        for existing_priority, existing_task in self.stack.items:
            if existing_task == task:
                print(f"Задача '{task}' уже существует.")
                return

        self.stack.push((priority, task))

    def remove_task(self, task: str):
        found = False
        temp_stack = Stack()

        while not self.stack.is_empty():
            priority, current_task = self.stack.pop()
            if current_task == task:
                found = True
                break
            temp_stack.push((priority, current_task))

        while not temp_stack.is_empty():
            self.stack.push(temp_stack.pop())

        if found:
            print(f"Задача '{task}' была удалена.")
        else:
            print(f"Задача '{task}' не найдена.")

    def __str__(self):
        priority_dict = {}
        for priority, task in self.stack.items:
            if priority not in priority_dict:
                priority_dict[priority] = []
            priority_dict[priority].append(task)

        result = []
        for priority in sorted(priority_dict.keys()):
            tasks = "; ".join(priority_dict[priority])
            result.append(f"{priority} {tasks}")
        return "\n".join(result)


if __name__ == "__main__":
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)

    print("Задачи в менеджере:")
    print(manager)

    manager.remove_task("помыть посуду")

    print("\nПосле удаления задачи:")
    print(manager)

    manager.new_task("сделать уборку", 4)
