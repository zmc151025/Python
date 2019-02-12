"""
类方法： 需要使用@classmethod方法声明 第一个参数为cls 可以访问类相关比如 类说明
实例方法： 方法的第一个参数为self , 用来操作实例属性
静态方法：需要使用@staticmethod声明，和类无关
"""


class Person(object):
    isAlive=False
    def __init__(self,_hp):
        self.hp=_hp
p=Person(100)
p1=Person(100)
Person.name="zmc"
print(p.name,Person.name)