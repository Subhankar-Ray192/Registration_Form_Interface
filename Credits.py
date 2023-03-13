from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk

colorPalette = ["#ffffff", "#fc6405", "#000000", "#fd9350","#808080"]

memberList=["Tanir Sahoo: Frontend Developer","Dyutiprovo Sarkar: Backend Developer","Souymadeep Samanta: Frontend Developer","Subhankar Ray : Project Manager & Backend Developer"]

abtWindObj=Toplevel()
abtWindObj.title("Credits")
        
        
class AboutWindows:
        
    def __init__(self):
      self.height=500
      self.width=600
          
    def windSize(self):
      abtWindObj.geometry("500x500")
      abtWindObj.minsize(self.height,self.width)
      abtWindObj.maxsize(self.height,self.width)
      abtWindObj["bg"]=colorPalette[0]
          
class AboutContainer:
          
    def __init__(self):
      self.fc=[]
      self.imagePointer=3
      return
          
    def frameGen(self):
      for i in range(2): 
        self.fc.append(Frame(abtWindObj,relief=SUNKEN,height=50,width=700,bg=colorPalette[0]))
           
           
    def imageLayout(self,imgPt):
           
      global profilePic
      profilePic=Image.open("Credits_Picture1.png")
           
      global defaultPic
      defaultPic=Image.open("Default_Pictures.png")
           
      global resizedProfilePic
      resizedProfilePic=profilePic.resize((500,500))
              
      global resizedDefaultPic
      resizedDefaultPic=defaultPic.resize((500,500))
           
      global img 
      img=[]
      for i in range(3):
        img.append(ImageTk.PhotoImage(resizedDefaultPic))
      img.append(ImageTk.PhotoImage(resizedProfilePic))
           
      self.fc[0].grid(row=0,column=0,columnspan=3)
           
      global imageLabel
      try:
        imageLabel=Label(abtWindObj,image=img[imgPt])
        imageLabel.grid(row=1,column=0,columnspan=3)
      except:
         imageLabel=Label(abtWindObj,text="x")
         imageLabel.grid(row=1,column=0,columnspan=3)
           
      self.fc[1].grid(row=2,column=0,columnspan=3)
           
    def layout(self):
       label=Label(self.fc[0],text="Registration App: V.2.6.14", background=colorPalette[0], font="System 15")
       label.pack()
          
       previous=Button(self.fc[1],text="<<",bg=colorPalette[0],command=lambda: self.back(-1))
       label=Label(self.fc[1],text=memberList[self.imagePointer], background=colorPalette[0], font="Bitter 11")
       forward=Button(self.fc[1],text=">>",bg=colorPalette[0],command=lambda: self.next(1))
           
       previous.grid(row=0,column=0)
       label.grid(row=0,column=1)
       forward.grid(row=0,column=2)
          
    def frameClear(self):
       for i in self.fc:
         for widgets in i.winfo_children():
           widgets.destroy()
          
    def back(self,i):
        self.frameClear()
        if(self.imagePointer>0):
          self.imagePointer=self.imagePointer+i
          self.eventGen()
          return 
          
    def next(self,i):
        self.frameClear()
        self.imagePointer=(self.imagePointer+i)%4
        self.eventGen()
        return
           
    def eventGen(self):
        self.frameGen()
        self.imageLayout(self.imagePointer)
        self.layout()
    
AboutWindows().windSize()
AboutContainer().eventGen()
abtWindObj.mainloop()