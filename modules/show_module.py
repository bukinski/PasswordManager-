from tkinter import *
from cryptography.fernet import Fernet

class Show(Button):
    def show(self):

        class MyButton(Button):
            def action(self):
                showwindow.destroy()

        showwindow = Tk()
        showwindow.geometry("400x500")
        showwindow.title("Your passwords, fucker!")
        frame = Frame(showwindow, relief = "ridge", borderwidth = 5, bg = "light blue")
        frame.pack(fill = "both", expand = 1)

        label = Label(frame, text = "Saved Passwords:", bg = "light blue")
        label.config(font = ("Arial", 14, "bold"))
        label.pack(pady = 25)

        frame2 = Frame(frame, relief = "ridge",  borderwidth=1)
        frame2.pack()

        f = open("encData.txt", "r")
        content = f.readlines()

        scrollbar = Scrollbar(frame2)
        list = Listbox(frame2, yscrollcommand = scrollbar.set,
        width = 30, height =15, bg = "beige", font=("arial", 12, "bold"))

        f=open("secretKey.txt", "r")
        secretKey=f.readlines()
        f.close()
        #print("secret key: ", secretKey)
        strSecretKey=str(secretKey[0])
        secretKeyBytes=strSecretKey.encode()
        #print("secretKey bytes: ", secretKeyBytes)

        key = secretKeyBytes
        fernet = Fernet(key)

        i=0
        for row in content:
            if i==0:
                row = row.strip()
                row = row.encode()
                row = fernet.decrypt(row).decode()
                output = "Service: "+row
                i+=1
            elif i==1:
                row = row.strip()
                row = row.encode()
                row = fernet.decrypt(row).decode()
                output = "Username: "+row
                i+=1
            elif i==2:
                row = row.strip()
                row = row.encode()
                row = fernet.decrypt(row).decode()
                output = "Password: "+row
                i+=1
            elif i==3:
                output = ""
                i=0

            list.insert(END, output)
        
        f.close()
        
        list.pack(side="left", fill="both")
        scrollbar.config(command = list.yview)
        scrollbar.pack(side = "right", fill = "both")

        okButton = MyButton(frame, text = "OK", width = 10, height = 2)
        okButton["command"] = okButton.action
        okButton.config(font = ("arial", 12, "bold"))
        okButton.pack(side = "bottom", pady = 15)        

        showwindow.mainloop()