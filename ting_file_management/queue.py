from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        ...

    def __len__(self):
        ...

    def enqueue(self, value):
        ...

    def dequeue(self):
        ...

    def search(self, index):
        ...
