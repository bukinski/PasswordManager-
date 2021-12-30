#from os import replace
from tkinter import *
from cryptography.fernet import Fernet

class Delete(Button):
    def delete(self):

        class MyButton(Button):
            def action(self):
                
                service = E1.get()
                username = E2.get()
                password = E3.get()

                f=open("secretKey.txt", "r")
                secretKey=f.readlines()
                f.close()
                #print("secret key: ", secretKey)
                strSecretKey=str(secretKey[0])
                secretKeyBytes=strSecretKey.encode()
                #print("secretKey bytes: ", secretKeyBytes)

                key = secretKeyBytes
                fernet = Fernet(key)

                def closeSuccessWindows():
                    successwindow.destroy()
                    deletewindow.destroy()
                
                def closeFailWindows():
                    failwindow.destroy()
                    deletewindow.destroy()

                f=open("encData.txt", "r")
                content = f.readlines()
                f.close()

                credentialsDel = False

                for i in range(0, len(content), 4):
                    #print("lenght content",  len(content))
                    #print("loop nr  ", i)
                    if content[i] != "\n":
                        strContentToken = content[i]
                        stripContentToken = strContentToken.strip()
                        encContentToken = stripContentToken.encode()
                        decContentToken1 = fernet.decrypt(encContentToken).decode()

                        if content[i+1] != "\n":
                            strContentToken = content[i+1]
                            stripContentToken = strContentToken.strip()
                            encContentToken = stripContentToken.encode()
                            decContentToken2 = fernet.decrypt(encContentToken).decode()

                            if content[i+2] != "\n":
                                strContentToken = content[i+2]
                                stripContentToken = strContentToken.strip()
                                encContentToken = stripContentToken.encode()
                                decContentToken3 = fernet.decrypt(encContentToken).decode()

                    if decContentToken1==service and decContentToken2==username and decContentToken3==password:
                        content = content[:i] + content[i+4:]
                        f=open("encData.txt", "w")
                        for line in content:
                            f.write(line)
                        f.close()
                        credentialsDel = True
                        break

                if credentialsDel==True:
                    successwindow = Tk()
                    successwindow.geometry("300x100")
                    successwindow.title("Evaluation")
                    frame2 = Frame(successwindow, relief="ridge", borderwidth=5, bg="light blue") 
                    frame2.pack(fill="both", expand = 1)
                    label = Label(frame2, text = "Credentials deleted successfully!", bg="light blue")
                    label.config(font=("Arial", 12, "bold"))
                    label.pack()

                    button1= Button(frame2, text = "OK", width = 5, height = 2)
                    button1.config(font = ("arial", 12, "bold"), command=closeSuccessWindows)
                    button1.pack()
                    successwindow.mainloop()
                else:
                    failwindow = Tk()
                    failwindow.geometry("300x100")
                    failwindow.title("Evaluation")
                    frame2 = Frame(failwindow, relief="ridge", borderwidth=5, bg="light blue") 
                    frame2.pack(fill="both", expand = 1)
                    label = Label(frame2, text = "Input incomplete or not existent!", bg="light blue")
                    label.config(font=("Arial", 12, "bold"))
                    label.pack()

                    button1= Button(frame2, text = "OK", width = 5, height = 2)
                    button1.config(font = ("Arial", 12, "bold"), command=closeFailWindows)
                    button1.pack()
                    failwindow.mainloop()

        deletewindow = Tk()
        deletewindow.geometry("600x300")
        deletewindow.title("Delete some of passwords, fucker!")
        frame=Frame(deletewindow, relief="ridge", borderwidth=5, bg = "light blue")
        frame.pack(fill="both", expand=1)

        label = Label(frame, text = "Enter service and username to delete:", bg = "light blue")
        label.pack(pady=20)
        label.config(font = ("Arial", 14, "bold"))

        L1 = Label(frame, text = "Enter service: ", bg = "light blue")
        L1.place(x = 110, y = 100)
        L1.config(font = ("Arial", 12, "bold"))
        E1 = Entry(frame, bd = 2, width = 25)
        E1.place(x = 310, y = 100)
        E1.config(font = ("Arial", 12, "bold"))

        L2 = Label(frame, text = "Enter username: ", bg = "light blue")
        L2.place(x = 110, y = 140)
        L2.config(font = ("Arial", 12, "bold"))
        E2 = Entry(frame, bd = 2, width = 25)
        E2.place(x = 310, y = 140)
        E2.config(font = ("Arial", 12, "bold"))

        L3 = Label(frame, text = "Enter password: ", bg = "light blue")
        L3.place(x = 110, y = 180)
        L3.config(font = ("Arial", 12, "bold"))
        E3 = Entry(frame, bd = 2, width = 25)
        E3.place(x = 310, y = 180)
        E3.config(font = ("Arial", 12, "bold"))

        okButton=MyButton(frame, text="Delete", width=10, height=2)
        okButton["command"]=okButton.action
        okButton.pack(side="bottom", pady=20)
        okButton.config(font = ("arial", 12, "bold"))

        deletewindow.mainloop()