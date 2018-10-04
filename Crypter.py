
import sys
import os
sys.path.append(os.path.abspath(__file__))
from header import *

class Crypter:

    def __init__(self):
        c = 0
        # Nothing Required

    def ImageEncrypter(self, loadedImage):

        fp = open(loadedImage, 'rb')
        image = fp.read()
        fp.close()

        image = bytearray(image)

        key = 48
        for index, value in enumerate(image):
            image[index] = value ^ key

        path = "SendFiles/EncryptedImages/en_" +loadedImage.split('/')[-1]

        fp = open(path, 'wb')
        fp.write(image)
        fp.close()

        return path

    def ImageDecrypter(self, encrptedImage):

        fp = open(loadedImage, 'rb')
        image = fp.read()
        fp.close()

        image = bytearray(image)

        key = 48
        for index, value in enumerate(image):
            image[index] = value ^ key

        temp = encrptedImage.split('/')[-1]
        temp = temp.split('_')[-1]

        path = "ReceivedFiles/" + temp

        fp = open(path, 'wb')
        fp.write(image)
        fp.close()

        return