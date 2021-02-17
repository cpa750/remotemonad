import rpyc
from typing import TypeVar, Callable

T = TypeVar('T')


class Remote:
    def __init__(self, address: str, port: int):
        self.command_queue = []
        self.conn = rpyc.connect(address, port)

    def queue(self, func: Callable[..., T], args: tuple, kwargs: dict):
        self.command_queue.append((func, args, kwargs))

    def send_procedure(self, func: Callable[..., T], args: tuple, kwargs: dict):
        self.send_queue()
        func(*args, **kwargs)

    def send_queue(self):
        for func in self.command_queue:
            # equivalent to command(*args, **kwargs)
            func[0](*func[1], **func[2])

        self.command_queue.clear()


def command(func, remote):
    def inner(*args, **kwargs):
        remote.queue(func, args, kwargs)
    return inner


def procedure(func, remote):
    def inner(*args, **kwargs):
        remote.send_procedure(func, args, kwargs)
    return inner
