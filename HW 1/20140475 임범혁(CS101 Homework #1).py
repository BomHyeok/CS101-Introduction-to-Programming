from cs1robots import *
from random import *

create_world()

hubo = Robot(beepers = 1000)
ami = Robot('yellow')

def turn_right_h():
 for i in range(3):
  hubo.turn_left()

def look_back_h():
 for i in range(2):
  hubo.turn_left()
  
def turn_right_a():
 for i in range(3):
  ami.turn_left()

def look_back_a():
 for i in range(2):
  ami.turn_left()

def stepback_and_restore():
 if hubo.on_beeper():
  look_back_h()
  hubo.move()
  while hubo.on_beeper():
   hubo.turn_left()
   hubo.pick_beeper()
   
def move_one_step_or_stay():
 a=randint(1,3)
 for i in range(a):
  hubo.drop_beeper()
 for i in range(6-a):
  hubo.turn_left()
 if hubo.front_is_clear():
  hubo.move()
  stepback_and_restore()
 else :
  for i in range(a):
   hubo.pick_beeper()
  for i in range(2+a):
   hubo.turn_left()  
 
def can_move():
 if hubo.front_is_clear():
  hubo.move()
  if not hubo.on_beeper():
   look_back_h()
   hubo.move()
   look_back_h()
   return True
  else:
   look_back_h()
   hubo.move()
   look_back_h()
 if hubo.right_is_clear():
  turn_right_h()
  hubo.move()
  if not hubo.on_beeper():
   look_back_h()
   hubo.move()
   look_back_h()
   hubo.turn_left()
   return True
  else:
   look_back_h()
   hubo.move()
   look_back_h()
   hubo.turn_left()
 if hubo.left_is_clear():
  hubo.turn_left()
  hubo.move()
  if not hubo.on_beeper():
   look_back_h()
   hubo.move()
   look_back_h()
   turn_right_h()
   return True
  else:
   look_back_h()
   hubo.move()
   look_back_h()
   turn_right_h()
 else:
  return False

def follow_trace():
 while ami.on_beeper():
  look_back_a()
  while ami.on_beeper():
   turn_right_a()
   ami.pick_beeper()
  ami.move()

while can_move():
 move_one_step_or_stay()
follow_trace()