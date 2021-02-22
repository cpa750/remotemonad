from typing import TypeVar, Callable

T = TypeVar('T')


class Bundler:
    def __init__(self):
        self.command_queue = list()

    def __del__(self):
        self.flush()

    def queue(self, func: Callable[..., None],
              args: tuple = (), kwargs: dict = None) -> None:
        if kwargs is None:
            kwargs = {}
        self.command_queue.append((func, args, kwargs))

    def send_procedure(self, func: Callable[..., T],
                       args: tuple = (), kwargs: dict = None) -> T:
        if kwargs is None:
            kwargs = {}
        self.flush()
        return func(*args, **kwargs)

    def flush(self):
        for func in self.command_queue:
            # equivalent to command(*args, **kwargs)
            func[0](*func[1], **func[2])
        self.command_queue.clear()

    def command(self, func):
        def inner(*args, **kwargs):
            self.queue(func, args, kwargs)
        return inner

    def procedure(self, func):
        def inner(*args, **kwargs):
            return self.send_procedure(func, args, kwargs)
        return inner
