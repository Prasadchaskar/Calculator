from tkinter import *
root=Tk()
root.geometry("744x1500")
root.title("Calculator")
root.configure(bg="sky blue")
l=Label(text="Prasad Calculator",font="lucida 15 bold",bg="orange")
l.pack()
scval=StringVar()
scval.set("")

def click(event):
    global scval
    text=event.widget.cget("text")
    # print(text)
    if text=='=':
        if scval.get().isdigit():
            value=int(scval.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"
        scval.set(value)
        screen.update()
    elif text=='C':
        scval.set("")
        screen.update()
    else:
        scval.set(scval.get()+text)
        screen.update()

screen=Entry(root,textvar=scval,font="lucida 40 bold")
screen.pack(fill=X,padx=10,pady=20)
#For First 9,8,7 Buttons
list1=['9','8','7']
# f=Frame(root,bg="grey")
# b=Button(f,text="9",padx=12,pady=12,font="lucida 30 bold")
# b.pack(side=LEFT,padx=12,pady=12)
# b.bind("<Button-1>",click)
# b=Button(f,text="8",padx=12,pady=12,font="lucida 30 bold")
# b.pack(side=LEFT,padx=12,pady=12)
# b.bind("<Button-1>",click)
# b=Button(f,text="7",padx=12,pady=12,font="lucida 30 bold")
# b.pack(side=LEFT,padx=12,pady=12)
# b.bind("<Button-1>",click)
# f.pack()
f=Frame(root,bg="yellow")
for i in list1:
    b=Button(f,text=i,padx=12,pady=12,font="lucida 30 bold")
    b.pack(side=LEFT,padx=12,pady=12)
    b.bind("<Button-1>",click)
f.pack()

#For First 6,5,4 Buttons
list2=['6','5','4']
f=Frame(root,bg="yellow")
for j in list2:
    b=Button(f,text=j,padx=12,pady=12,font="lucida 30 bold")
    b.pack(side=LEFT,padx=12,pady=12)
    b.bind("<Button-1>",click)
f.pack()

#For First 3,2,1 Buttons
list3=['3','2','1']
f=Frame(root,bg="yellow")
for k in list3:
    b=Button(f,text=k,padx=12,pady=12,font="lucida 30  bold")
    b.pack(side=LEFT,padx=12,pady=12)
    b.bind("<Button-1>",click)
f.pack()



#For First 0,-,+
list4=['0','-','+']
f=Frame(root,bg="yellow")
for l in list4:
    b=Button(f,text=l,padx=12,pady=12,font="lucida 30 bold")
    b.pack(side=LEFT,padx=12,pady=12)
    b.bind("<Button-1>",click)
f.pack()

list5=['/','*','C']
f=Frame(root,bg="yellow")
for m in list5:
    b=Button(f,text=m,padx=13,pady=13,font="lucida 30 bold")
    b.pack(side=LEFT,padx=13,pady=13)
    b.bind("<Button-1>",click)
f.pack()

list6=['.','%','=']
f=Frame(root,bg="yellow")
for n in list6:
    b=Button(f,text=n,padx=11,pady=11,font="lucida 30 bold")
    b.pack(side=LEFT,padx=11,pady=11)
    b.bind("<Button-1>",click)
f.pack()
root.mainloop()