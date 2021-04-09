from typing import TypeVar, Callable

from core.multicaller import BatchMethod

T = TypeVar('T')


class StrongBundler:
    def __init__(self, multicaller):
        self.multicaller = multicaller
        self.commands = list()

    def __del__(self):
        if self.multicaller.has_queued_calls():
            self.send()

    def queue(self, func: BatchMethod, *args, **kwargs):
        self.multicaller.queue(func, args, kwargs)
        if func.get_name() not in self.commands:
            return self.send()
        else:
            return None

    def register_command(self, func: BatchMethod):
        self.commands.append(func.get_name())

    def send(self):
        *_, last = self.multicaller()
        return last

