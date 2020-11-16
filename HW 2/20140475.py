from cs1graphics_HW2 import *
from time import sleep

# Objects
## Create Scene
scene = Canvas(w = 750, h = 600)

## Load Image
thatcher_face = Image('./Thatcher.png')
thatcher_face.move(250, 330)
scene.add(thatcher_face)

## Add buttons
text_title = Text('Thatcher Effect', fontsize=36)
text_title.move(375, 50)
scene.add(text_title)

layer_step = Layer()

text_title1 = Text('Experiment Steps', fontsize=24)
text_title1.move(0, 0)
layer_step.add(text_title1)

text_rotate_face1 = Text('1. Rotate Face', fontsize=16)
text_rotate_face1.setFontColor('green')
text_rotate_face1.move(0, 50)
layer_step.add(text_rotate_face1)

text_rotate_eye_mouth = Text('2. Rotate Eye and Mouth', fontsize=16)
text_rotate_eye_mouth.move(0, 90)
layer_step.add(text_rotate_eye_mouth)

text_rotate_face2 = Text('3. Rotate Face', fontsize=16)
text_rotate_face2.move(0, 130)
layer_step.add(text_rotate_face2)

text_rotate_face3 = Text('4. Rotate Face Start', fontsize=16)
text_rotate_face3.move(0, 170)
layer_step.add(text_rotate_face3)


text_title2 = Text('Extra Experiment', fontsize=24)
text_title2.move(0, 240)
layer_step.add(text_title2)

text_add_eye_mouth = Text('- Add Eyes & Mouth', fontsize=16)
text_add_eye_mouth.move(0, 280)
layer_step.add(text_add_eye_mouth)


layer_step.move(600, 170)
scene.add(layer_step)


"""
Homework Area Starts
You are not allowed to modify any code until now, but you should revise the code under this area.
Fill the python code to execute the function correctly.
"""
# Rotate 90 degree
def Rotate_90_CW(img):
    """
    Rotate Image class object 90 degrees clockwise
    Parameters
        img: Image class object
    Return value
        new Image class object which is rotated 90 degrees clockwise
    Calling example
        new_img = Rotate_90_CW(thatcher_face)
    """
    w, h = img.size()
    new_img = Image(h, w)

    #----------------------------------------
    # Do something on here !
    for y in range(h):
        for x in range(w):
            new_img.set(h-y-1, x,img.get(x, y))
    
    #----------------------------------------
    
    return new_img


# Rotate 180 degree
def Rotate_180(img):
    """
    Rotate Image class object 180 degrees
    Parameters
        img: Image class object
    Return value
        new Image class object which is rotated 180 degrees
    Calling example
        new_img = Rotate_180(thatcher_face)
    """
    w, h = img.size()
    new_img = Image(w, h)
    
    #----------------------------------------
    # Do something on here !
    for x in range(w):
        for y in range(h):
            new_img.set(w-x-1, h-y-1, img.get(x, y))
    
    #----------------------------------------    
    
    return new_img


# Rotate 180 degree with part of image
def Rotate_180_Part_Rectangle(img, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
    """
    Rotate sub-part of Image class object 180 degrees
    Parameters
        img: Image class object
        top_left_x: Top left point x value
        top_left_y: Top left point y value
        bottom_right_x: Bottom right point x value
        bottom_right_y: Bottom right point y value
    Return value
        new Image class object
    Calling example
        new_img = Rotate_180_Part_Rectangle(thatcher_face, 130, 240, 257, 263)
    """
    # Image copy
    w, h = img.size()
    new_img = Image(w, h)
    for x in range(w):
        for y in range(h):
            new_img.set(x, y, img.get(x, y))
    
    #----------------------------------------
    # Do something on here !
    for x in range(top_left_x, bottom_right_x):
        for y in range(top_left_y, bottom_right_y):
            new_img.set(bottom_right_x+top_left_x-x-1, bottom_right_y+top_left_y-y-1, img.get(x, y))
    
    #----------------------------------------
    
    return new_img


# Copy and Paste
def Copy_Add_Below_Part_Rectangle(img, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
    """
    Copy sub-part of Image class object and add it to below
    Parameters
        img: Image class object
        top_left_x: Top left point x value
        top_left_y: Top left point y value
        bottom_right_x: Bottom right point x value
        bottom_right_y: Bottom right point y value    
    Return value
        new Image class object
    Calling example
        new_img = Copy_Add_Below_Part_Rectangle(thatcher_face, 85, 166, 140, 190)
    """
    # Image copy
    w, h = img.size()
    new_img = Image(w, h)
    for x in range(w):
        for y in range(h):
            new_img.set(x, y, img.get(x, y))
    
    #----------------------------------------
    # Do something on here !
    for x in range(top_left_x, bottom_right_x):
        for y in range(top_left_y, bottom_right_y):
            new_img.set(x, y+bottom_right_y-top_left_y, img.get(x, y))
    
    #----------------------------------------
    
    return new_img


# Animation
def Animate_Face_Rotation(iter_count):
    """
    Rotate Face with iter_count times
    Parameters
        iter_count: the number of rotation counts
    Return value
        None
    Calling example
        Animate_Face_Rotation(6)
    """
    #----------------------------------------
    # Do something on here !
    # hint) Read the codes as below for handling face rotation
    for i in range(iter_count):
        Rotate_90_CW(thatcher_face)
        new_img = Rotate_90_CW(thatcher_face)
        thatcher_face.update_image(new_img)
        sleep(0.5)
    
    #----------------------------------------
        

"""
Homework Area Ends
You are not allowed to modify any code as below.
"""

# Handle user mouse input
event_number = 1
while True:
    if 1 == event_number:
        """
        1. Rotate Face
        """
        event = text_rotate_face1.wait()
        if 'mouse click' == event.getDescription() and 'green' == event._trigger.getFontColor().getColorName():
            # User click mouse to '1. Rotate Face'
            event._trigger.setFontColor('red')
            new_img = Rotate_180(thatcher_face)
            thatcher_face.update_image(new_img)
            event._trigger.setFontColor('blue')
            text_rotate_eye_mouth.setFontColor('green')
            event_number = 2
    elif 2 == event_number:
        """
        2. Rotate Eye and Mouth
        """        
        event = text_rotate_eye_mouth.wait()
        if 'mouse click' == event.getDescription() and 'green' == event._trigger.getFontColor().getColorName():
            # User click mouse to '2. Rotate Eye and Mouth'
            event._trigger.setFontColor('red')
            # Eye
            new_img = Rotate_180_Part_Rectangle(thatcher_face, 130, 240, 257, 263)
            thatcher_face.update_image(new_img)
            # Mouth
            new_img = Rotate_180_Part_Rectangle(thatcher_face, 153, 150, 232, 184)
            thatcher_face.update_image(new_img)
            event._trigger.setFontColor('blue')
            text_rotate_face2.setFontColor('green')
            event_number = 3
    elif 3 == event_number:
        """
        3. Rotate Face
        """
        event = text_rotate_face2.wait()
        if 'mouse click' == event.getDescription() and 'green' == event._trigger.getFontColor().getColorName():
            # User click mouse to '3. Rotate Face'
            event._trigger.setFontColor('red')
            new_img = Rotate_180(thatcher_face)
            thatcher_face.update_image(new_img)
            event._trigger.setFontColor('blue')
            text_rotate_face3.setFontColor('green')
            event_number = 4
    elif 4 == event_number:
        """
        4. Rotate Face Start
        """
        event = text_rotate_face3.wait()
        if 'mouse click' == event.getDescription() and 'green' == event._trigger.getFontColor().getColorName():
            # User click mouse to '3. Rotate Face'
            text_rotate_face3.setFontColor('red')
            Animate_Face_Rotation(6)
            text_rotate_face3.setFontColor('blue')
            text_add_eye_mouth.setFontColor('green')
            event_number = 5
    elif 5 == event_number:
        """
        - Add Eyes & Mouth
        """
        event = text_add_eye_mouth.wait()
        if 'mouse click' == event.getDescription() and 'green' == event._trigger.getFontColor().getColorName():
            thatcher_face.load('./Thatcher.png')
            sleep(0.5)
            event._trigger.setFontColor('red')
            # Left Eye
            new_img = Copy_Add_Below_Part_Rectangle(thatcher_face, 85, 166, 140, 190)
            thatcher_face.update_image(new_img)
            # Right Eye
            new_img = Copy_Add_Below_Part_Rectangle(thatcher_face, 169, 161, 218, 187)
            thatcher_face.update_image(new_img)
            # Mouth
            new_img = Copy_Add_Below_Part_Rectangle(thatcher_face, 118, 248, 193, 277)
            thatcher_face.update_image(new_img)
            event._trigger.setFontColor('blue')
            event_number = 6
    else:
        """
        End Program
        """
        break
    