import csv
import os

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as tmsg

preDefinedFilePath="D:\\Git_&_Github\\Git\\Group_Project\\Data.csv"
preDefinedDIRPath="D:\\Git_&_Github\\Git\\Group_Project"

windObj = Tk()
colorPalette=["#ffffff","#429ef5","#000000"]
fontStyles=[]
header=["Registration Number:","First Name:","Middle Name:","Last Name:","Contact Number:","Email:","Gender:"]

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
  return
 
 def register_by_tanir(self):
   print("Hello this is registration portal")

 def view_by_tanir(self):
   print("Hello this is view portal")
 
 def register_button(self):
    print("Your data has been submitted.")

 def menu(self):
  yourmenu = Menu(windObj)
  m_first = Menu(yourmenu , tearoff=0)
  m_first.add_command(label = self.menuNm[0] , command =lambda:self.register_by_tanir())
  m_first.add_command(label = self.menuNm[1], command = lambda:self.view_by_tanir())
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
   f=open("Data.csv","a",newline="")
   csvWriter=csv.writer(f)
   #csvWriter.writerow(header)
   csvWriter.writerow(data)
   f.close()
  
  def viewData(self):
   filePath=fd.askopenfilename(initialdir=preDefinedDIRPath,title="MasterViewer",filetypes=[("Excel Speadsheet","*.csv"),("Text Files","*.txt")])
   file=open(filePath,"r")
   print("GoTo:",filePath)
   file.close()
   tmsg.showinfo(str(filePath),str(filePath))
  
  
def main():
 RegWindow().windows()
 
 if(not os.path.exists(preDefinedFilePath)):
  fileHandle().createFile()
 Container().conEvent()
 windObj.mainloop()

main()

