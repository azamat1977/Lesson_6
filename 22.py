class Second:
    color = "red"
    form = "circle"
def changecolor(self,newcolor):
    self.color = newcolor
def changeform(self,newform):
    self.form = newform

obj1 = Second()
obj2 = Second()

print (obj1.color, obj1.form) # вывод на экран "red circle"
print (obj2.color, obj2.form) # вывод на экран "red circle"

obj1.changecolor("green")# изменение цвета первого объекта
obj1.changeform("oval")
obj2.changecolor("blue") # изменение цвет второго объекта
obj2.changeform("oval") # изменение формы второго объекта

print (obj1.color, obj1.form) # вывод на экран "green circle"
print (obj2.color, obj2.form) # вывод на экран "blue oval"