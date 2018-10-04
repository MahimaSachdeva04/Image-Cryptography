import sys
import os
sys.path.append(os.path.abspath(__file__))
from header import *
from Connection import *
from FileOperations import *

class GUI:
    pass

    def __init__(self):

        self.Conn = Connection()
        self.Fop = FileOperations()


    def AlertWindow(self, msg):

        master = Tk()

        master.title("Connection Status")
        master.geometry("300x100")

        Text = Label(master, text=msg)
        Text.pack()
        Text.place(relx=.5, rely=0.25, anchor="center")

        button = Button(master, text="   Ok   ", command=lambda: self.CloseWindow(master))
        button.pack()
        button.place(relx=.5, rely=.8, anchor="center")


    def RetrieveInput(self, ipTextBox):

        ipAddress = ipTextBox.get("1.0", "end-1c")

        if (len(ipAddress) == 0):
            msg = "\nInvalid Arguments!\nPlease enter correct details!\n"
            self.AlertWindow(msg)

            return

        msg = self.Conn.EstablishConnection(ipAddress)
        self.AlertWindow(msg)


    def IPWindow(self):

        if self.Conn.connStatus == "TRUE":
            msg = "\nConnection previously established!\nTo create new connection first Disconnect!\n"
            self.AlertWindow(msg)

            return

        master = Tk()

        master.title("Connection Parameters")
        master.geometry("300x150")

        ipText = Label(master, text="\nEnter IP Address")
        ipText.pack()

        ipTextBox = Text(master, height=1, width=25)
        ipTextBox.pack()
        ipTextBox.place(relx=.5, rely=.35, anchor="center")

        button = Button(master, text="   Ok   ",
                        command=lambda: [self.RetrieveInput(ipTextBox), self.CloseWindow(master)])
        button.pack()
        button.place(relx=.5, rely=0.70, anchor="center")


    def RootWindow(self):

        #Creating Root Window
        root = Tk()

        root.title("GUI_Application")

        width, height = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry('%dx%d+0+0' % (width, height-50))

        canvas = Canvas(root, width=1366, height=120)
        canvas.pack()

        canvas.create_rectangle(5, 10, 1360, 60)
        canvas.create_window(10, 5, anchor=NW, window=Label(root, text="Image Options"))

        canvas.create_rectangle(5, 70, 1360, 120)
        canvas.create_window(10, 65, anchor=NW, window=Label(root, text="Connection Options"))


        # Path To Choose Image File
        path = "/"
        L1B1 = Button(text="Open Image", command=lambda: [self.Fop.OpenImage(root, path)])
        L1B1.place(relx=.007, rely=0.040)

        L1B2 = Button(text="View Send Images", command=lambda: [self.Fop.OpenImage(root, "SendFiles")])
        L1B2.place(relx=.818, rely=0.040)

        L1B3 = Button(text="View Received Images", command=lambda: [self.Fop.OpenImage(root, "ReceivedFiles")])
        L1B3.place(relx=.900, rely=0.040)

        L2B1 = Button(text="Create Connection", command=lambda: self.IPWindow())
        L2B1.place(relx=.007, rely=0.121)

        L2B2 = Button(text="Start Server", command=lambda: self.AlertWindow(self.Conn.WaitForConnection()))
        L2B2.place(relx=.092, rely=0.121)

        L2B3 = Button(text="Disconnect", command=lambda: self.AlertWindow(self.Conn.CloseConnection()))
        L2B3.place(relx=.148, rely=0.121)

        L3B1 = Button(text="    Send    ", command=lambda: self.AlertWindow(self.Fop.SendImage(self.Conn)))
        L3B1.place(relx=.470, rely=.950, anchor="center")

        L3B2 = Button(text="  Receive  ", command=lambda: self.AlertWindow(self.Fop.ReceiveImage(self.Conn)))
        L3B2.place(relx=.530, rely=.950, anchor="center")

        root.mainloop()


    def CloseWindow(self, root):
        root.destroy()

g1 = GUI()
g1.RootWindow()