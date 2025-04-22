#LAB03 การกำหนด Attribute

class Employee:
    #สร้าง methode
    def detail (self,name,salary):#ต้องใส่ self ด้วย เพื่อให้รู้ว่าเป็น Methode
        print("เรียกใช้งาน Method ใน Class Employee")
        self.name = name #กำหนด Attribute
        self.salary = salary
    def showData(self):
        print("======================================")
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))

#สร้างวัตถุจากคลาส employee
obj1 = Employee() #นำชื่อคลาสมาระบุ
obj1.detail("Peelaphat",50000)#เรียกใช้งาน Methode ในคลาส Employee
obj1.showData()

obj2 = Employee()
obj2.detail("Kaewkong",60000)#เรียกใช้งาน Methode ในคลาส Employee
obj2.showData()