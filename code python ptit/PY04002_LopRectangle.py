class Rectangle:
    def __init__(self, width, height, c):
        self.width = width
        self.height = height
        self.c = c

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height
    
    def color(self):
        return str(self.c).title()

arr = input().split() 
if int(arr[0]) > 0 and int(arr[1]) > 0: 
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2]) 
    print("{} {} {}".format(r.perimeter(), r.area(), r.color())) 
else: print("INVALID")