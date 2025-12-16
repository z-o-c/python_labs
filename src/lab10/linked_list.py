from typing import Any

class Node:
    def __init__(self, value: Any, next = None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node

        self.tail = new_node
        self._size += 1     

    def prepend(self, value: Any) -> None:
        """Добавить элемент в начало списка"""
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:  # если список был пустым
            self.tail = new_node
        self._size += 1 

    def insert(self, idx: int, value: Any) -> None:
        """Вставка по индексу"""
        if idx < 0:
            raise IndexError("индекс < 0")

        if idx == 0:
            self.prepend(value)
            return

        if idx > len(self):
            raise IndexError("индекс > len(list)")

        current = self.head
        for _ in range(idx - 1):
            assert current is not None
            current = current.next

        assert current is not None, "Current node is None but index is valid"

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

        # Обновляем tail, если вставка в конец
        if new_node.next is None:
            self.tail = new_node

    def remove(self, value: Any) -> None:
        """Удаление первого вхождения значения"""
        if self.head is None:
            return

        # Специальный случай: удаление головы
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            # Если список стал пустым, обнуляем tail
            if self.head is None:
                self.tail = None
            return

        # Поиск узла для удаления
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        # Если нашли значение
        if current.next is not None:
            current.next = current.next.next
            self._size -= 1
            # Обновляем tail, если удалили последний элемент
            if current.next is None:
                self.tail = current

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        values = list(self)
        return f"SinglyLinkedList({values})"


if __name__ == "__main__":
    lst = SinglyLinkedList()

    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(f"После append: {lst}")

    lst.prepend(0)
    print(f"\nПосле prepend: {lst}")

    lst.insert(2, 1.5)
    print(f"\nПосле insert(2, 1.5): {lst}")

    lst.remove(1.5)
    print(f"\nПосле remove(1.5): {lst}")

    letters = SinglyLinkedList()
    letters.append("A")
    letters.append("B")
    letters.append("C")
    print(f"\nСписок букв: {letters}")