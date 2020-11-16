from cs1media import *

original_picture_path = "original_pictures/"
steganography_picture_path = "steganography_pictures/"
hiding_picture_path = "hiding_pictures/"

letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "."]

# ------------------------------------------------------------------
# 1. integer_to_binary
# ------------------------------------------------------------------
# Input 	: integer i, integer l (integer value, length)
# Output 	: string (binary string)
# ------------------------------------------------------------------
# Convert an integer value into a binary string
def integer_to_binary(i, l):
    binum = ''
    for k in range(l):
        remainder = i/(2**(l-k-1))
        binum += str(remainder)
        if remainder == 1:
            i = i-remainder*(2**(l-k-1))
    return binum


# ------------------------------------------------------------------
# 2. binary_to_integer
# ------------------------------------------------------------------
# Input 	: string bs (binary string)
# Output 	: integer (integer value)
# ------------------------------------------------------------------
# Convert a binary string into an integer value
def binary_to_integer(bs):
    intnum = 0
    for i in range(len(bs)):
        intnum += int(bs[i])*(2**(len(bs)-i-1))
    return intnum


# ------------------------------------------------------------------
# 3. text_to_binary
# ------------------------------------------------------------------
# Input 	: string ts (text string)
# Output 	: string (binary string) or None
# ------------------------------------------------------------------
# Convert a text string into a binary string
def text_to_binary(ts):
    binum = '0'
    if len(ts)>255:
        return None
    binum += integer_to_binary(len(ts), 8)
    for j in range(len(ts)):
        position = letter_list.index(ts[j])
        binum += integer_to_binary(position, 6)
    return binum


# ------------------------------------------------------------------
# 4. binary_to_text
# ------------------------------------------------------------------
# Input 	: string bs (binary string)
# Output 	: string (text string)
# ------------------------------------------------------------------
# Convert a binary string into a text string
def binary_to_text(bs):
    text = ''
    length = binary_to_integer(bs[1:9])
    for k in range(length):
        num = binary_to_integer(bs[9+6*k:15+6*k])
        text += letter_list[num]
    return text


# ------------------------------------------------------------------
# 5. image_to_binary
# ------------------------------------------------------------------
# Input 	: image img (image data)
# Output 	: string (binary string)
# ------------------------------------------------------------------
# Convert an image data into a binary string
def image_to_binary(img):
    w, h = img.size()
    if w>127 or h>127:
        return None
    binum = '1'
    binum += integer_to_binary(w, 7)
    binum += integer_to_binary(h, 7)    
    for x in range(w):
        for y in range(h):
            r, g, b = img.get()
            binum += integer_to_binary(r, 8)
            binum += integer_to_binary(g, 8)
            binum += integer_to_binary(b, 8)
    return binum
    

# ------------------------------------------------------------------
# 6. binary_to_image
# ------------------------------------------------------------------
# Input 	: string bs (binary string)
# Output 	: image (image data)
# ------------------------------------------------------------------
# Convert a binary string into an image data
def binary_to_image(bs):
    w = binary_to_integer(bs[1:8])
    h = binary_to_integer(bs[8:15])
    image = create_picture(w, h)
    for x in range(w):
        for y in range(h):
            r = binary_to_integer(bs[15+24*(x*h+y):23+24*(x*h+y)])
            g = binary_to_integer(bs[23+24*(x*h+y):31+24*(x*h+y)])
            b = binary_to_integer(bs[31+24*(x*h+y):39+24*(x*h+y)])            
            image.set(x, y, (r, g, b))
    return image

# ------------------------------------------------------------------
# 7. hiding
# ------------------------------------------------------------------
# Input 	: string bs, string img_fname (binary string, image file name)
# Output 	: None (no return)
# ------------------------------------------------------------------
# Hide a binary string into a big image file
def hiding(bs, img_fname):
    image = load_picture(original_picture_path + img_fname)
    w, h = image.size()
    for x in range(w):
        for y in range(h):
            r, g, b = image.get(x, y)
            if r%2 == 1:
                r = r-1
            if g%2 == 1:
                g = g-1 
            if b%2 == 1:
                b = b-1
            if 3 * (h*x+y) < len(bs):
                r = r + int(bs[0+3*(h*x+y)])
                g = g + int(bs[1+3*(h*x+y)])
                b = b + int(bs[2+3*(h*x+y)])
            image.set(x, y, (r, g, b))
    image.save_as(steganography_picture_path+img_fname)
    
    
# ------------------------------------------------------------------
# 8. extracting
# ------------------------------------------------------------------
# Input 	: string img_fname (image file name)
# Output 	: None (no return)
# ------------------------------------------------------------------
# Show hiddne information in a big image file.
def extracting(img_fname):
    image=load_picture(steganography_picture_path+img_fname)
    w, h = image.size()    


def main():
    select_1 = -1
    while select_1 != 0:
        select_1 = input("===============================\n0. Exit\n1. Hiding data\n2. Extracting data\n===============================\nSelect a menu : ")
        if select_1 == 1:
            select_2 = input("===============================\n1. Hiding text\n2. Hiding image\n===============================\nSelect a menu : ")
            img_fname = raw_input("Enter an image file name for hiding : ")
            if select_2 == 1:
                text = raw_input("Enter text data : ")
                hiding(text_to_binary(text), img_fname)
            elif select_2 == 2:
                image = raw_input("Enter a hiding image file name: ")
                img = load_picture(hiding_picture_path + image)
                hiding(image_to_binary(img), img_fname)
            else :
                print "Wrong input! Please try again!"
        elif select_1 == 2:        
            img_fname = raw_input("Enter an image file name for extracting : ")            
            extracting(img_fname)
        elif select_1 == 0:
            print "Program is terminated"
        else :
            print "Wrong input! Please try again!"
            
main()