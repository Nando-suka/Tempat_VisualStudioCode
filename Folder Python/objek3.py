# Light Switch Procedural
def turnOn ():
    global switchIsOn
    # turn the light on
    switchIsOn = True

def turnOff ():
    global switchIsOff
    # turn the light off
    switchIsOff = False

# main code
switchIsOn = False # Sebuah global variabel
# Test code
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)

class Televisi:
    def __init__(self, merek, lebar, warna):
        self.merek = merek
        self.lebar = lebar
        self.warna = warna
        
    def display (self):
        print("Informasi: ", self.merek, self.lebar, self.warna)

    def menyala (self):
        x = "Televisi Menyala"
        print(x)
    
    def mematikan (self):
        x = "Televisi Mati"
        print(x)
    
tv1 = Televisi("Toshiba", "30 CM", "Hitam")
tv1.display()
tv1.menyala()
tv1.mematikan()

        


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist2:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " --> ".join(nodes)
    
llist = Linkedlist2()
print(llist)
