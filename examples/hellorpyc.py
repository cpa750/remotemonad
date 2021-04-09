import Pyro5.api

from core.multicaller import *
from core.strongbundler import *

nameserver = Pyro5.api.locate_ns()
uri = nameserver.lookup("sayhello")
proxy = Pyro5.api.Proxy(uri)

multicaller = MultiCaller(proxy)
bundler = StrongBundler(multicaller)

bundler.register_command(multicaller.say_hello)

bundler.queue(multicaller.say_hello, "Cian")
print(bundler.queue(multicaller.multiply, 2, 2))
bundler.queue(multicaller.say_hello, "Joe")
