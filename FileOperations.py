import sys
import os
sys.path.append(os.path.abspath(__file__))
from header import *
from Crypter import *

class FileOperations:
    loadedImage = ""

    def __init__(self):
        self.Cryp = Crypter()

    # Function to Open the Image File
    def OpenImage(self, root, path):

        resizedImage = 0
        originalImage = ""

        # Selecting Image File
        root.loadedImage = askopenfilename(initialdir=path)

        # Checking if any Image File was selected
        if root.loadedImage == "":
            root.loadedImage = self.loadedImage
        else:
            self.loadedImage = root.loadedImage

        if root.loadedImage == "":
            return

        # Opening Image File
        originalImage = Image.open(root.loadedImage)
        # Calculating Dimensions of the selected Image File
        width, height = originalImage.size

        # Checking Dimensions of the selected Image File
        if(width > 840):
            width = 840

        if(height > 500):
            height = 500

        # Setting the Dimensions of the Image File
        resizedImage = originalImage.resize((width, height), Image.ANTIALIAS)

        # Opening Image File in Tkinter Window
        root.loadedImage = ImageTk.PhotoImage(resizedImage)

        # Setting Labels for the Image File
        label = Label(root, image=root.loadedImage)
        label.place(relx=0.5, rely=0.55, anchor="center")


    # Function to Save the Image File
    def SaveFile(self, path, imageName):

        # Opening Source Image File
        with open(imageName, "rb") as fpSrc:
            data = fpSrc.read()
            fpSrc.close()

        # Extracting the name of the Image File
        imageName = imageName.split('/')[-1]

        # Setting Destination for the Image File
        destFile = path + imageName

        # Opening Destination Image File
        with open(destFile, "wb") as fpDest:
            fpDest.write(data)
            fpDest.close()


    # Function to Send the Image File
    def SendImage(self, Conn):

        imageSize = 0
        imageName = ""
        imageMetaData = ""

        # Check if the Image File was Loaded
        if self.loadedImage == "":
            msg = "\nNo Image has been Loaded!\nLoad any Image First!\n"

            return msg

        # Check Connection Status
        if Conn.connStatus == "FALSE":
            msg = "\nDisconnected!\nEstablish Connection First!\n"

            return msg

        # Encrypting Image
        encryptedImage = self.Cryp.ImageEncrypter(self.loadedImage)

        # Extracting Size of the Image File
        imageSize = os.path.getsize(encryptedImage)

        # Extracting Name of the Image File
        imageName = encryptedImage.split('/')[-1]

        # Concatinating the Image File Name with its Size
        imageMetaData = str(imageSize) + "~" + imageName

        """msg = "\nSending Image!\nPlease Wait!\n"
        alert_window(msg)"""

        acknowledgement = 0
        i = 1
        while i <= 3:
            i = i + 1

            # Sending Image Meta-Data
            Conn.Socket.send((str(imageMetaData)).encode('utf8'))

            # Opening File and Setting File Pointer
            with open(encryptedImage, "rb") as fp:

                # Sending File
                Conn.Socket.sendall(fp.read())

                # Receiving Acknowledgement
                acknowledgement = Conn.Socket.recv(1024).decode();
                acknowledgement = str(acknowledgement)

                if acknowledgement == "1":
                    # Closing File
                    fp.close()

                    path = "SendFiles/"
                    self.SaveFile(path, self.loadedImage)

                    msg = "\nCongratulations!\nFile was successfully Send!\n"
                    return msg

        # Checking Acknowledgement Status
        if acknowledgement == "0":
            msg = "\nSorry!\nFile Could Not be Send!\nCheck Your Connection Status!\n"

            return msg

    # Function To Receive File
    def ReceiveImage(self, Conn):

        imageSize = 0
        imageName = ""
        imageMetaData = ""
        recievedImage = ""

        # Check Connection Status
        if Conn.connStatus == "FALSE":
            msg = "\nDisconnected!\nEstablish Connection First!\n"
            return msg


        startTime = time.time()
        while True:
            # Receive Image Meta-Data
            imageMetaData = Conn.conn.recv(2048).decode()

            # Separate Image Size and Image Name
            imageSize = str(imageMetaData).split('~')[0]
            imageName = str(imageMetaData).split('~')[1]

            # Retrieving File Size
            imageSize = int(imageSize)

            recievedImage = "ReceivedFiles/EncryptedImages/" + imageName

            # Opening File
            fp = open(recievedImage, "wb")

            tempImageSize = 0
            while True:
                # Getting File Data Bytes
                imageData = Conn.conn.recv(4096)
                # Calculating File Data Received
                tempImageSize += len(imageData)

                # Write Data Bytes On File
                fp.write(imageData)

                # Checking if File Fully Received
                if (tempImageSize - imageSize == 0):
                    # Closing Image File
                    fp.close()

                    self.Cryp.ImageDecrypter(recievedImage)

                    acknowledgement = 1
                    acknowledgement = str(acknowledgement)
                    Conn.conn.send(acknowledgement.encode("utf8"))

                    msg = "\nCongratulations!\nFile was successfully Received!\n"
                    return msg

                endTime = time.time()
                if(endTime - startTime >= 120):
                    msg = "\nSorry!\nFile was not Received Completely!\n"
                    return msg