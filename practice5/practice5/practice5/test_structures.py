import pytest
from stack_linked_list import Stack
from queue_array import Queue
from deque_wrapper import Deque


def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.top() == 1


def test_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.top() == 2


def test_deque():
    d = Deque()
    d.push_back(1)
    d.push_front(2)
    assert d.pop_front() == 2
    assert d.pop_back() == 1