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






#--------------------------------------------------- 
# Question 1.1
#--------------------------------------------------- 
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


#--------------------------------------------------- 
# Question 1.2
#--------------------------------------------------- 
# Computes the sum of all the pixels of the input image
def sumPixel(img):
    (width, height) = img.shape
    sum             = 0
    for x in xrange(width):
        for y in xrange(height):
            sum += img[x, y]
    return sum

# return the list of solutions (u, v) such as ft2D(u, v) = s
def solveDiscretEquationFT(ft2d, s):
    res = []
    for x in xrange(len(ft2d)):
        for y in xrange(len(ft2d[0])):
            if ft2d[x, y] == s:
                res.append((x, y))
    return res
        


#--------------------------------------------------- 
# Question 1.2
#--------------------------------------------------- 
def powerSpectrum(ft2d):
    res     = []
    epsilon = np.finfo(float).eps
    for x in xrange(len(ft2d)):
        for y in xrange(len(ft2d[0])):
            val             = ft2d[x][y]
            magnitudeSquare = val.imag * val.imag + val.real * val.real
            res.append(np.log(magnitudeSquare + epsilon))
    return res

    




if __name__ == "__main__":
    path = "../resource/wheele.pgm"
#    path = "../resource/damierHV.pgm"

# Question 1.1
    img = read_pgm(path)
    displayImage(img)

# Question 1.2
    ft2d    = fft2(img)
    sum     = sumPixel(img)
    freqSol = solveDiscretEquationFT(ft2d, sum)
    
# Question 1.3
    (width, height) = img.shape
    epsilon         = np.finfo(float).eps
    axis            = np.array(range(width*height))
    spectrum        = powerSpectrum(ft2d)
    plt.figure()
    plt.plot(axis, spectrum, label='Square modulus of the 2D Fourier transform (log scale)')
    plt.grid()
    plt.xlabel('Pixel\'s index (= x + y*width)')
    plt.ylabel('log(modulus(ft(x, y))^2)')
    plt.legend('TODO')
    plt.show()

# Question 1.4



