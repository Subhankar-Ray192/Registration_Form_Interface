import csv
import os
import numpy as np

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as tmsg
from tkinter import simpledialog

mKey = "123"

preDefinedFilePath = "D:\\DataFolder\\Data.csv"
preDefinedDirPath = "D:\\DataFolder"

windObj = Tk()
colorPalette = ["#ffffff", "#429ef5", "#000000"]
fontStyles = ["Bitter 10"]
header = ["Registration Number:", "First Name:", "Middle Name:", "Last Name:", "Contact Number:", "Email:", "Gender:"]
err = ["0x01:Invalid-Entry", "0x02:Invalid-Character", "0x03:Compulsory-Entry", "0x04:Invalid-Digit"]
gCategory = ["F", "M", "O"]
portal_work = 0

class RegWindow:

    def __init__(self):
        self.height = 500
        self.width = 550
        self.header = "TDSSS and Company"

    def windows(self):
        windObj.geometry("500x550")
        windObj.maxsize(self.height, self.width)
        windObj.minsize(self.height, self.width)
        windObj.title("TDSSS and Company")
        windObj.configure(bg=colorPalette[0])

class view_port:
    def __init__(self):
        self.menuNm = ["Register", "View", "Menu", "Master Terminal", "Admin"]
        self.fc = []
        self.data = []
        self.eObj = []
        self.fh = fileHandle()
        self.er = Errors()
        self.currGender = ""
        return

    def register(self):
        windObj.destroy()
        import Phase1
        Phase1.RegWindow().windows()
        Phase1.Container().conEvent()
        Phase1.windObj.mainloop()

    def view(self):
        tmsg.showinfo("view-portal", "You are inside the view portal.")

    def menu(self):
        yourmenu = Menu(windObj)
        m_first = Menu(yourmenu, tearoff=0)
        m_first.add_command(label=self.menuNm[0], command=lambda: self.register())
        m_first.add_command(label=self.menuNm[1], command=lambda: self.view())
        yourmenu.add_cascade(label=self.menuNm[2], menu=m_first)

        m_second = Menu(yourmenu, tearoff=0)
        m_second.add_command(label=self.menuNm[3], command=lambda: self.fh.viewData())
        yourmenu.add_cascade(label=self.menuNm[4], menu=m_second)
        windObj.config(menu=yourmenu)






    def frameGen(self, bd, wd, ht):
        self.fc.append(Frame(windObj, borderwidth=bd, relief=SUNKEN, width=wd, height=ht))
        for i in range(3):
            self.fc.append(Frame(windObj, borderwidth=bd, relief=SUNKEN))

        self.fc[0].pack(side="top", expand=False)
        self.fc[0].configure(bg=colorPalette[1])
        self.fc[0].pack_propagate(0)

        self.fc[1].pack(side="top", pady=(20, 0))
        self.fc[1].configure(bg=colorPalette[0])

        self.fc[2].pack(side="top", pady=(10, 0))
        self.fc[2].configure(bg=colorPalette[0])

        self.fc[3].pack(side="top", pady=(10, 0), expand=False)
        self.fc[3].configure(bg=colorPalette[0])
        self.fc[3].pack_propagate(0)




    def fetch_reg_info(self):
            print("You are trying to fetch the data out of the excel sheet.")


    def layout(self):
        lObj = []

        gSelect = 0

        rObj = []





        heading_label = Label(self.fc[0] , text="WELCOME TO TDSSS & COMPANY" , fg="white" , bg="#429ef5" , font="Courier 18 bold")
        heading_label.pack(side="top" , pady=(40 , 20))

        heading_label_2 = Label(self.fc[0] , text="Check your registration status in this portal" , fg="white" , bg="#429ef5" , font="System 15 bold" , pady=0)
        heading_label_2.pack(side="top")


        Label(self.fc[1], text="Registration Number: ", bg="white", font="Bitter 10").grid(row=1, column=1)

        regis_number = StringVar()
        Entry(self.fc[1], bg="white", font="Bitter 10", textvariable=regis_number, highlightbackground="black",
          highlightthickness=1).grid(row=1, column=2)

        Button(self.fc[2], text="Fetch Info", command=self.fetch_reg_info, bg="#429ef5", fg="white", font="Bitter 10", padx=10, pady=2).grid(row=1, column=1)

        Label(self.fc[3], text="----------------------------------------------------------------------------------------",
          font="Bitter 10", bg="white").grid(row=1, column=1)
        Label(self.fc[3], text="This Label is under construction by TDSSS and Company", font="Bitter 10",
          bg="white").grid(row=2, column=1)
        Label(self.fc[3], text="----------------------------------------------------------------------------------------",
          font="Bitter 10", bg="white").grid(row=3, column=1)






    
    def viewevent(self):
        self.menu()
        self.frameGen(0 , 500 , 150)
        self.layout()

class fileHandle:

    def __init__(self):
        return

    def createFile(self):
        f = open(preDefinedFilePath, "w", newline="")
        csvWriter = csv.writer(f)
        csvWriter.writerow(header)

    def writeData(self, data):
        print("Data:", data)
        if (not self.isRepeatEntry(data)):
            f = open(preDefinedFilePath, "a", newline="")
            csvWriter = csv.writer(f)
            csvWriter.writerow(data)
            f.close()

    def viewData(self):
        dialogueBox = Tk()
        dialogueBox.withdraw()
        key = simpledialog.askstring(title="Master Key", prompt="Key?")
        if (key == mKey):
            os.system(r"D:\\DataFolder\\Data.csv")
        dialogueBox.destroy()

    def isRepeatEntry(self, data):
        rows = []
        rows = np.array(self.readData())
        for i in range(len(rows)):
            if ((rows[i][0] == data[0]) or (rows[i][5] == data[5])):
                return True
        return False

    def readData(self):
        f = open(preDefinedFilePath, "r")
        csvReader = csv.reader(f)
        tempVar = next(csvReader)
        rows = []
        for i in csvReader:
            rows.append(i)
        f.close()
        return rows

class Errors:

    def reg(self, num):
        k = num.isalnum()
        if k == True:
            if len(num) == 5:
                return 5
            else:
                return 0
        else:
            return 1

    def names(self, f, m, l):
        if len(f) == 0 or len(l) == 0:
            return 2
        else:
            f1 = f.isalpha()
            l1 = l.isalpha()
            m1 = True
            if len(m) != 0:
                m1 = m.isalpha()
                if f1 is True and m1 is True and l1 is True:
                    return 5
                else:
                    return 1
            else:
                if f1 is True and l1 is True:
                    return 5
                else:
                    return 1

    def phone(self, n):
        if len(n) < 10 or len(n) > 10:
            return 0
        else:
            n1 = n.isdigit()
            if n1 == True:
                return 5
            else:
                return 3

    def mail(self, e):
        if len(e) == 0:
            return 2
        else:
            return 5

    def checker(self, num, f, l, n, e):
        if len(num) == 0 or len(f) == 0 or len(l) == 0 or len(e) == 0 or len(n) == 0:
            return False
        else:
            return True

class pathManager:

    def __init__(self):
        return

    def dirHandler(self):
        if (not os.path.exists(preDefinedDirPath)):
            os.mkdir(preDefinedDirPath)
        self.isFileExist()

    def isFileExist(self):
        if (not os.path.exists(preDefinedFilePath)):
            fileHandle().createFile()
