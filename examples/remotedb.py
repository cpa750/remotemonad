from core.strongbundler import *
import rpyc

bundler = StrongBundler()
conn = rpyc.connect("localhost", 18861)


@bundler.command
def insert_name(name, age):
    conn.root.insert_person(name, age)


@bundler.procedure
def query_name(name):
    return conn.root.query_name(name)


@bundler.command
def insert_pet(name, owner):
    conn.root.insert_pet(name, owner)


@bundler.procedure
def query_pet_name(name):
    return conn.root.query_pet_name(name)


@bundler.procedure
def query_pet_owner(owner):
    return conn.root.query_pet_owner(owner)


insert_name("Joe", 21)
res = query_name("Joe")
print(res)
insert_pet("Lucy", res[0][0])
insert_pet("Fido", res[0][0])
print(query_pet_name("Lucy"))
print(query_pet_owner(1))
