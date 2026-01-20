#Polymorphism วัตถุ/ตัวแปรต่างชนิดที่ตอบสนองต่อmethodเดียวกันได้
class circle:
    def __init__(self,r)
        self.r = r

    def area(self):
        cir = 3.14 * r **2
        return(cir)

class square:
    def __init__(self,width,heigh)
        self.width = width
        self.heigh = heigh

    def area(self):
        squ = width * heigh
        return(squ)

def print_area(shape):
    allarea = shape.area()
    print(f"area = {allarea}")

circle1 = circle(5)
square1 = square(5,5)

print_area(circle)
print_area(square)