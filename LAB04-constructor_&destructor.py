#LAB04 constructor และ destructor

class Employee:
    def __init__(self,name,salary): #สร้าง Contructure
        self.name = name #กำหนด Attribute
        self.salary = salary
    def showData(self):
        print("======================================")
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
    def __del__(self):
        print("Call destructor") #ทำหน้าที่เคลียหน่วยความจำ เช่น RAM (ไม่จำเป็นต้องใส่ก็ได้)

#สร้างวัตถุจากคลาส employee
obj1 = Employee("นายพีลพัทร์ แก้วคง",50000)
obj1.showData()
obj1.salary = 70000 #เราสามารถแก้ไขหรืออัพเดตข้อมูลใน methode contructure ได้
obj1.showData()
obj2 = Employee("แก้ว",2000)
obj2.showData()