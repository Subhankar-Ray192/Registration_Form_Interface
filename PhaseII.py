import csv
import os
import numpy as np
import uuid

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as tmsg
from tkinter import simpledialog

mKey="123"
policy="\nWe at our company respect the privacy of our registered canditates."+"\nWe assure you that your personal information shall not be ,misused."+"\nWe can guarantee safety of data incase of third party data breach."

preDefinedFilePath="D:\\DataFolder\\Data.csv"
preDefinedDirPath="D:\\DataFolder"

windObj = Tk()
colorPalette=["#ffffff","#fc6405","#000000","#fd9350"]
fontStyles=["Bitter 11","System 15 bold","Courier 18 bold"]


title=["Candidate's details:","Guardian's details:"]
header=["First Name:","Middle Name:","Last Name:","First Name:","Middle Name:","Last Name:" ,"Address:", "Contact Number:","Email:","Gender:","Registration Number"]

can_details=["Candidates Name:" , "Guardian's Name: " ,  "Address: " , "Contact number: " , "Email-id: " , "Gender: " , "Registration Status: "]

err=["0x00:Empty Field Error->","0x01:Invalid:Characters Allowed(Only)-->","0x02:Invalid:Phone-Digits[10] Allowed(Only)","0x03:Invalid:Phone Number-Digits(Only)","0x04:Mail-ID:Compulsory","0x05:Policy-Acceptance:Compulsory"]
gCategory=["Female","Male","Others"]

regStatus=["Valid","Invalid"]


class Window:

 def __init__(self):
  self.width=550
  self.height=670
  self.header="TDSSS and Company"

 def windows(self):
  windObj.geometry("550x670")
  windObj.maxsize(self.width ,self.height)
  windObj.minsize(self.width, self.height)
  windObj.title("TDSSS and Company")
  windObj.configure(bg=colorPalette[0])
  windObj.iconphoto(False , PhotoImage(file="logo2.png"))

 def resizeWin(self,status):
  if(status):
   windObj.maxsize(self.width ,self.height-5)
   windObj.minsize(self.width,self.height-5)
  else:
   windObj.maxsize(self.width ,self.height)
   windObj.minsize(self.width, self.height)
  
  
 def quit(self):
  windObj.destroy()
  
 def keyControls(self):
  windObj.bind('<Control-q>',quit)


class keyManual:
 
 def __init__(self):
  return
 
 def keysAvail(self):
  tmsg.showinfo("Keys","\nQuit: Ctrl+q \n\n Hide-Menu: Ctrl+h \n \n Reveal-Menu: Ctrl+j \n \n View-Portal: Ctrl+z \n \n Register-Portal: Ctrl+x\n \n") 
  
 def info(self):
  tmsg.showinfo("Information","Registration App: V.2.4.10 \n \n Created By: \n Subhankar Ray, \n Tanir Sahoo, \n Dyutiprovo Sarkar, \n Soumyadeep Samanta, \n Sankho Subhro Maitro.")
 
class Container:
 
 def __init__(self):
  self.menuNm=["Register","View","Menu","Master Terminal","Admin","Key Preferences","About","Help"]
  self.fc=[]
  self.data=[]
  self.fh=fileHandle()
  self.er=Errors()
  self.currGender=""
  self.acceptTC=0
  self.reg=Registration()
 
 def hmenuKeyControls(self):
  windObj.bind('<Control-h>',lambda event: self.hiddenMenu())

 def menuKeyControls(self):
  windObj.bind('<Control-j>',lambda event: self.menu())
 
 def regKeyControls(self,eObj):
  windObj.bind('<Return>',lambda event:self.collectInfo(eObj))
 
 def viewKeyControls(self,eObj):
  windObj.bind('<Return>',lambda event:self.fetchInfo(eObj))
 
 def viewWinKey(self):
  windObj.bind('<Control-z>',lambda event: self.view())
 
 def regWinKey(self):
  windObj.bind('<Control-x>',lambda event: self.register())
 
 def fetchInfo(self,eObj):
   lObj=[]
   rows=[]
   row=[]
   rows=self.fh.readData()
   for i in range(7):
    lObj.append(Label(self.fc[3] , text=can_details[i] , bg=colorPalette[0], font=fontStyles[0]))
   
   if(not self.fh.searchData(eObj.get(),10)==-1):
    row=rows[self.fh.searchData(eObj.get(),10)]
    
    #Label:Info
    lObj.append(Label(self.fc[3] , text=str(row[0]+" "+row[1]+" "+row[2]), bg=colorPalette[0], font=fontStyles[0]))
    lObj.append(Label(self.fc[3] , text=str(row[3]+" "+row[4]+" "+row[5]), bg=colorPalette[0], font=fontStyles[0]))
    lObj.append(Label(self.fc[3] , text=row[6], bg=colorPalette[0], font=fontStyles[0]))
    lObj.append(Label(self.fc[3] , text=row[7], bg=colorPalette[0], font=fontStyles[0]))
    lObj.append(Label(self.fc[3] , text=row[8], bg=colorPalette[0], font=fontStyles[0]))
    lObj.append(Label(self.fc[3] , text=row[9], bg=colorPalette[0], font=fontStyles[0]))
    lObj.append(Label(self.fc[3] , text=regStatus[0], bg=colorPalette[0], font=fontStyles[0]))
    
    #Label:Position
    lObj[0].grid(row=3 , column=1 , sticky=W , pady=(10 , 0))
    lObj[7].grid(row=3 , column=2 , sticky=W , pady=(10 , 0))
    lObj[1].grid(row=4 , column=1 , sticky=W , pady=(10 , 0))
    lObj[8].grid(row=4 , column=2 , sticky=W , pady=(10 , 0))
    lObj[2].grid(row=5 , column=1 , sticky=W , pady=(10 , 0))
    lObj[9].grid(row=5 , column=2 , sticky=W , pady=(10 , 0))
    lObj[3].grid(row=6 , column=1 , sticky=W , pady=(10 , 0))
    lObj[10].grid(row=6 , column=2 , sticky=W , pady=(10 , 0))
    lObj[4].grid(row=7 , column=1 , sticky=W , pady=(10 , 0))
    lObj[11].grid(row=7 , column=2 , sticky=W , pady=(10 , 0))
    lObj[5].grid(row=8 , column=1 , sticky=W , pady=(10 , 0))
    lObj[12].grid(row=8 , column=2 , sticky=W , pady=(10 , 0))
    lObj[6].grid(row=9 , column=1 , sticky=W , pady=(10 , 0))
    lObj[13].grid(row=9 , column=2 , sticky=W , pady=(10 , 0))
   else:
    lObj.append(Label(self.fc[3] , text=regStatus[1], bg=colorPalette[0], font=fontStyles[0]))
    
    lObj[6].grid(row=3 , column=1 , sticky=W , pady=(10 , 0))
    lObj[7].grid(row=3 , column=2 , sticky=W , pady=(10 , 0))
 
 def register(self):
   self.frameClear()
   self.regEvent()
   return
 
 def frameClear(self):
  for i in self.fc:
   for widgets in i.winfo_children():
     widgets.destroy()
    
 
 def view(self):
   self.frameClear()
   self.viewEvent()

 def menu(self):
  yourmenu = Menu(windObj)
  m_first = Menu(yourmenu , tearoff=0)
  m_first.add_command(label = self.menuNm[0] , command =lambda:self.register())
  m_first.add_command(label = self.menuNm[1], command = lambda:self.view())
  yourmenu.add_cascade(label=self.menuNm[2], menu=m_first)

  m_second = Menu(yourmenu , tearoff=0)
  m_second.add_command(label=self.menuNm[3] , command=lambda:self.fh.viewData())
  yourmenu.add_cascade(label=self.menuNm[4], menu=m_second)

  m_third = Menu(yourmenu , tearoff=0)
  m_third.add_command(label = self.menuNm[5] , command =lambda:keyManual().keysAvail())
  m_third.add_command(label = self.menuNm[6] , command =lambda:keyManual().info())
  yourmenu.add_cascade(label = self.menuNm[7], menu=m_third)
  windObj.config(menu=yourmenu)
  
  Window().resizeWin(0)
  self.hmenuKeyControls()
 
 def hiddenMenu(self):
  emptyMenu=Menu(windObj)
  windObj.configure(menu=emptyMenu)
  Window().resizeWin(1)
  self.menuKeyControls()
  
 def frameGen(self,bd,wd,ht):
  self.fc.append(Frame(windObj, borderwidth=bd , relief=SUNKEN , width=wd , height=ht))
  for i in range(3):
    self.fc.append(Frame(windObj, borderwidth=bd , relief=SUNKEN)) 
  
  self.fc[0].configure(width=550)
  self.fc[0].pack(side = "top" , expand=False)
  self.fc[0].configure(bg=colorPalette[1])
  self.fc[0].pack_propagate(0)

  self.fc[1].pack(side = "top" , pady=(10 , 0))
  self.fc[1].configure(bg=colorPalette[0])

  self.fc[2].pack(side="top" , pady=(10 , 0))
  self.fc[2].configure(bg=colorPalette[0])

  self.fc[3].pack(side="top" , pady=(10 , 0) , expand=False)
  self.fc[3].configure(bg=colorPalette[0])
  self.fc[3].pack_propagate(0)

 def regLayout(self):
   lObj=[]
   
   gSelect=0
 
   rObj=[]
  
   pSelect=0
 
   eObj=[]
   
   #Layout-Component:Gen
   lObj.append(Label(self.fc[0] , text="WELCOME TO TDSSS & COMPANY" , fg=colorPalette[0] , bg=colorPalette[1] , font=fontStyles[2]))
   lObj.append(Label(self.fc[0] , text="Please complete your registration" , fg=colorPalette[0] , bg=colorPalette[1] , font=fontStyles[1] , pady=0))
   for i in range(2):
    lObj.append(Label(self.fc[1] , text=title[i], font=fontStyles[0] , bg=colorPalette[0])) 
   
   for i in range(10):
    lObj.append(Label(self.fc[1] , text=header[i], font=fontStyles[0] , bg=colorPalette[0]))
   
   for i in range(9):
    eObj.append(Entry(self.fc[1],font=fontStyles[0] , highlightbackground=colorPalette[2], highlightthickness=1))
    
   gSelect=IntVar()
   gSelect.set("None")
   for i in range(3):
    rObj.append(Radiobutton(self.fc[1], text=gCategory[i] , font=fontStyles[0] , bg=colorPalette[0] , variable=gSelect , value=i, command=lambda:self.genderSelect(gSelect.get())))
   
   pSelect=IntVar()
   terms_and_conditions = Checkbutton(self.fc[2], text="By clicking on this button you agree to our terms and conditions."+policy  , bg=colorPalette[0] , font=fontStyles[0],variable=pSelect,onvalue=1,offvalue=0,command=lambda:self.policyS(pSelect))
   
   lObj[4].configure(font=("Bitter" , 9))
   lObj[5].configure(font=("Bitter" , 9))
   lObj[6].configure(font=("Bitter" , 9))
   lObj[7].configure(font=("Bitter" , 9))
   lObj[8].configure(font=("Bitter" , 9))
   lObj[9].configure(font=("Bitter" , 9))

   rObj[0].configure(font=("Bitter" , 9))
   rObj[1].configure(font=("Bitter" , 9))
   rObj[2].configure(font=("Bitter" , 9))
   
   #Layout-Component:Position
   lObj[0].pack(pady=(40 , 20) , side="top")
   lObj[1].pack(side="top")
   lObj[2].grid(row = 0 , column = 0 , sticky=W , pady=(0 , 0))
   lObj[4].grid(row = 1 , column = 0 , sticky=W , pady=(7 , 0) , padx=(0 , 5))
   lObj[5].grid(row = 1 , column = 1 , sticky=W , pady=(7 , 0) , padx=(0 , 5))
   lObj[6].grid(row = 1 , column = 2 , sticky=W , pady=(7 , 0) , padx=(0 , 5))
   lObj[3].grid(row = 3 , column = 0 , sticky=W , pady=(20 , 0) , padx=(0 , 0))
   lObj[7].grid(row = 4 , column = 0 , sticky=W , pady=(7 , 0) , padx=(0 , 5))
   lObj[8].grid(row = 4 , column = 1 , sticky=W , pady=(7 , 0) , padx=(0 , 5))
   lObj[9].grid(row = 4 , column = 2 , sticky=W , pady=(7 , 0) , padx=(0 , 5))
   lObj[10].grid(row = 6 , column = 0 , sticky=W , pady=(20 , 0) , padx=(0 , 0))
   lObj[11].grid(row = 7 , column = 0 , sticky=W , pady=(10 , 0) , padx=(0 , 0))
   lObj[12].grid(row = 8 , column = 0 , sticky=W , pady=(10 , 0) , padx=(0 , 0))
   lObj[13].grid(row = 9 , column = 0 , sticky="W" , pady=(10 , 0) , padx=(0 , 0))  
   
   eObj[0].grid(row = 2 , column=0 , sticky=W , pady=(7 , 0) , padx=(2 , 2))
   eObj[1].grid(row = 2 , column=1 , sticky=W , pady=(7 , 0) , padx=(2 , 2))
   eObj[2].grid(row = 2 , column=2 , sticky=W , pady=(7 , 0) , padx=(2 , 2))
   eObj[3].grid(row = 5 , column=0 , sticky=W , pady=(7 , 0) , padx=(2 , 2))
   eObj[4].grid(row = 5 , column=1 , sticky=W , pady=(7 , 0) , padx=(2 , 2))
   eObj[5].grid(row = 5 , column=2 , sticky=W , pady=(7 , 0) , padx=(2 , 2))
   eObj[6].grid(row = 6 , column=1 , columnspan=3 , sticky="we" , pady=(20 , 0) , padx=(2 , 2))
   eObj[7].grid(row = 7 , column=1 , sticky=W , pady=(10 , 0) , padx=(2 , 2))
   eObj[8].grid(row = 8 , column=1 , columnspan=3 , sticky="we" , pady=(10 , 0) , padx=(2 , 2))
 
   rObj[0].grid(row=10 , column=0  , padx=(0 , 0) , pady=(10 , 0))
   rObj[1].grid(row=10 , column=1  , padx=(0 , 0) , pady=(10 , 0))
   rObj[2].grid(row=10 , column=2  , padx=(0 , 0) , pady=(10 , 0))
 
   terms_and_conditions.grid(row=11 , column=0 , pady=(0 , 0))
   self.regKeyControls(eObj)
   self.regButton(eObj)
 
 def viewLayout(self):
   lObj=[]
   
   lObj.append(Label(self.fc[0] , text="WELCOME TO TDSSS & COMPANY" , fg=colorPalette[0] , bg=colorPalette[1] , font=fontStyles[2]))
   lObj.append(Label(self.fc[0] , text="Check your registration status in this portal" , fg=colorPalette[0], bg=colorPalette[1] , font=fontStyles[1] , pady=0))


   lObj.append(Label(self.fc[1], text=header[10], bg=colorPalette[0], font=fontStyles[0]))
   
   eObj=Entry(self.fc[1], bg=colorPalette[0],font=fontStyles[0], highlightbackground=colorPalette[2],highlightthickness=1)
   
   lObj.append(Label(self.fc[2] , text="------------------------------------------------x------------------------------------------------" , bg="white"))
   row=[]
   
   lObj[0].pack(side="top" , pady=(40 , 20))
   lObj[1].pack(side="top")
   lObj[2].grid(row=1, column=1)
   eObj.grid(row=1, column=2)
   self.viewKeyControls(eObj)
   self.viewButton(eObj)
   lObj[3].grid(row=2 , column=1 , pady=(10 , 0))
   



 def viewButton(self,eObj):
  btn=Button(self.fc[2], text="Fetch Info", bg=colorPalette[1], fg=colorPalette[0], font=fontStyles[0], padx=10, pady=2, command=lambda:self.fetchInfo(eObj), activebackground=colorPalette[3])
  btn.grid(row=1, column=1)
  
 def regButton(self,eObj):
  btn=Button(self.fc[3], text="Register" , command=lambda:self.collectInfo(eObj), bg=colorPalette[1] , fg=colorPalette[0] , padx=232 , pady=10 , font="Bitter 14" , activebackground=colorPalette[3])
  btn.grid(row=9 , column=1)
 
 def genderSelect(self,value):
  self.currGender=gCategory[value]

 def policyS(self,x):
  self.acceptTC=x.get()
  
 def collectInfo(self,eObj):
  for i in eObj:
    self.data.append(i.get())
  self.data.append(self.currGender)
  self.data.append(self.reg.regGen())
  if(self.er.names(self.data[0],self.data[1],self.data[2])!=7):
      tmsg.showinfo("ERROR",err[self.er.names(self.data[0],self.data[1],self.data[2])-1]+can_details[0])
  elif(self.er.names(self.data[3],self.data[4],self.data[5])!=7):
      tmsg.showinfo("ERROR",err[self.er.names(self.data[3],self.data[4],self.data[5])-1]+can_details[1])
  elif(self.er.address(self.data[6])!=7):
      tmsg.showinfo("ERROR",err[self.er.address(self.data[6])]+can_details[2])
  elif(self.er.phone(self.data[7])!=7):
      if(self.er.phone(self.data[7])==0):
          tmsg.showinfo("ERROR",err[2])
      else:
          tmsg.showinfo("ERROR",err[self.er.phone(self.data[7])])
  elif(self.er.mail(self.data[8])!=7):
    tmsg.showinfo("ERROR",err[self.er.mail(self.data[8])]+can_details[4])
  elif((self.currGender!=gCategory[0])and(self.currGender!=gCategory[1])and(self.currGender!=gCategory[2])):
    tmsg.showinfo("ERROR",err[0]+can_details[5])
  elif(not self.acceptTC):
    tmsg.showinfo("ERROR",err[5])
  else:
   tmsg.showinfo("Registration Portal","Your Registration-UID:"+" "+str(self.data[10]))
   self.fh.writeData(self.data)
   self.refresh(eObj)
  self.data.clear()

 def refresh(self,eObj):
  for i in eObj:
   i.delete(0,END) 
  
 def regEvent(self):
  self.menu()
  self.frameGen(0,500,150)
  self.viewWinKey() 
  self.regLayout()

 def viewEvent(self):
   self.menu()
   self.frameGen(0,500,150)
   self.regWinKey()
   self.viewLayout()


class Registration:
 
  def __init__(self):
   return

  def regGen(self):
   return str(uuid.uuid4().node)[:5]

class fileHandle:
 
  def __init__(self):
   return
  
  def createFile(self):
   f=open(preDefinedFilePath,"w",newline="")
   csvWriter=csv.writer(f)
   csvWriter.writerow(header)
  
  def writeData(self,data):
   if(self.searchData(data[8],8)==-1):
    f=open(preDefinedFilePath,"a",newline="")
    csvWriter=csv.writer(f)
    csvWriter.writerow(data)
    f.close()
    self.sortData()

  def sortData(self):
   rows=[]
   rows=self.readData()
   rows.sort(key=lambda x:x[10])
   self.createFile()
   f=open(preDefinedFilePath,"a",newline="")
   csvWriter=csv.writer(f)
   csvWriter.writerows(rows)
   f.close()
   
  def viewData(self):
   dialogueBox=Tk()
   dialogueBox.withdraw()
   key=simpledialog.askstring(title="Master Key",prompt="Key?")
   if(key==mKey):
    os.system(r"D:\\DataFolder\\Data.csv")
   dialogueBox.destroy()

  def readData(self):
   f=open(preDefinedFilePath,"r")
   csvReader=csv.reader(f)
   tempVar=next(csvReader)
   rows=[]
   for i in csvReader:
     rows.append(i)
   f.close()
   return rows
   
  def searchData(self,x,j):
   rows=[]
   rows=np.array(self.readData())
   for i in range(len(rows)):
    if(rows[i][j]==x):
     return i
   return -1
  
class Errors:
  
  def address(self,a):
   if len(a)==0:
      return 0
   else:
      return 7
      
  def names(self,f,m,l):
   if len(f)==0 or len(l)==0:
     return 1
   else:
     f1=f.isalpha()
     l1=l.isalpha()
     m1=True
     if len(m)!=0:
       m1=m.isalpha()
       if f1 is True and m1 is True and l1 is True:
         f2=f.isupper()
         l2=l.isupper()
         m2=m.isupper()
         if f2 is True and m2 is True and l2 is True:
           return 7
     else:
           if f1 is True and l1 is True:
               f2=f.isupper()
               l2=l.isupper()
               if f2 is True and l2 is True:
                   return 7
     return 2
         
  def phone(self,n):
   if len(n)<10 or len(n)>10:
     return 0
   else:
     n1=n.isdigit()
     if n1==True:
       return 7
     else:
       return 3
            
  def mail(self,e):
   if len(e)==0:
     return 0
   else:
     return 7
      
  def checker(self,num,f,l,n,e):
   if len(num) == 0 or len(f) == 0 or len(l) == 0 or len(e) == 0 or len(n) == 0:
     return False
   else:
     return True
  
      
class pathManager:
  
  def __init__(self):
   return
   
  def dirHandler(self):
   if(not os.path.exists(preDefinedDirPath)):
    os.mkdir(preDefinedDirPath)
   self.isFileExist()
    
  def isFileExist(self):
   if(not os.path.exists(preDefinedFilePath)):
    fileHandle().createFile()
  
def main():
 Window().windows()
 Window().keyControls()
 pathManager().dirHandler()
 Container().regEvent()
 windObj.mainloop()
main()
