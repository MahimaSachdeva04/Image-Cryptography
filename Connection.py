import sys
import os
sys.path.append(os.path.abspath(__file__))
from header import *

class Connection:
    Socket = 0
    conn = 0
    addr = 0
    connStatus = "FALSE"
    hostIP = ""
    portNumber = 9999

    # Default Constructor
    def __init__(self):

        # Creating SOCKET Object
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def ParametersInitializer(self):
        self.conn = 0
        self.addr = 0
        self.connStatus = "FALSE"
        self.hostIP = ""

    # Function to Establish Connection
    def EstablishConnection(self, hostIP):

        self.hostIP = hostIP

        # Connecting To IP
        try:
            self.Socket.connect((self.hostIP, self.portNumber))

            self.connStatus = "TRUE"
            msg = "\nCongratulations!\nConnection Successfully Established With The Server!\n"

        except Exception as excep:
            msg = "\nSorry!\nError Establishing Connection!\n"

        return msg

    # Function to Wait For Client
    def WaitForConnection(self):

        self.Socket.bind((self.hostIP, self.portNumber))
        self.Socket.listen(5)

        try:
            self.conn, self.addr = self.Socket.accept()

            msg = "\nCongratulations!\nConnection Established Successfully!\nAddress: "#, self.addr
            self.connStatus = "TRUE"

        except Exception as excep:
            msg = "\nSorry!\nError Connecting With Client!\n"

        return msg

    # Function to Terminate Established Connection
    def CloseConnection(self):

        # Checking Connection Status
        if self.connStatus == "TRUE":
            self.Socket.close()
            self.ParametersInitializer()

            msg = "\nConnection Terminated!\n"

        else:
            msg = "\nNo Connection Found!\n"

        return msg