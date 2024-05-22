x = 4
arr = [1,2,3,6,10]

for ulang in range(0,5):
    if (arr[ulang] == (x - 1)) or (arr[ulang] == (x + 1)):
        print(arr[ulang])


# Membuat List Stack 
 class ListStack:
    def __init__(self):
        self._L = []

    def push(self,item):
         