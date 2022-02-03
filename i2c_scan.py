from machine import I2C,Pin

# construct an I2C bus
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
x= i2c.scan()

s1=[]
if x==[]:
    s="*** keine i2c adr erkannt ***"
else:
    for i in x:
        s1.append(hex(i))
    s="i2c-Adr: {} erkannt".format(s1)
print(s)
        
