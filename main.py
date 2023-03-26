from tkinter import *
from tkinter import ttk

class Main(object):
    def __init__(self,master):
        self.master = master

        #frames
        mainFrame=Frame(self.master)
        mainFrame.pack()
        #top frames
        topFrame= Frame(mainFrame,width=1350,height=70,bg='#f8f8f8',padx=20,relief=SUNKEN,borderwidth=2)
        topFrame.pack(side=TOP,fill=X)
        #center frame
        centerFrame = Frame(mainFrame,width=1350,relief=RIDGE,bg='#e0f0f0',height=680)
        centerFrame.pack(side=TOP)
        #Center Left frame
        centerLeftFrame = Frame(centerFrame,width=900,height=700,bg='#e0f0f0',borderwidth=2,relief=SUNKEN)
        centerLeftFrame.pack(side=LEFT)
        #center Right frame
        centerRightFrame = Frame(centerFrame,width=450,height=700,bg='#e0f0f0',borderwidth=2,relief=SUNKEN)
        centerRightFrame.pack()

        #search bar
        search_bar = LabelFrame(centerRightFrame,width=440,height=75,text='Search Box',bg='#9bc9ff')
        search_bar.pack(fill=BOTH)
        self.lbl_search=Label(search_bar,text='Search :', font='aerial 12 bold',bg='#9bc9ff',fg='white')
        self.lbl_search.grid(row=0,column=0,padx=20,pady=10)
        self.ent_search=Entry(search_bar,width=30,bd=10)
        self.ent_search.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
        self.btn_search=Button(search_bar,text='Search',font='arial 12',bg='#fcc324',fg='white')
        self.btn_search.grid(row=0,column=4,padx=20,pady=10)

        #list bar
        list_bar = LabelFrame(centerRightFrame, width=440, height=175, text='Search Box', bg='#fcc324')
        list_bar.pack(fill=BOTH)
        lbl_list=Label(list_bar,text='Short By',font='times 16 bold',fg='#2488ff',bg='#fcc324')
        lbl_list.grid(row=0,column=2)
        self.listChoice=IntVar()
        rb1=Radiobutton(list_bar,text='All Books',var=self.listChoice,value=1,bg='#fcc324')
        rb2 = Radiobutton(list_bar, text='In Library', var=self.listChoice, value=2, bg='#fcc324')
        rb3 = Radiobutton(list_bar, text='Borrowed Books', var=self.listChoice, value=3, bg='#fcc324')
        rb1.grid(row=1,column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btn_list=Button(list_bar,text='List Books',bg='#2488ff',fg='white',font='arial 12')
        btn_list.grid(row=1,column=3,padx=40,pady=10)

        #title and image
        image_bar=Frame(centerRightFrame,width=440,height=350)
        image_bar.pack(fill=BOTH)
        self.title_right=Label(image_bar,text='Welcome to the Library',font='arial 16 bold')
        self.title_right.grid(row=0)
        self.img_library=PhotoImage(file='icons/library32.png')
        self.lblimg=Label(image_bar,image=self.img_library)

##########################################Tool Bar#########################################################
        #add book
        self.iconbook=PhotoImage(file='icons/add_book.png')
        self.btnbook= Button(topFrame,text='Add Book',image=self.iconbook,compound=LEFT,font='arial 12 bold')
        self.btnbook.pack(side=LEFT,padx=10)
        #add member button
        self.iconmember=PhotoImage(file='icons/users.png')
        self.btnmember=Button(topFrame,text='Add Member', font='arial 12 bold', padx=10)
        self.btnmember.configure(image=self.iconmember,compound=LEFT)
        self.btnmember.pack(side=LEFT)
        #give book
        self.icongive=PhotoImage(file='icons/givebook.png')
        self.btngive=Button(topFrame,text='Give Book',font='arial 12 bold',padx=10,image=self.icongive,compound=LEFT)
        self.btngive.pack(side=LEFT)


def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1350x750+350+200")
    root.iconbitmap('icons/icon.ico')
    root.mainloop()

if __name__ == '__main__':
    main()
