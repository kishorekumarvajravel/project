from tkinter import *
from tkinter .font import Font 
v=Tk()
v.title('calculator')
v.configure(bg="#00ffAA")
v.geometry("214x363")
v.iconbitmap(r'D:\ca.ico') #location of a file 
st=StringVar()

# adding styles to the widget

s=Font(family="times",size=16,weight="bold",slant="italic",underline=1)
bu=Font(weight='bold')


# working the calculator

def click(a):
    
    if "=" ==a:
        st.set(eval(e1.get()))
        
    else:
        st.set(e1.get()+str(a))
def clear():
     e1.delete(first=0,last=22)




        
    
#creaing a widgets

Label(v,text="Calculator",bg="#ffffff",font=s).grid(row=0,column=0,columnspan=4)
e1=Entry(v,text=st,bg="black",fg="white",bd=10,width=31)
e1.grid(row=1,column=0,columnspan=4)
b1=Button(v,text=" 1 ",height=1,bd=4,width=3,command=lambda:click(1),bg="#DED1D1",padx=10,pady=10)
b1.grid(row=2,column=0)

b2=Button(v,text=" 2 ",bd=4,height=1,width=3,command=lambda:click(2),bg="#DED1D1",padx=10,pady=10)
b2.grid(row=2,column=1)

b3=Button(v,text=" 3 ",bd=4,height=1,width=3,command=lambda:click(3),bg="#DED1D1",padx=10,pady=10)
b3.grid(row=2,column=2)

b4=Button(v,text=" + ",bd=4,height=1,width=3,command=lambda:click("+"),bg="#ABEEEC",padx=10,pady=10)
b4.grid(row=2,column=3)



b5=Button(v,text=" 4 ",bd=4,height=1,width=3,command=lambda:click(4),bg="#DED1D1",padx=10,pady=10)
b5.grid(row=3,column=0)



b6=Button(v,text=" 5 ",bd=4,height=1,width=3,command=lambda:click(5),bg="#DED1D1",padx=10,pady=10)
b6.grid(row=3,column=1)


b7=Button(v,text=" 6 ",bd=4,height=1,width=3,command=lambda:click(6),bg="#DED1D1",padx=10,pady=10)
b7.grid(row=3,column=2)


b8=Button(v,text=" - ",bd=4,height=1,width=3,command=lambda:click("-"),bg="#ABEEEC",padx=10,pady=10)
b8.grid(row=3,column=3)


b9=Button(v,text=" 7 ",bd=4,height=1,width=3,command=lambda:click(7),bg="#DED1D1",padx=10,pady=10)
b9.grid(row=4,column=0)


b10=Button(v,text=" 8 ",bd=4,height=1,width=3,command=lambda:click(8),bg="#DED1D1",padx=10,pady=10)
b10.grid(row=4,column=1)


b11=Button(v,text=" 9 ",bd=4,height=1,width=3,command=lambda:click(9),bg="#DED1D1",padx=10,pady=10)
b11.grid(row=4,column=2)


b12=Button(v,text=" * ",bd=4,height=1,width=3,command=lambda:click("*"),bg="#ABEEEC",padx=10,pady=10)
b12.grid(row=4,column=3)


b13=Button(v,text=" . ",bd=4,height=1,width=3,command=lambda:click("."),bg="#DED1D1",padx=10,pady=10)
b13.grid(row=5,column=0)

b14=Button(v,text=" 0 ",height=1,width=11,bd=4,command=lambda:click(0),bg="#DED1D1",padx=10,pady=10)
b14.grid(row=5,column=1,columnspan=2)

b15=Button(v,text=" / ",bd=4,height=1,width=3,command=lambda:click("/"),bg="#ABEEEC",padx=10,pady=10)
b15.grid(row=5,column=3)
    
b16=Button(v,text=" = ",bd=4,height=1,width=26,command=lambda:click("="),bg="#0C375D",fg="white",font=("bold",9),padx=10,pady=10)
b16.grid(row=6,column=0,columnspan=4)


 
b17=Button(v,text="clear",bd=4,height=1,width=18,font=bu,command=clear,bg="#ABEEAE",padx=10,pady=10)
b17.grid(row=7,column=0,columnspan=4)


v.mainloop()
