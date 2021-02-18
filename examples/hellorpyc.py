from core.bundler import *
import rpyc

bundler = Bundler()
conn = rpyc.connect("localhost", 18861)


@bundler.command
def say_hello(name: str):
    conn.root.say_hello(name)


@bundler.procedure
def multiply(a: int, b: int) -> int:
    return conn.root.multiply(a, b)


print("Sending command...")
say_hello("Cian")
print("Command sent, sending procedure...")
c = multiply(2, 2)
print("Procedure result received: {}".format(c))
