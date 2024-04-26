from cProfile import label
from cmath import exp
from dis import show_code
from tkinter import*
from tkinter import ttk
root= Tk()
root.title("Calculator")
#root.geometry("170x150")
exp=""
opr=StringVar()

def show(n):
    global exp
    exp=exp+n 
    opr.set(exp)

def clear():
    global exp
    opr.set("")
    exp=""

def calculate():
    try:
      global exp
      eq=eval(exp)
      opr.set(eq)
    except Exception as e:
        print("error!",e)

def delete():
    global exp
    length=len(exp)
    b=""
    for i in range(0,length-1):
        b=b+exp[i]
    exp=b    
    opr.set(exp) 


# def keyboard(a):
#     Label(root,text=a.char).grid()
    
# for i in range(10):
#     root.bind(str(i),keyboard)
    

    
#f1=Frame(root,width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2).grid() 
btns_frame = Frame(root, bg="grey",bd=0,highlightbackground="black", highlightcolor="black", highlightthickness=2).grid()   

    
      
      
            
e=Entry(root, textvariable=opr, font="arial,40",bd=0,bg="#eee").grid(row=0,column=0, columnspan=6)
btn=Button(root,btns_frame,text="C", width="4",bg="orange", command=lambda:clear(),font="arial,30").grid(row=1,column=1)
btn=Button(root,btns_frame,text="DE", width="4",bg="orange", command=lambda:delete(),font="arial,30").grid(row=1,column=2)
btn=Button(root,btns_frame,text="%", width="4",bg="orange", command=lambda:show("%"),font="arial,30").grid(row=1,column=3)
btn=Button(root,btns_frame,text="÷", width="4",bg="orange", command=lambda:show("/"),font="arial,30").grid(row=1,column=4)

btn=Button(root,btns_frame,text="7", width="4", command=lambda:show("7"),font="arial,30").grid(row=2,column=1)
btn=Button(root,btns_frame,text="8", width="4", command=lambda:show("8"),font="arial,30").grid(row=2,column=2)
btn=Button(root,btns_frame,text="9", width="4", command=lambda:show("9"),font="arial,30").grid(row=2,column=3)
btn=Button(root,btns_frame,text="x", width="4",bg="orange", command=lambda:show("*"),font="arial,30").grid(row=2,column=4)

btn=Button(root,btns_frame,text="4", width="4", command=lambda:show("4"),font="arial,30").grid(row=3,column=1)
btn=Button(root,btns_frame,text="5", width="4", command=lambda:show("5"),font="arial,30").grid(row=3,column=2)
btn=Button(root,btns_frame,text="6", width="4", command=lambda:show("6"),font="arial,30").grid(row=3,column=3)
btn=Button(root,btns_frame,text="-", width="4",bg="orange", command=lambda:show("-"),font="arial,30").grid(row=3,column=4)

btn=Button(root,btns_frame,text="1", width="4", command=lambda:show("1"),font="arial,30").grid(row=4,column=1)
btn=Button(root,btns_frame,text="2", width="4", command=lambda:show("2"),font="arial,30").grid(row=4,column=2)
btn=Button(root,btns_frame,text="3", width="4", command=lambda:show("3"),font="arial,30").grid(row=4,column=3)
btn=Button(root,btns_frame,text="+", width="4",bg="orange", command=lambda:show("+"),font="arial,30").grid(row=4,column=4)

btn=Button(root,btns_frame,text="0", width="12", command=lambda:show("0"),font="arial,30").grid(row=5,column=1,columnspan=2)
btn=Button(root,btns_frame,text=".", width="4", command=lambda:show("."),font="arial,30").grid(row=5,column=3)
btn=Button(root,btns_frame,text="=", width="4",bg="orange", command=lambda:calculate(),font="arial,30").grid(row=5,column=4)

root.bind('1',lambda event:show("1"))
root.bind('2',lambda event:show("2"))
root.bind('3',lambda event:show("3"))
root.bind('4',lambda event:show("4"))
root.bind('5',lambda event:show("5"))
root.bind('6',lambda event:show("6"))
root.bind('7',lambda event:show("7"))
root.bind('8',lambda event:show("8"))
root.bind('9',lambda event:show("9"))
root.bind('0',lambda event:show("0"))
root.bind('<+>',lambda event:show("+"))
root.bind('-',lambda event:show("-"))
root.bind('<*>',lambda event:show("*"))
root.bind('/',lambda event:show("/"))
root.bind('Backspace',lambda event:delete())
root.bind('=',lambda event:calculate())

root.mainloop() 