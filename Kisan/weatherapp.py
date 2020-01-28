from tkinter import *
from tkinter import messagebox
import requests
w=Tk()
w.title('Weather application')

def weather():
    s=E1.get()
    url="http://api.openweathermap.org/data/2.5/weather?q={}&APPID=14fc8e75ac7a90b89f2e93b0914723bf&units=matric".format(s)
    response=requests.get(url)
    x=response.json()
    print(x)
  
    if x['cod']!='404':
        y=x["main"]
        current_temperature=y["temp"]
        current_pressure=y["pressure"]
        current_humidity=y["humidity"]
       
        z=x["weather"]
        weather_discription=z[0]["description"]
        E2.insert(0,str(current_temperature)+'Kelvin')
        E3.insert(0,str(current_pressure)+'hPa')
        E4.insert(0,str(current_humidity)+'\n')
        E5.insert(0,str(weather_discription))
    else:
        messagebox.showerror("error","City Not Error \n" "Please enter valid city name")
        E1.delete(0,END)
                
def clear():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E5.delete(0,END)
                  
       
        
        

w.configure(bg='light green')
w.geometry("300x260")
F1=Frame(w,bg='light green')
text=StringVar()
L1=Label(F1,text='Enter Name Of City :',bg='powder blue')
L1.grid(row=0,column=0,columnspan=2)
E1=Entry(F1,textvariable=text)
E1.grid(row=0,column=3,ipadx=100)
F1.pack()

F2=Frame(w,bg='light green')
L2=Label(F2,text='TEMPERATURE :',bg='powder blue')
L2.grid(row=1,column=0,columnspan=2)
E2=Entry(F2)
E2.grid(row=1,column=3,ipadx=100)
F2.pack()

F3=Frame(w,bg='light green')
L3=Label(F3,text='PRESSURE :',bg='powder blue')
L3.grid(row=2,column=0,columnspan=2)
E3=Entry(F3)
E3.grid(row=2,column=3,ipadx=100)
F3.pack()

F4=Frame(w,bg='light green')
L4=Label(F4,text='HUMIDITY :',bg='powder blue')
L4.grid(row=3,column=0,columnspan=2)
E4=Entry(F4)
E4.grid(row=3,column=3,ipadx=100)
F4.pack()

F7=Frame(w,bg='light green')
L7=Label(F7,text='Weather Description :',bg='powder blue')
L7.grid(row=4,column=0,columnspan=2)
E5=Entry(F7)
E5.grid(row=4,column=3,ipadx=100)
F7.pack()

F5=Frame(w,bg='light green')
B1=Button(F5,text=' CLEAR ',command= clear,bg='powder blue')
B1.grid(row=5)
F5.pack()

F6=Frame(w,bg='light green')
B2=Button(F6,text='OK',command= weather,bg='powder blue')
B2.grid(row=6)
F6.pack()

w.mainloop()
