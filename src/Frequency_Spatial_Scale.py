#######To clear the working memory###########
from scipy.fftpack.basic import fft2
def clearall():
    all = [var for var in globals() if var[0] != "_"]
    for var in all:
        del globals()[var]
#############################################
 
clearall()
 
# imports necessary for this exercise       
import re
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft2, fftshift, ifft2






 
# Function to read a pgm image from a file
def read_pgm(filename, byteorder='>'):
    """Return image data from a raw PGM file as numpy array.
 
    Format specification: http://netpbm.sourceforge.net/doc/pgm.html
 
    """
    with open(filename, 'rb') as f:
        buffer = f.read()
    try:
        header, width, height, maxval = re.search(
            b"(^P5\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n]\s)*)", buffer).groups()
    except AttributeError:
        raise ValueError("Not a raw PGM file: '%s'" % filename)
    return np.frombuffer(buffer,
                            dtype='u1' if int(maxval) < 256 else byteorder+'u2',
                            count=int(width)*int(height),
                            offset=len(header)
                            ).reshape((int(height), int(width)))
 
# Function used in this computer exercise to display an images                                   
def displayImage(image):
    plt.imshow(image, plt.cm.gray, vmin=0, vmax=255)
    plt.show()






if __name__ == "__main__":
    path = "../resource/wheele.pgm"
    img = read_pgm(path)
    displayImage(img)
    tab = fft2(img)
