#LAB08 Class&instance variable

class Animal:
    #class variable คือการสร้างตัวแปรภายในคลาส
    _minlimb = 4 #ประกาศแบบ protected
    __maxlimb = 6 #ไม่สามารถเข้าถึงข้อมูลนี้ได้เนื่องจาก private
    def __init__(self,name,limb):
        #instance variable
        self.__name = name #protected attribuit
        self.__limb = limb
    def _showDataAnimal(self): #protected Methode
        print("===============Protected=======================")
        print("สัตว์มีชื่อว่า = {}".format(self.__name))
        print("มีจำนวนขา = {} ขา".format(self.__limb))
        print("===============Protected=======================")
    def __del__(self):
        print("Call destructor")

animal = Animal("สุนัข",4)
#print("จำนวนขาสูงสุดของสัตว์" ,animal._maxlimb) #Error
print("จำนวนขาต่ำสุดของสัตว์" ,animal._minlimb)