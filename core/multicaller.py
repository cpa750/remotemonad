from Pyro5.client import BatchProxy, _BatchedRemoteMethod


class BatchMethod(_BatchedRemoteMethod):
    """
    Overriding __call__ to pass so it isn't possible to
    inadvertently add a procedure to the queue without sending it.
    """
    def __call__(self, *args, **kwargs):
        pass

    def get_name(self):
        return self._BatchedRemoteMethod__name


class MultiCaller(BatchProxy):
    """
    Adding a queue method to manually add a function to the batch.
    """
    def queue(self, func: BatchMethod, args, kwargs):
        self._BatchProxy__calls.append((func.get_name(), args, kwargs))

    def has_queued_calls(self):
        return len(self._BatchProxy__calls) > 0

    def __getattr__(self, item):
        return BatchMethod(self._BatchProxy__calls, item)
