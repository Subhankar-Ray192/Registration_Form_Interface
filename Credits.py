import tkinter as window

from tkinter import *
from PIL import Image,ImageTk

memberList=["Subhankar Ray","Tanir Sahoo"]
postList=["Project Manager","Frontend Developer","Backend Developer"]
colorPalette=["#ffffff"]



abtWindObj=window.Tk()
abtWindObj.title("Credits")



class Windows:
  
  def __init__(self):
   self.height=500
   self.width=600

  def windSize(self):
   abtWindObj.geometry("500x500")
   abtWindObj.minsize(self.height,self.width)
   abtWindObj.maxsize(self.height,self.width)
   abtWindObj["bg"]=colorPalette[0]
   
class Component:
  
  def __init__(self):
    self.fc=[]
    return

  def frameGen(self):
    for i in range(2): 
      self.fc.append(Frame(abtWindObj,relief=SUNKEN,height=50,width=700,bg=colorPalette[0]))

   
  def imageLayout(self):
   
   global profilePic
   profilePic=Image.open("Credits_Picture1.png")
   
   global resizedProfilePic
   resizedProfilePic=profilePic.resize((500,500))
   
   global img 
   img=ImageTk.PhotoImage(resizedProfilePic)
   
   self.fc[0].pack(side=TOP,expand=False)
   self.fc[0].pack_propagate(0)
   
   label=Label(image=img)
   label.pack()
   
   self.fc[1].pack(side=TOP,expand=False)
   self.fc[1].pack_propagate(0)
  
  def layout(self):
   label=Label(self.fc[0],text="Registration App: V.2.4.13", background=colorPalette[0], font="System 15")
   label.pack()
   
   previous=Button(self.fc[1],text="<<",bg=colorPalette[0])
   label=Label(self.fc[1],text=memberList[0]+" :: "+postList[0]+" & "+postList[2], background=colorPalette[0], font="Bitter 11")
   forward=Button(self.fc[1],text=">>",bg=colorPalette[0])
   
   previous.grid(row=0,column=0)
   label.grid(row=0,column=1)
   forward.grid(row=0,column=2)
   
  def eventGen(self):
   self.frameGen()
   self.imageLayout()
   self.layout()

def main():
  Windows().windSize()
  Component().eventGen()
  abtWindObj.mainloop()
