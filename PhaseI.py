import csv
import os
import numpy as np

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as tmsg
from tkinter import simpledialog

mKey="123"

preDefinedFilePath="D:\\Git_&_Github\\Git\\Group_Project\\Data.csv"
preDefinedDIRPath="D:\\Git_&_Github\\Git\\Group_Project"

windObj = Tk()
colorPalette=["#ffffff","#429ef5","#000000"]
fontStyles=[]
header=["Registration Number:","First Name:","Middle Name:","Last Name:","Contact Number:","Email:","Gender:"]
err=["0x01:Invalid-Entry","0x02:Invalid-Character","0x03:Compulsory-Entry","0x04:Invalid-Digit"]


class RegWindow:

 def __init__(self):
  self.height=500
  self.width=550
  self.header="TDSSS and Company"

 def windows(self):
  windObj.geometry("500x550")
  windObj.maxsize(self.height ,self.width)
  windObj.minsize(self.height, self.width)
  windObj.title("TDSSS and Company")
  windObj.configure(bg=colorPalette[0])

class Container:
 
 def __init__(self):
  self.menuNm=["Register","View","Menu","Master Terminal","Admin"]
  self.fc=[]
  self.data=[]
  self.eObj=[]
  self.rObj=[]
  self.fh=fileHandle()
  self.er=Errors()
  return
 
 def register(self):
   tmsg.showinfo("register-portal","Register-Portal")

 def view(self):
   tmsg.showinfo("view-portal","View-Portal") 

 def menu(self):
  yourmenu = Menu(windObj)
  m_first = Menu(yourmenu , tearoff=0)
  m_first.add_command(label = self.menuNm[0] , command =lambda:self.register())
  m_first.add_command(label = self.menuNm[1], command = lambda:self.view())
  yourmenu.add_cascade(label=self.menuNm[2], menu=m_first)

  m_second = Menu(yourmenu , tearoff=0)
  m_second.add_command(label=self.menuNm[3] , command=lambda:self.fh.viewData())
  yourmenu.add_cascade(label=self.menuNm[4], menu=m_second)
  windObj.config(menu=yourmenu)  
  
 def frameGen(self,bd,wd,ht):
  self.fc.append(Frame(windObj, borderwidth=bd , relief=SUNKEN , width=wd , height=ht))
  for i in range(3):
    self.fc.append(Frame(windObj, borderwidth=bd , relief=SUNKEN)) 
  
  self.fc[0].pack(side = "top" , expand=False)
  self.fc[0].configure(bg=colorPalette[1])
  self.fc[0].pack_propagate(0)

  self.fc[1].pack(side = "top" , pady=(20 , 0))
  self.fc[1].configure(bg=colorPalette[0])

  self.fc[2].pack(side="top" , pady=(10 , 0))
  self.fc[2].configure(bg=colorPalette[0])

  self.fc[3].pack(side="top" , pady=(10 , 0) , expand=False)
  self.fc[3].configure(bg=colorPalette[0])
  self.fc[3].pack_propagate(0)

 def layout(self):
   lObj=[]
   
   dataEntry=[]
   
   #Layout-Component:Gen
   lObj.append(Label(self.fc[0] , text="WELCOME TO TDSSS & COMPANY" , fg=colorPalette[0] , bg=colorPalette[1] , font="Courier 18 bold"))
   lObj.append(Label(self.fc[0] , text="Please complete your registration" , fg=colorPalette[0] , bg=colorPalette[1] , font="System 15 bold" , pady=0))
   lObj.append(Label(self.fc[1] , text=header[0], font="Bitter 10" , bg=colorPalette[0]))
   lObj.append(Label(self.fc[1] , text=header[1], font="Bitter 10" , bg=colorPalette[0]))
   lObj.append(Label(self.fc[1] , text=header[2], font="Bitter 10" , bg=colorPalette[0]))
   lObj.append(Label(self.fc[1] , text=header[3], font="Bitter 10" , bg=colorPalette[0])) 
   lObj.append(Label(self.fc[1] , text=header[4], font="Bitter 10" , bg=colorPalette[0])) 
   lObj.append(Label(self.fc[1], text=header[5] , font="Bitter 10" , bg=colorPalette[0]))
   lObj.append(Label(self.fc[1] , text=header[6], font="Bitter 10" , bg=colorPalette[0]))
   
   dataEntry.append(StringVar())
   self.eObj.append(Entry(self.fc[1], textvariable=dataEntry[0],font="Bitter 10" , highlightbackground=colorPalette[2], highlightthickness=1))
   dataEntry.append(StringVar())
   self.eObj.append(Entry(self.fc[1] , textvariable=dataEntry[1] , font="Bitter 10" , highlightbackground=colorPalette[2], highlightthickness=1))
   dataEntry.append(StringVar())
   self.eObj.append(Entry(self.fc[1] , textvariable=dataEntry[2] , font="Bitter 10" , highlightbackground=colorPalette[2], highlightthickness=1))
   dataEntry.append(StringVar())
   self.eObj.append(Entry(self.fc[1] , textvariable=dataEntry[3] , font="Bitter 10" , highlightbackground=colorPalette[2], highlightthickness=1))
   dataEntry.append(StringVar())
   self.eObj.append(Entry(self.fc[1], textvariable = dataEntry[4] , font="Bitter 10" , highlightbackground=colorPalette[2], highlightthickness=1))
   
   dataEntry.append(StringVar())
   self.eObj.append(Entry(self.fc[1], textvariable=dataEntry[5], font="Bitter 10" , highlightbackground=colorPalette[2], highlightthickness=1))
   
   dataEntry.append(StringVar())
   dataEntry[6].set("Male")
   self.rObj.append(Radiobutton(self.fc[1], text="Female" , font="Bitter 10" , bg=colorPalette[0] , variable=dataEntry[6] , value="Female"))
   self.rObj.append(Radiobutton(self.fc[1] , text="Male" , font="Bitter 10" , bg=colorPalette[0], variable=dataEntry[6] , value="Male"))
   self.rObj.append(Radiobutton(self.fc[1] , text="Others" , font="Bitter 10" , bg=colorPalette[0] , variable=dataEntry[6] , value="Others"))
   
   dataEntry.append(StringVar())
   terms_and_conditions = Checkbutton(self.fc[2], text="By clicking on this button you agree to our terms and conditions." , variable=dataEntry[7] , bg=colorPalette[0] , font="Bitter 10")
   
   #Layout-Component:Position
   lObj[0].pack(side="top" , pady=(40 , 20))
   lObj[1].pack(side="top")
   lObj[2].grid(row=1 , column=1 , sticky=W , pady=(20,0))
   self.eObj[0].grid(row=1 , column=2 , pady=(20,0) , padx=(5,0))
   lObj[3].grid(row=2 , column=1 , sticky=W , pady=(20,0) , padx=(0 , 5))
   self.eObj[1].grid(row=3 , column=1 , sticky=W , pady=(10 , 0) , padx=(0 , 5))   
   lObj[4].grid(row=2 , column=2 , sticky=W , pady=(20,0) , padx=5)
   self.eObj[2].grid(row=3 , column=2 , sticky=W , pady=(10 , 0) , padx=5)   
   lObj[5].grid(row=2 , column=3 , sticky=W , pady=(20,0) , padx=5)
   self.eObj[3].grid(row=3 , column=3 , sticky=W , pady=(10 , 0) , padx=5)
   lObj[6].grid(row=4 , column=1 , sticky=W , pady=(20,0))
   self.eObj[4].grid(row=4 , column=2 , sticky=W , pady=(20 , 0) , padx=(5 , 0))
   lObj[7].grid(row=5 , column=1 , sticky=W , pady=(20 , 0))
   self.eObj[5].grid(row=5 , column=2 , sticky=W , pady=(20 , 0) , padx=(5 , 0))
   lObj[8].grid(row=6 , column=1 , sticky=W , pady=(20 , 0))
   self.rObj[0].grid(row=7 , column=1 , sticky=W , padx=(0 , 0) , pady=(0 , 0))
   self.rObj[1].grid(row=7 , column=2 , sticky=W , padx=(0 , 0) , pady=(0 , 0))
   self.rObj[2].grid(row=7 , column=3 , sticky=W , padx=(0 , 0) , pady=(0 , 0))
   terms_and_conditions.grid(row=8 , column=1 , pady=(10 , 0))

 def button(self):
  btn=Button(self.fc[3], text="Register" , command=lambda:self.collectInfo(), bg=colorPalette[1] , fg=colorPalette[0] , padx=208 , pady=10 , font="Bitter 14")
  btn.grid(row=9 , column=1)
 
 def collectInfo(self):
  for i in self.eObj:
    self.data.append(i.get())
  if(self.er.reg(self.data[0])!=5):
    tmsg.showinfo("ERROR",err[self.er.reg(self.data[0])])
  elif(self.er.names(self.data[1],self.data[2],self.data[3])!=5):
    tmsg.showinfo("ERROR",err[self.er.names(self.data[1],self.data[2],self.data[3])])
  elif(self.er.phone(self.data[4])!=5):
    tmsg.showinfo("ERROR",err[self.er.phone(self.data[4])])
  elif(self.er.mail(self.data[5])!=5):
    tmsg.showinfo("ERROR",err[self.er.mail(self.data[5])])
  else:
    self.fh.writeData(self.data)
  self.data.clear()
  
 def conEvent(self):
  self.menu()
  self.frameGen(0,500,150) 
  self.layout()
  self.button()  


class fileHandle:
 
  def __init__(self):
   return
  
  def createFile(self):
   f=open("Data.csv","w",newline="")
   csvWriter=csv.writer(f)
   csvWriter.writerow(header)
  
  def writeData(self,data):
   print("Data:",data)
   if(not self.isRepeatEntry(data)):
    f=open("Data.csv","a",newline="")
    csvWriter=csv.writer(f)
    csvWriter.writerow(data)
    f.close()
  
  def viewData(self):
   dialogueBox=Tk()
   dialogueBox.withdraw()
   key=simpledialog.askstring(title="Master Key",prompt="Key?")
   if(key==mKey):
    filePath=fd.askopenfilename(initialdir=preDefinedDIRPath,title="MasterViewer",filetypes=[("Excel Speadsheet","*.csv"),("Text Files","*.txt")])
    tmsg.showinfo(str(filePath),str(filePath))
    os.system(r"Data.csv")
  
  def isRepeatEntry(self,data):
   rows=[]
   rows=np.array(self.readData())
   for i in range(len(rows)):
    if((rows[i][0]==data[0])or(rows[i][5]==data[5])):
     return True
   return False

  def readData(self):
   f=open("Data.csv","r")
   csvReader=csv.reader(f)
   tempVar=next(csvReader)
   rows=[]
   for i in csvReader:
     rows.append(i)
   f.close()
   return rows
  
class Errors:
  
  def reg(self,num):
   k=num.isalnum()
   if k==True:
     if len(num)==5:
         return 5
     else:
         return 0
   else:
     print("Alpha",k)
     return 1
      
  def names(self,f,m,l):
   if len(f)==0 or len(l)==0:
     return 2
   else:
     f1=f.isalpha()
     l1=l.isalpha()
     m1=True
     if len(m)!=0:
       m1=m.isalpha()
       if f1 is True and m1 is True and l1 is True:
         return 5
       else:
         return 1
     else:
       if f1 is True and l1 is True:
         return 5
       else:
         return 1
         
  def phone(self,n):
   if len(n)<10 or len(n)>10:
     return 0
   else:
     n1=n.isdigit()
     if n1==True:
       return 5
     else:
       return 3
            
  def mail(self,e):
   if len(e)==0:
     return 2
   else:
     return 5
      
  def checker(self,num,f,l,n,e):
   if len(num) == 0 or len(f) == 0 or len(l) == 0 or len(e) == 0 or len(n) == 0:
     return False
   else:
     return True
  
def main():
 RegWindow().windows()
 if(not os.path.exists(preDefinedFilePath)):
  fileHandle().createFile()
 Container().conEvent()
 windObj.mainloop()

main()

