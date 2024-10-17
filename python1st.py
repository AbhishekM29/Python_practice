class Abhi:
    def name(self):
        print("Abhishek")

    def surname(self):
        print("Mujumdar")

class shek(Abhi):
    def name1(self):
        print("Abhilasha")

    def surname1(self):
        print("MUJUMDAR")


class AM(shek,Abhi):
    def relation(self):
        print("brother-sister")



ob=AM()
ob.name()
ob.surname()
ob.name1()
ob.surname1()
ob.relation()


