from core.bundler import *

bundler = Bundler()


@command(bundler)
def say_hello(name: str):
    print("Hello, {}!".format(name))


@procedure(bundler)
def multiply(a: int, b: int) -> int:
    return a * b


print("Sending command...")
say_hello("Cian")
print("Command sent, sending procedure...")
c = multiply(2, 2)
print("Procedure result received: {}".format(c))
