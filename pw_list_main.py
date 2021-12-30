from tkinter import *
from modules.show_module import *
from modules.save_module import *
from modules.change_module import *
from modules.delete_module import *

class Cancel(Button):
    def action(self):
        quit()

class MasterPwChange(Button):
    def changeMaster(self):

        class MyButton(Button):
            def action1(self):
                
                newPassword = E2.get()

                if masterPassword == []:
                    f = open("masterPassword.txt", "w")
                    #content = f.readlines()
                    #content[0] = newPassword
                    f.write(newPassword)
                    f.close()

                    class MyButton5(Button):
                            def action5(self):
                                masterChanged.destroy()

                    masterChanged = Tk()   
                    masterChanged.geometry("600x200")
                    masterChanged.title("Yeah u got it changed, fucker!")
                    frame5 = Frame(masterChanged, relief = "ridge", borderwidth = 5, bg="light blue")
                    frame5.pack(fill = "both", expand = 1)

                    label = Label(frame5, text = "Password changed!", bg = "light blue")
                    label.pack(pady=20)
                    label.config(font = ("Arial", 14, "bold"))

                    masterPwChangeWindow.destroy()

                    okButton = MyButton5(frame5, text = "OK", width = 12, height = 2)
                    okButton.pack(side="bottom", pady = 20)
                    okButton.config(font = ("arial", 12, "bold"))
                    #okButton.place(x = 320, y = 70)
                    okButton["command"]=okButton.action5


                elif masterPassword != []:
                    f=open("masterPassword.txt", "r")
                    content = f.readlines()
                    f.close()

                    if oldPassword == str(content[0]) or oldPassword == "":
                        class MyButton5(Button):
                            def action5(self):
                                masterChanged.destroy()

                        f = open("masterPassword.txt", "w")
                        content[0]=newPassword
                        f.write(content[0])
                        f.close()

                        masterChanged = Tk()   
                        masterChanged.geometry("600x200")
                        masterChanged.title("Yeah u got it changed, fucker!")
                        frame5 = Frame(masterChanged, relief = "ridge", borderwidth = 5, bg="light blue")
                        frame5.pack(fill = "both", expand = 1)

                        label = Label(frame5, text = "Password changed!", bg = "light blue")
                        label.pack(pady=20)
                        label.config(font = ("Arial", 14, "bold"))

                        masterPwChangeWindow.destroy()

                        okButton = MyButton5(frame5, text = "OK", width = 12, height = 2)
                        okButton.pack(side="bottom", pady = 20)
                        okButton.config(font = ("arial", 12, "bold"))
                        #okButton.place(x = 320, y = 70)
                        okButton["command"]=okButton.action5

                    elif oldPassword != str(content[0]):
                        class MyButton4(Button):
                            def action4(self):
                                oldPwWrong.destroy()

                        oldPwWrong = Tk()   
                        oldPwWrong.geometry("600x200")
                        oldPwWrong.title("Typo, fucker!")
                        frame4 = Frame(oldPwWrong, relief = "ridge", borderwidth = 5, bg="light blue")
                        frame4.pack(fill = "both", expand = 1)

                        label = Label(frame4, text = "Old password wrong, try again!", bg = "light blue")
                        label.pack(pady=20)
                        label.config(font = ("Arial", 14, "bold"))

                        okButton = MyButton4(frame4, text = "OK", width = 12, height = 2)
                        okButton.pack(side="bottom", pady = 20)
                        okButton.config(font = ("arial", 12, "bold"))
                        #okButton.place(x = 320, y = 70)
                        okButton["command"]=okButton.action4

        masterPwChangeWindow = Tk()   
        masterPwChangeWindow.geometry("600x300")
        masterPwChangeWindow.title("I dare you change your master password, fucker!")
        frame1 = Frame(masterPwChangeWindow, relief = "ridge", borderwidth = 5, bg="light blue")
        frame1.pack(fill = "both", expand = 1)

        label = Label(frame1, text = "Change master password", bg = "light blue")
        label.pack(pady=20)
        label.config(font = ("Arial", 14, "bold"))

        f=open("masterPassword.txt", "r")
        masterPassword = f.readlines()
        f.close()
        
        if masterPassword != []:
            L1 = Label(frame1, text = "Old password: ", bg = "light blue")
            L1.place(x = 110, y = 100)
            L1.config(font = ("Arial", 12, "bold"))
            E1 = Entry(frame1, bd = 2)
            E1.place(x = 310, y = 100)
            E1.config(font = ("Arial", 12, "bold"))
            oldPassword = E1.get()

        L2 = Label(frame1, text = "New password: ", bg = "light blue")
        L2.place(x = 110, y = 140)
        L2.config(font = ("Arial", 12, "bold"))
        E2 = Entry(frame1, bd = 2)
        E2.place(x = 310, y = 140)
        E2.config(font = ("Arial", 12, "bold"))

        buttonChangeMaster = MyButton(frame1, text = "OK", width = 12, height = 2)
        buttonChangeMaster.pack(side="bottom", pady = 20)
        buttonChangeMaster.config(font = ("arial", 12, "bold"))
        #buttonChangeMaster.place(x = 320, y = 70)
        buttonChangeMaster["command"]=buttonChangeMaster.action1

        masterPwChangeWindow.mainloop()

f= open("masterPassword.txt", "r")
content = f.readlines()
f.close()

if content is not None:
    masterPwWindow = Tk()   
    masterPwWindow.geometry("600x300")
    masterPwWindow.title("Type in master password, fucker!")
    frame2 = Frame(masterPwWindow, relief = "ridge", borderwidth = 5, bg="light blue")
    frame2.pack(fill = "both", expand = 1)

    label = Label(frame2, text = "Master password, click Enter if none is set", bg = "light blue")
    label.pack(pady=20)
    label.config(font = ("Arial", 14, "bold"))

    L3 = Label(frame2, text = "Master password: ", bg = "light blue")
    L3.place(x = 110, y = 140)
    L3.config(font = ("Arial", 12, "bold"))
    E3 = Entry(frame2, bd = 2)
    E3.place(x = 310, y = 140)
    E3.config(font = ("Arial", 12, "bold"))

 
class MyButton2(Button):
    def action2(self):
        masterInput = E3.get()
        f=open("masterPassword.txt", "r")
        masterPassword = f.readlines()
        #print("Master: ", masterPassword)
        f.close()

        if masterPassword == [] or masterInput == str(masterPassword[0]):
            mainwindow = Tk()   
            mainwindow.geometry("600x400")
            mainwindow.title("Welcome to password manager, fucker!")
            frame = Frame(mainwindow, relief = "ridge", borderwidth = 5, bg="light blue")
            frame.pack(fill = "both", expand = 1)

            label = Label(frame, text = "Welcome to password manager", bg = "light blue")
            label.pack(pady=20)
            label.config(font = ("Arial", 14, "bold"))

            showbutton = Show(frame, text = "Show passwords", width = 20, height = 5, bg="light green")
            showbutton.pack()
            showbutton.config(font = ("arial", 12, "bold"))
            showbutton.place(x = 320, y = 70)
            showbutton["command"]=showbutton.show

            savebutton = Save(frame, text = "Save password", width = 20, height = 5, bg="light green")
            savebutton.pack()
            savebutton.config(font = ("arial", 12, "bold"))
            savebutton.place(x = 60, y = 70)
            savebutton["command"]=savebutton.save

            deletebutton = Delete(frame, text = "Delete password", width = 20, height = 5, bg="light green")
            deletebutton.pack()
            deletebutton.config(font = ("arial", 12, "bold"))
            deletebutton.place(x=320, y=200)
            deletebutton["command"] = deletebutton.delete

            changebutton = Change(frame, text="Change password", width = 20, height = 5, bg="light green")
            changebutton.pack()
            changebutton.config(font = ("arial", 12, "bold"))
            changebutton.place(x = 60, y = 200)
            changebutton["command"] = changebutton.change

            cancelButton=Cancel(frame, text = "Cancel", width = 12, height = 2)
            cancelButton["command"] = cancelButton.action
            cancelButton.place(x = 140, y =325)
            cancelButton.config(font = ("arial", 12, "bold"))

            changeMasterButton=MasterPwChange(frame, text = "Set master", width = 12, height = 2)
            changeMasterButton["command"] = changeMasterButton.changeMaster
            changeMasterButton.place(x = 320, y = 325)
            changeMasterButton.config(font = ("arial", 12, "bold"))

            masterPwWindow.destroy()
        else:
            class MyButton3(Button):
                def action3(self):
                    wrongMasterWindow.destroy()

            wrongMasterWindow=Tk()   
            wrongMasterWindow.geometry("600x200")
            wrongMasterWindow.title("Wrong password, fucker!")
            frame3 = Frame(wrongMasterWindow, relief = "ridge", borderwidth = 5, bg="light blue")
            frame3.pack(fill = "both", expand = 1)

            label = Label(frame3, text = "Wrong password, try again", bg = "light blue")
            label.pack(pady=20)
            label.config(font = ("Arial", 14, "bold"))

            okButton = MyButton3(frame3, text = "OK", width = 12, height = 2)
            okButton.pack(side="bottom", pady = 20)
            okButton.config(font = ("arial", 12, "bold"))
            #okButton.place(x = 320, y = 70)
            okButton["command"]=okButton.action3

buttonCheckMaster = MyButton2(frame2, text = "Enter", width = 12, height = 2)
buttonCheckMaster.pack(side="bottom", pady = 20)
buttonCheckMaster.config(font = ("arial", 12, "bold"))
#buttonCheckMaster.place(x = 320, y = 70)
buttonCheckMaster["command"]=buttonCheckMaster.action2

f=open("masterPassword.txt", "r")
masterPassword = f.readlines()
#masterPassword = masterPassword[0]
#print("Master PW: ", masterPassword)
f.close()

mainloop()