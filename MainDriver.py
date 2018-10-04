import sys

sys.path.append(r"C:\Users\Harshit\PycharmProjects\ImageCryptography")
from Socket import *


def main():
    s1 = Socket()

    #print(s1.CloseConnection())
    print(s1.EstablishConnection("192.168.43.98", 9999))


if __name__== "__main__":
    main()