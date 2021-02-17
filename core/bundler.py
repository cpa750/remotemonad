from typing import TypeVar, Callable

T = TypeVar('T')


class Bundler:
    def __init__(self):
        self.command_queue = list()

    def queue(self, func: Callable[..., None],
              args: tuple = (), kwargs: dict = None) -> None:
        if kwargs is None:
            kwargs = {}
        self.command_queue.append((func, args, kwargs))

    def send_procedure(self, func: Callable[..., T],
                       args: tuple = (), kwargs: dict = None) -> T:
        if kwargs is None:
            kwargs = {}
        self.__send_queue()
        return func(*args, **kwargs)

    def __send_queue(self):
        for func in self.command_queue:
            # equivalent to command(*args, **kwargs)
            func[0](*func[1], **func[2])
        self.command_queue.clear()


def command(bundler):
    # This wonderful bit of code is necessary for a decorator with params
    def decorator(func):
        def inner(*args, **kwargs):
            bundler.queue(func, args, kwargs)
        return inner
    return decorator


def procedure(bundler):
    # Same here
    def decorator(func):
        def inner(*args, **kwargs):
            return bundler.send_procedure(func, args, kwargs)
        return inner
    return decorator
