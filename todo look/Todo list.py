from tkinter import *
import tkinter.messagebox as messagebox
import datetime


# function Button

def Update():
    A = st_Entry.get()
    if A:
        Task.append(A)
        st_Entry.delete(0,END)
        list_box.insert(0,A)
        date = datetime.datetime.now()


        with open("Task.txt","a") as f:
            f.write(f"{date.strftime('%c')}\n{A}\n")

def delete():
    select_index = list_box.curselection()
    if select_index:
        index = int(select_index[0])
        del Task[index]
        list_box.delete(index)
        list_box.update()

    else:
        messagebox.showwarning("Alert","Please select a task to remove.😢")




# --------------------------------------
def file():
    pass

# -----------------------------------------
root = Tk()

root.geometry("800x450")
root.title("Todo List")
root.wm_iconbitmap("task_icon.ico")
Task = []
root.config(background="#5783db")

mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="Coming Soon",command=file)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

st = StringVar()


lable = Label(root,text="ADD TASK",font="Arial 14 bold",bg="#5783db",fg="white")
lable.pack(pady=10)

st_Entry = Entry(root,textvariable=st,relief=SUNKEN,width=40)
st_Entry.pack(pady=10)


lable1 = Label(root,text="YOUR TASK",font="Arial 14 bold",bg="#5783db",fg="White")
lable1.pack(pady=25)

list_box =Listbox(root,width=120)
list_box.pack()

frame =Frame(root,borderwidth=20,bg="#5783db")
Update = Button(frame,text="Update",font="Arial 10 bold",command=Update,bg="#80669d",fg="white")
Update .pack(side=LEFT,padx=30)


delete = Button(frame,text="Delete",font="Arial 10 bold",command=delete,bg="#5dbea3",fg="white")
delete .pack(side=RIGHT,padx=30)

frame.pack()

root.mainloop()