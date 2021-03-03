from typing import TypeVar, Callable

T = TypeVar('T')


class WeakBundler:
    def send_procedure(self, func: Callable[..., T],
                       args: tuple = (), kwargs: dict = None):
        if kwargs is None:
            kwargs = {}
        return func(*args, **kwargs)

    def procedure(self, func):
        def inner(*args, **kwargs):
            return self.send_procedure(func, args, kwargs)

        return inner
