from collections import deque
from typing import Any

class Stack:
    """
    Реализация стека LIFO (Last In, First Out) с использованием списка.

    push() - добавление в конец списка O(1)
    pop() - снятие верхнего элемента O(1)
    peek() - Возвращает верхний элемент без удаления O(1)
    len()/is_empty() - O(1)
    """
    def __init__(self):
        # внутреннее хранилище стека
        self._data = []

    def __len__(self) -> int:
        return len(self._data)

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if not self._data:
            raise IndexError("пустой стек")

        return self._data.pop()

    def peek(self) -> Any:
        if not self._data:
            return None

        return self._data[-1]

    def is_empty(self) -> bool:
        return not self._data


class Queue:
    """
    Реализация очереди FIFO (First In, First Out) с использованием deque.

    enqueue() - добавление в конец очереди O(1)
    dequeue() - извлечение из начала очереди O(1)
    peek() - просмотр первого элемента без удаления O(1)
    len()/is_empty() - O(1)
    """
    def __init__(self):
        # deque для операций O(1) на обоих концах
        self._data = deque()
    
    def __len__(self) -> int:
        return len(self._data)

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if not self._data:
            raise IndexError("пустая очередь")

        return self._data.popleft()

    def peek(self) -> Any:
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data


if __name__ == "__main__":
    print("\n--- Stack ---")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Стек после push: {s._data}")
    s.pop()
    print(f"Стек после pop: {s._data}")
    print(f"Верхний элемент peek: {s.peek()}")
    print(f"Пустой?: {s.is_empty()}")

    print("\n--- Queue ---")
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(f"Очередь после enqueue: {list(q._data)}")
    q.dequeue()
    print(f"Очередь после dequeue: {list(q._data)}")
    print(f"Первый элемент peek: {q.peek()}")
    print(f"Пустая?: {q.is_empty()}")