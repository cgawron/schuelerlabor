# senden nach_thingspeak
# daten ansehen unter...
# https://thingspeak.com/channels/1533730/widgets/366313
# https://thingspeak.com/channels/1533730

# Constants and variables: 
WRITE_API_KEY = 'OFSMOZN1COHG6PAV'
HTTPS= "https://api.thingspeak.com/update"

# libraries
from time import sleep,gmtime
import urequests

def zeit():
    x= gmtime()  #(2021, 10, 12, 15, 50, 55, 1, 285)
    return "{:02d}.{:02d}.{:02d} {:02d}:{:02d}:{:02d}".format( x[2],x[1],x[0]-2000, x[3],x[4],x[5])


def send(f1=18.1,f2=55.5,f3=999.9,f4=5.3):
  
    felder = {'field1':f1, 'field2':f2, 'field3':f3, 'field4':f4}
    url=f"{HTTPS}?api_key={WRITE_API_KEY}&field1={f1}&field2={f2}&field3={f3}&field4={f4}"
   
    ok=False
    i=0
    while not ok:
        x = urequests.get(url)
        y=x.reason
        print(y)
        if y == b'OK':
            ok=True
        else:
            print('.',end='')
            i=i+1
            if i>10:
                break
    if ok:
        print(zeit())
        print(felder)
    else:
        raise Exception (' send()')

    

if __name__ == '__main__':
    send()
