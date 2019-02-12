class Person(object):
    isAlive=False
    def __init__(self,_hp):
        self.hp=_hp
p=Person(100)
p1=Person(100)
Person.name="zmc"
print(p.name,p1.name)