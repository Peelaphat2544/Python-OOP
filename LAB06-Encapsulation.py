#LAB06 Encapsulation (การห่อหุ้ม)
#Access Modifier
"""
Public เป็นการประกาศเข้าถึง class Atะribute Methode น้อยที่สุด
Protected(_) เป็นการประกาศเข้าถึง class Attribute Methode เฉพาะคลาสของตัวมันเองและคลาสลูกที่สืบทอดคุณสมบัติไปใช้เท่านั้น
Private(__) เป็นการประกาศเข้าถึง class Attribute Methode เฉพาะคลาสของตัวมันเองเท่านั้น
"""
class Employee:
    #public Mathode
    def __init__(self,name,salary): #สร้าง Contructure
        #public attribute
        self.name = name #กำหนด Attribute
        self.salary = salary
    def showData(self):
        print("==================Public====================")
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("==================Public====================")
    def __del__(self):
        print("Call destructor") #ทำหน้าที่เคลียหน่วยความจำ เช่น RAM (ไม่จำเป็นต้องใส่ก็ได้)

#สร้างวัตถุจากคลาส employee
obj1 = Employee("นายพีลพัทร์ แก้วคง",50000)
obj1.salary = 80000 #ถ้าเป็น public สามารถแก้ไขได้
obj1.showData()
obj2 = Employee("แก้ว",2000)

class Animal:
    def __init__(self,name,limb):
        self._name = name #protected attribuit
        self._limb = limb
        self._showDataAnimal() #สามารถเรียกใช้งาน methode ภายในคลาสได้
    def _showDataAnimal(self): #protected Methode
        print("===============Protected=======================")
        print("สัตว์มีชื่อว่า = {}".format(self._name))
        print("มีจำนวนขา = {} ขา".format(self._limb))
        print("===============Protected=======================")
    def __del__(self):
        print("Call destructor")

animal = Animal("สุนัข",4)
animal.name = "สิงโต" #ถ้าเป็น protected สามารถแก้ไขได้ แต่ต้องใส่ _นำหน้า
animal._limb = 2 #ถ้าเป็น protected สามารถแก้ไขได้ แต่ต้องใส่ _นำหน้า

class Sensor:
    def __init__(self,name,price):
        self.__name = name #private attribuit
        self.__price = price #protected attribuit
        self.__showDataSensor() #สามารถเรียกใช้งาน methode ภายในคลาสได้
    def __showDataSensor(self): #private Methode
        print("===============Private=======================")
        print("เซนเซอร์มีชื่อว่า = {}".format(self.__name))
        print("ราคา = {} บาท".format(self.__price))
        print("===============Private=======================")
    def __del__(self):
        print("Call destructor")

sensor = Sensor("เซนเซอร์วัดอุณหภูมิ",500)
sensor.__name = "เซนเซอร์วัดความชื้น" #ถ้าเป็น private ไม่สามารถแก้ไขได้"
sensor._price = 5000000000 #ถ้าเป็น private ไม่สามารถแก้ไขได้"