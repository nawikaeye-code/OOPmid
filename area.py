width = int(input('กรอกความกว้าง :'))
heigh = int(input('กรอกความสูง :'))
def area(width,heigh):
    trian = (1/2) * width * heigh
    square = width * heigh
    return(trian,square)

#ใช้รับค่าตัวด้านบนออกมาให้ปริ้นออกมาได้
area_tri,area_squ = area(width,heigh)
print (area_tri,area_squ)