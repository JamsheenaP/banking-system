from tkinter import*
import random
import time

root = Tk()
root.geometry("900x550")
root.title("BANK MANAGEMENT SYSTEM")
root.configure(bg = "white")

Tops = Frame(root,bg="white",width = 800,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 300,height=700,bg = "white",relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width = 400,height=700,bg = "white",relief=SUNKEN)
f2.pack(side=RIGHT)


localtime=time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="BANK MANAGEMENT SYSTEM",fg="Indian Red",bg = "white",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="Indian Red",bg = "white",anchor=W)
lblinfo.grid(row=1,column=0)

number = StringVar()
amount = StringVar()
withd = StringVar()
acca = " "

def bank():
    global acca
    accno=["0009879","0001234","0009829","1002789","2030456"]
    account = number.get()
    if account in accno:
        label.config(text="Registered member")
        bank = {"0009879":10000, "000123":20000, "0009829":30000}
        balance = bank[account]
        acca = balance

    else:
        label.config(text="Non-Registered member")

def deposit():
    global acca
    amo = float(amount.get())
    bal = acca+amo
    label3.config(text=("Net Balance:",str(bal)))

def withdrawn():
    global acca
    wd = float(withd.get())
    if acca >= wd:
        ace = acca-wd
        label4.config(text=("Net Balance :",str(ace)))
    else:
        label4.config(text="Insufficient Balance")
        
def reset():
    number.set("")
    amount.set("")
    withd.set("")
    label.config(text="")
    label4.config(text="")
    label3.config(text="")
    label5.config(text="")
    
def bal():
    global acca
    label5.config(text=("Net Balance :",str(acca)))
    
    
    

lbl = Label(f1, font=( 'aria' ,16, 'bold' ),text="Enter the account number:            ",bg = "white",fg="Indian Red",bd=10,anchor='w')
lbl.grid(row=0,column=3)
txt = Entry(f1,font=('ariel' ,16,'bold'), textvariable=number , bd=6,insertwidth=4,bg="Indian Red" ,justify='right')
txt.grid(row=0,column=4)
label = Label(f1, fg="black",bg = "white",font=( 'aria' ,16, 'bold' ) )
label.grid(row=1, column=4)
btnsubmit =Button(f2,padx=16,pady=4, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=8, text="SUBMIT", bg="Indian Red",command=bank)
btnsubmit.grid(row=0, column=4)

lblTotal = Label(f1,text="                                      ",fg="black",bg = "white")
lblTotal.grid(row=3,columnspan=10)

lbl = Label(f1, font=( 'aria' ,16, 'bold' ),text="Enter the amount to be deposited:",fg="Indian Red",bg = "white",bd=10,anchor='w')
lbl.grid(row=4,column=3)
txt = Entry(f1,font=('ariel' ,16,'bold'), textvariable=amount , bd=6,insertwidth=4,bg="Indian Red" ,justify='right')
txt.grid(row=4,column=4)
label3 = Label(f1, fg="black",bg = "white",font=( 'aria' ,16, 'bold' ) )
label3.grid(row=5, column=4)
btndeposit =Button(f2,padx=16,pady=4, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=8, text="DEPOSIT", bg="Indian Red",command=deposit)
btndeposit.grid(row=4, column=4)

lblTotal = Label(f1,text="                                    ",fg="black",bg = "white")
lblTotal.grid(row=7,columnspan=10)

lbl = Label(f1, font=( 'aria' ,16, 'bold' ),text="Enter the amount to be withdrawn:",fg="Indian Red",bg = "white",bd=10,anchor='w')
lbl.grid(row=8,column=3)
txt = Entry(f1,font=('ariel' ,16,'bold'), textvariable=withd , bd=6,insertwidth=4,bg="Indian Red" ,justify='right')
txt.grid(row=8,column=4)
label4 = Label(f1, fg="black",bg = "white",font=( 'aria' ,16, 'bold' ) )
label4.grid(row=9, column=4)
label5 = Label(f1, fg="black",bg = "white",font=( 'aria' ,16, 'bold' ) )
label5.grid(row=10, column=4)

btnwithdraw =Button(f2,padx=16,pady=4, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=8, text="WITHDRAWAL", bg="Indian Red",command=withdrawn)
btnwithdraw.grid(row=8, column=4)
btnbal =Button(f2,padx=16,pady=4, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=8, text="BALANCE", bg="Indian Red",command=bal)
btnbal.grid(row=10, column=4)
btnreset =Button(f2,padx=16,pady=4, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=8, text="RESET", bg="Indian Red",command=reset)
btnreset.grid(row=11, column=4)
btnexit =Button(f2,padx=16,pady=4, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=8, text="EXIT", bg="Indian Red",command=root.destroy)
btnexit.grid(row=12, column=4)



root.mainloop()
