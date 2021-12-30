from tkinter import *
from cryptography.fernet import Fernet
from .check_existence_function import *

class Save(Button):
    def save(self):

        class MyButton(Button):
            def action(self):

                service = E1.get()
                username = E2.get()
                password = E3.get()
                no_input = ""

                def closeSuccessWindows():
                    successwindow.destroy()
                    savewindow.destroy()

                def closeFailWindows():
                    failwindow.destroy()
                    savewindow.destroy()
                
                #print("Existent: ", checkExistence(service, username, password))

                if (service != no_input and username != no_input and password != no_input and
                    checkExistence(service, username, password) == False):
                    
                    f=open("secretKey.txt", "r")
                    secretKey=f.readlines()
                    f.close()
                    #print("secretKey: ", secretKey)
                    strSecretKey=str(secretKey[0])
                    secretKeyBytes=strSecretKey.encode()
                    #print("secretKey bytes: ", secretKeyBytes)

                    key = secretKeyBytes
                    fernet = Fernet(key)

                    encServiceToken = fernet.encrypt(service.encode())
                    decServiceToken = encServiceToken.decode()
                    strServiceToken = str(decServiceToken)
                    #print("save: "+strServiceToken)

                    encUsernameToken = fernet.encrypt(username.encode())
                    decUsernameToken = encUsernameToken.decode()
                    strUsernameToken = str(decUsernameToken)

                    encPasswordToken = fernet.encrypt(password.encode())
                    decPasswordToken = encPasswordToken.decode()
                    strPasswordToken = str(decPasswordToken)

                    f=open("encData.txt", "a")
                    f.write(strServiceToken+"\n")
                    f.write(strUsernameToken+"\n")
                    f.write(strPasswordToken+"\n")
                    f.write("\n")
                    f.close()

                    successwindow = Tk()
                    successwindow.geometry("300x100")
                    successwindow.title("Evaluation")
                    frame2 = Frame(successwindow, relief="ridge", borderwidth=5, bg="light blue") 
                    frame2.pack(fill="both", expand = 1)
                    label = Label(frame2, text = "Credentials saved!", bg="light blue")
                    label.config(font=("Arial", 12, "bold"))
                    label.pack()
                    button1= Button(frame2, text = "OK", width = 5, height = 2)
                    button1.config(font = ("arial", 12, "bold"), command = closeSuccessWindows)
                    button1.pack()
                    successwindow.mainloop()

                else:
                    failwindow = Tk()
                    failwindow.geometry("300x100")
                    failwindow.title("Evaluation")
                    frame2 = Frame(failwindow, relief="ridge", borderwidth=5, bg="light blue") 
                    frame2.pack(fill="both", expand = 1)
                    label = Label(frame2, text = "Missing input or \n credentials already saved!",
                            bg="light blue")
                    label.config(font=("Arial", 12, "bold"))
                    label.pack()
                    button1= Button(frame2, text = "OK", width = 5, height = 2)
                    button1.config(font = ("Arial", 12, "bold"), command = closeFailWindows)
                    button1.pack()
                    failwindow.mainloop() 

                savewindow.destroy()

        savewindow = Tk()
        savewindow.geometry("600x350")
        savewindow.title("Save new password, fucker!")

        frame = Frame(savewindow, relief = "ridge", borderwidth = 5, bg = "light blue")
        frame.pack(fill = "both", expand = 1)

        label = Label(frame, text = "Enter new credentials:", bg = "light blue")
        label.pack(pady=20)
        label.config(font = ("Arial", 14, "bold"))

        L1 = Label(frame, text = "Service: ", bg="light blue")
        L1.place(x = 110, y = 100)
        L1.config(font = ("Arial", 12, "bold"))
        E1 = Entry(frame, bd = 2, width = 25)
        E1.place(x = 310, y = 100)
        E1.config(font = ("Arial", 12, "bold"))

        L2 = Label(frame, text = "Username: ", bg="light blue")
        L2.place(x = 110, y = 140)
        L2.config(font = ("Arial", 12, "bold"))
        E2 = Entry(frame, bd = 2, width = 25)
        E2.place(x = 310, y = 140)
        E2.config(font = ("Arial", 12, "bold"))

        L3 = Label(frame, text = "Password: ", bg="light blue")
        L3.place(x = 110, y = 180)
        L3.config(font = ("Arial", 12, "bold"))
        E3 = Entry(frame, bd = 2, width = 25)
        E3.place(x = 310, y = 180)
        E3.config(font = ("Arial", 12, "bold"))

        exeButton = MyButton(frame, text = "Write data", width = 10, height = 2)
        exeButton["command"] = exeButton.action
        exeButton.config(font = ("arial", 12, "bold"))
        exeButton.pack(side = "bottom", pady = 50)

        savewindow.mainloop()