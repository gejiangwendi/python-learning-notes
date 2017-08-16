#练习 类 对象 继承
class People:
    name = 'xiaoming'
    sex = 'man'
    age = 12

    def showInf(self):
        print(self.name + ' ' + self.sex + ' ' + str(self.age))


a = People()

a.name = 'danghao'
a.sex = 'man'
a.age = 27

a.showInf()

class Disabledpeople(People):
    disabled = 'eye'

    def tell(self):
        print('I have some defect in my ' + self.disabled)

b = Disabledpeople()

b.name
b.sex
b.age

b.showInf()
b.disabled
b.disabled = 'leg'

b.tell()