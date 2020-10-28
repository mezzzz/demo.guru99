from selenium import webdriver

class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Собака создана")
    def SobakaSela(self):
        print('SobakaSela')

sokaba1 = Dog("Vova",22)

sokaba1.SobakaSela()

sokaba2.SobakaSela('Vova',23)