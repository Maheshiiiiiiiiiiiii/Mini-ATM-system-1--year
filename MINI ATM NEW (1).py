from tkinter import *
from tkinter import ttk 
import tkinter.message box

class atm:
    def_init_(self,root):
        self,root = root
        blank_space = ""
        self.root.title (110 * blank_space + "ATM")
        self.root.geometry ("774* 760 +280+0")
        self.root.configure (bg= "gainsboro")
        
        #********************************************Frames****************************************************************************************

        MainFrame = Frames(self.root,bd = 20, width = 748, heigth = 700, relief = RIDGE)MainFrame.grid ()
        TopFrame1 = Frames (MainFrame,bd = 7, width = 734, heigth = 300, relief = RIDGE)
        TopFrame1 = (row = 1, column = 0,padx = 12)

        TopFrame2 = Frames (MainFrame,bd = 7, width = 734, heigth = 300, relief = RIDGE)
        TopFrame2 = (row = 0, column = 0,padx = 8)

        TopFrame2 Left = Frames (TopFrame2,bd = 5, width = 190, heigth = 300, relief = RIDGE)
        TopFrame2 Left = (row = 0, column = 0,padx = 3)

        TopFrame2 Mid = Frames (TopFrame2,bd = 5, width = 200, heigth = 300, relief = RIDGE)
        TopFrame2 Mid = (row = 0, column = 0,padx = 3)

        TopFrame2 Right = Frames (TopFrame2,bd = 5, width = 190, heigth = 300, relief = RIDGE)
        TopFrame2 Right = (row = 0, column = 0,padx = 3)

        #*****************************************Functions***************************************************************************************

        def enter_pin():
            pinNo = self.txtRecipt.get("1.0",end- 10")
            if (pinNo == str("2213")) or (pinNo == str ("4323")) or (pinNo + str ("5982")):
                self.txtRecipt.delete ("1.0",END)
                Self.txtRecipt.insert (END,"\t\t\t ATM "+ "\n\n")
                 Self.txtRecipt.insert (END,'withdraw cash\t\t\t Loan'+ "\n\n")
                  Self.txtRecipt.insert (END,'Cash with Recipt\t\t\t Deposit '+ "\n\n")
                   Self.txtRecipt.insert (END,'Balance\t\t\t Request New Pin '+ "\n\n")
                 Self.txtRecipt.insert (END,'Mini satement\t\t\t PRINT Satement' + "\n\n")

self.btnArrow R1 = Button (TopFrame2Rigth,width = 160, height= 60,state = Normal)
                 command = widthdraw cash, image = self_img_arrow_Right).grid (row = 0, column =0 padx = 2,pady= 2) 
 self.btnArrow R2 = button (TopFrame 2 Right,width = 160, height= 60, state = NORMAL)    
                 command = withdraw cash,image = self.img_arrow_Right).grid(row=1.column=0 padx=2,pady=2)
Self.btnArrowL3=Button(TopFrame2 Left,width=160,height=60,state=NORMAL,command= withdrawcash  image=self,img_arrow_Left).grid(row=2,column=0,padx=2,pady=2)
Self.btnArrowL4=Button(TopFrame2 Left,width=160,height=60,state=NORMAL,command=withdrawcash image=self,img_arrow_Left).grid(row=3,column=0,padx=2,pady=2)

#*************************************************Pin Number Button****************************************************************************************************************
Self.img_arrow_left=photoimage(file="arrowL.png")
Self.btnArrowL1=Button(TopFrame2 Left,width=160,height=60,state=NORMAL,command=withdrawcash, image=self,img_arrow_Left).grid(row=0,column=0,padx=2,pady=2)
Self.btnArrowL2=Button(TopFrame2 Left,width=160,height=60,state=NORMAL ,image=self,img_arrow_Left).grid(row=1,column=0,padx=2,pady=2)
Self.btnArrowL3=Button(TopFrame2 Left,width=160,height=60,state=NORMAL ,image=self,img_arrow_Left).grid(row=2,column=0,padx=2,pady=2)
Self.btnArrowL4=Button(TopFrame2 Left,width=160,height=60,state=NORMAL ,image=self,img_arrow_Left).grid(row=3,column=0,padx=2,pady=2)

def clear():
    def insert0():
value0 = 0
self.txtReceipt.insert(END,value0)

def insert1():
value1 = 1
self.txtReceipt.insert(END,value1)

def insert2():
value2 = 2
self.txtReceipt.insert(END,value2)


def insert3():
value3 = 3
self.txtReceipt.insert(END,value3)

def insert4():
value4 = 4
self.txtReceipt.insert(END,value4)

def insert5():
value5 = 5
self.txtReceipt.insert(END,value5)

def insert6():
value6 = 6
self.txtReceipt.insert(END,value6)

def insert7():
value7 = 7
self.txtReceipt.insert(END,value7)

def insert8():
value8 = 8
self.txtReceipt.insert(END,value8)

def insert9():
value9 = 9
self.txtReceipt.insert(END,value9)

def cancel():
cancel = tkinter.messagebox.yesno ("ATM","confirm if you want to cancel")
if cancel >0:
self.root.destroy()
return

def withdrawcash ():
enter_pin()
self.txtReceipt.delete("1.0",END)
self.txtReceipt.focus_set()

def withdrawcash ():
enter_pin()
self.txtReceipt.delete("1.0",END)
self.txtReceipt.insert(END, 'Loan $')

def loan():
Enter_pin()
self.txtReceipt.delete("1.0",END)
self.txtReceipt.focus_set()

def deposit():
enter_pin()
self.txtReceipt.delete("1.0".END")
self.txtReceipt.focus_set()

def request new_pin():
enter_pin()
self.self.txtReceipt.delete("1.0",END)
Self.txtReceipt.insert(END,'\t\t welcome to ibank\n")
Self.txtReceipt.insert(END,"New pin will be send to your home address\n")
Self.txtReceipt.insert(END,"withdraw cash \t\t\t\t Deposit","\n\n\n\n")
Self.txtReceipt.insert(END,"balance \t\t\t request new pin+"\n\n\n\n")
Self.txtReceipt.insert(END,\t\t Thank you For using ibank\n")

def balance():
Self.txtReceipt.delete("1.01,END)
Self.txtReceipt.insert(END,'\t\t welcome to ibank\n")
Self.txtReceipt.insert(END,"$1296"+"\n")
Self.txtReceipt.insert(END,"withdraw cash \t\t\t\t Deposit","\n\n\n\n")
Self.txtReceipt.insert(END,"balance \t\t\t request new pin+"\n\n\n\n")
Self.txtReceipt.insert(END,\t\t Thank you For using ibank\n")

def statement():
Pin No1=str(self.txtReceipt.get("1.0"end1c")
Pin No2=str(pinNo1)
Pin No3=float(pinNo2)
Pin No4=float(1296-(pinNo3))
Self.txtReceipt.delete("1.01,END)
Self.txtReceipt.insert(END,"\n\t" + str(pinNo4)+ "\t\t")
Self.txtReceipt.insert(END,"withdraw cash \t\t\t\t Deposit","\n\n\n\n")
Self.txtReceipt.insert(END,"balance \t\t\t request new pin+"\n\n\n\n")
Self.txtReceipt.insert(END,\t\t Thank you For using ibank\n")


#***********************************************Widget********************************************************************************************************************
Self.txtReceipt=Text(TopFrame2Mid,height=17,width=42,bd=12,font('arial',9,bold))
Self.txtReceipt.grid(row=0,column=0)
Self.img_arrow_left=photoimage(file="arrowL.png")
Self.btnArrowL1=Button(TopFrame2 Left,width=160,height=60,state=DISABLED,command=withdrawcash, image=self,img_arrow_Left).grid(row=0,column=0,padx=2,pady=2)
Self.btnArrowL2=Button(TopFrame2 Left,width=160,height=60,state=DISABLED,image=self,img_arrow_Left).grid(row=1,column=0,padx=2,pady=2)
Self.btnArrowL3=Button(TopFrame2 Left,width=160,height=60,state=DISABLED,image=self,img_arrow_Left).grid(row=2,column=0,padx=2,pady=2)
Self.btnArrowL4=Button(TopFrame2 Left,width=160,height=60,state=DISABLED,image=self,img_arrow_Left).grid(row=3,column=0,padx=2,pady=2)

else:
self.self.txtReceipt.delete("1.0",END)
self.self.txtReceipt.insert(END,'Invalid pin Number' + "\n\n")

def clear():
self.self.txtReceipt.delete("1.0",END)
==================================================================
Self.img_arrow_Right=photoimage(file="arrowL.png")
Self.btnArrowR1=Button(TopFrame2 Right,width=160,height=60,state=DISABLED,command=Loan,mage=self,img_arrow_Right).grid(row=0,column=0,padx=2,pady=2)
Self.btnArrowR2=Button(TopFrame2 Right,width=160,height=60,state=DISABLED,image=self,img_arrow_Right).grid(row=1,column=0,padx=2,pady=2)
Self.btnArrowR3=Button(TopFrame2 Right,width=160,height=60,state=DISABLED,image=self,img_arrow_Right).grid(row=2,column=0,padx=2,pady=2)
Self.btnArrowR4 =Button(TopFrame2 Right,width=160,height=60,state=DISABLED,image=self,img_arrow_Right).grid(row=3,column=0,padx=2,pady=2)

#===================================Pin Number Button=========================================
Self.img1=photo
Image(file=="one png")
Self.btn1=Button(TopFrame1,width=160,height=60,command=insert1,img=self.img1).grid(row=2,column=0,padx=4,pady=4)
Self.img2=photoImage(file=="two png")
Self.btn2=Button(TopFrame1,width=160,height=60,command=insert2,img=self.img2).grid(row=2,column=1,padx=4,pady=4)
Self.img3=photoImage(file=="three png")
Self.btn3=Button(TopFrame1,width=160,height=60,command=insert3,img=self.img3).grid(row=2,column=2,padx=4,pady=4)
Self.imgCE=photoImage(file=="cancel png")
Self.cancel=Button(TopFrame1,width=160,height=60,command=cancel,img=self.imgCE).grid(row=2,column=3,padx=4,pady=4)

Self.img4=photoImage(file=="four png")
Self.btn4=Button(TopFrame1,width=160,height=60,command=insert4,img=self.img4).grid(row=3,column=0,padx=4,pady=4)
Self.img5=photoImage(file=="five png")
Self.btn5=Button(TopFrame1,width=160,height=60,command=insert5,img=self.img5).grid(row=3,column=1,padx=4,pady=4)
Self.img6=photoImage(file=="six png")
Self.btn6=Button(TopFrame1,width=160,height=60,command=insert6,img=self.img6).grid(row=3,column=2,padx=4,pady=4)
Self.imgCl=photoImage(file=="clear png")
Self.clear=Button(TopFrame1,width=160,height=60,command=clear,img=self.imgCl).grid(row=3,column=3,padx=4,pady=4)

Self.img7=photoImage(file=="seven png")
Self.btn7=Button(TopFrame1,width=160,height=60,command=insert7,img=self.img7).grid(row=4,column=0,padx=4,pady=4)
Self.img8=photoImage(file=="eight png")
Self.btn8=Button(TopFrame1,width=160,height=60,command=insert8,img=self.img8).grid(row=4,column=1,padx=4,pady=4)
Self.img9=photoImage(file=="nine png")
Self.btn9=Button(TopFrame1,width=160,height=60,command=insert9,img=self.img9).grid(row=4,column=1,padx=4,pady=4)

Self.imgEnter=photoImage(file=="Enter png")
Self.Enter=Button(TopFrame1,width=160,height=60,command=Enter,img=self.imgEn).grid(row=4,column=3,padx=4,pady=4)