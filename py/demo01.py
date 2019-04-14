class Person(object):
    def __init__(self,name):
        print(1,self)
        self.name = name

    def show(self):
        print(3,self)
        print(f'name={self.name}')

    def __del__(self):
        print(4,self)

class Dog(Person):
    def __init__(self,name):
        super(Dog,self).__init__(name)

p = Person("小明")
print(2,p)
print(id(p),type(p))
print(f'name:{p.name}')
p.show()
#del p
#.show()
d = Dog("gou")

def show():
    print('show...')

if __name__ == '__main__':
    print('aaaaa')