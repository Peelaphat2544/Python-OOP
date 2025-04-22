# ฟังก์ชันที่ทำงานกับ Class และ Object

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
obj2 = Employee("แก้ว",2000)

print(isinstance(obj1,Employee)) #ตรวจเช็คว่า obj1 เป็นสมาชิกใน class Employee หรือไม่ ผลออกมาเป็น boolean
print(dir(obj1)) #ตรวจเช็คว่า obj1 มี Attribute และ Methode อะไรบ้าง
print(obj1.__class__) #ตรวจสอบว่า obj1 ถูกสร้างมาจากคลาสอะไร