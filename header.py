try:
    from tkinter.filedialog import askopenfilename
    from tkinter import *
    from PIL import ImageTk,Image
    import socket
    import time
except Exception as excep:

    print("Error Importing ")

    from tkinter.filedialog import askopenfilename
    from tkinter import *
    from PIL import ImageTk, Image
    import socket
    import time

    print(" Library")