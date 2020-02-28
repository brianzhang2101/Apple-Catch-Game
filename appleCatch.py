from tkinter import *
import tkinter as tk
import time
import random
from os import startfile
class fruit(object):
     
     def close(self, event):
          self.root.destroy()
          print("You Have Successfully Closed the Game!")
          
     def __init__(self):
          #Coordinates of Apples and Rotten Apples and Basket
          apple_x = random.randint(20, 480)
          apple_y = random.randint(-80, 0)
          rottenapple_x = random.randint(20, 480)
          rottenapple_y = random.randint(-240, -160)
          
          apple_x2 = random.randint(20, 480)
          apple_y2 = random.randint(-400, -320)
          rottenapple_x2 = random.randint(20, 480)
          rottenapple_y2 = random.randint(-540, -480)

          apple_x3 = random.randint(20, 480)
          apple_y3 = random.randint(-720, -640)
          rottenapple_x3 = random.randint(20, 480)
          rottenapple_y3 = random.randint(-880, -800)

          apple_x4 = random.randint(20, 480)
          apple_y4 = random.randint(-1040, -960)
          rottenapple_x4 = random.randint(20, 480)
          rottenapple_y4 = random.randint(-1200, -1120)

          apple_x5 = random.randint(20, 480)
          apple_y5 = random.randint(-1360, -1280)
          rottenapple_x5 = random.randint(20, 480)
          rottenapple_y5 = random.randint(-1520, -1440)

          apple_x6 = random.randint(20, 480)
          apple_y6 = random.randint(-1680, -1600)
          rottenapple_x6 = random.randint(20, 480)
          rottenapple_y6 = random.randint(-1840, -1760)

          apple_x7 = random.randint(20, 480)
          apple_y7 = random.randint(-2000, -1920)
          rottenapple_x7 = random.randint(20, 480)
          rottenapple_y7 = random.randint(-2160, -2080)

          apple_x8 = random.randint(20, 480)
          apple_y8 = random.randint(-2320, -2240)
          rottenapple_x8 = random.randint(20, 480)
          rottenapple_y8 = random.randint(-2480, -2400)

          apple_x9 = random.randint(20, 480)
          apple_y9 = random.randint(-2640, -2560)
          rottenapple_x9 = random.randint(20, 480)
          rottenapple_y9 = random.randint(-2800, -2720)

          apple_x10 = random.randint(20, 480)
          apple_y10 = random.randint(-2960, -2880)
          rottenapple_x10 = random.randint(20, 480)
          rottenapple_y10 = random.randint(-3120, -3040)
          
          self.root = Tk()
          self.root.title("Apple Catch!")
          self.root.resizable(0,0)
          self.canvas = Canvas(self.root, width = 500, height = 500)
          self.canvas.pack()
          menubar = Menu(self.root)
          menubar.add_command(label="Instructions", command=self.hello)
          self.root.config(menu=menubar)
          #Create Apples, Rotten Apples and Basket
          self.apple = self.canvas.create_oval(apple_x, apple_y, apple_x + 20, apple_y +20, outline="white", fill="red")
          self.rottenapple = self.canvas.create_oval(rottenapple_x, rottenapple_y , rottenapple_x +20, rottenapple_y +20, outline ="white", fill="blue")

          self.apple2 = self.canvas.create_oval(apple_x2, apple_y2, apple_x2 + 20, apple_y2 +20, outline="white", fill="red")
          self.rottenapple2 = self.canvas.create_oval(rottenapple_x2, rottenapple_y2 , rottenapple_x2 +20, rottenapple_y2 +20, outline ="white", fill="blue")
          
          self.apple3 = self.canvas.create_oval(apple_x3, apple_y3, apple_x3 + 20, apple_y3 +20, outline="white", fill="red")
          self.rottenapple3 = self.canvas.create_oval(rottenapple_x3, rottenapple_y3 , rottenapple_x3 +20, rottenapple_y3 +20, outline ="white", fill="blue")

          self.apple4 = self.canvas.create_oval(apple_x4, apple_y4, apple_x4 + 20, apple_y4 +20, outline="white", fill="red")
          self.rottenapple4 = self.canvas.create_oval(rottenapple_x4, rottenapple_y4 , rottenapple_x4 +20, rottenapple_y4 +20, outline ="white", fill="blue")

          self.apple5 = self.canvas.create_oval(apple_x5, apple_y5, apple_x5 + 20, apple_y5 +20, outline="white", fill="red")
          self.rottenapple5 = self.canvas.create_oval(rottenapple_x5, rottenapple_y5 , rottenapple_x5 +20, rottenapple_y5 +20, outline ="white", fill="blue")

          self.apple6 = self.canvas.create_oval(apple_x6, apple_y6, apple_x6 + 20, apple_y6 +20, outline="white", fill="red")
          self.rottenapple6 = self.canvas.create_oval(rottenapple_x6, rottenapple_y6 , rottenapple_x6 +20, rottenapple_y6 +20, outline ="white", fill="blue")

          self.apple7 = self.canvas.create_oval(apple_x7, apple_y7, apple_x7 + 20, apple_y7 +20, outline="white", fill="red")
          self.rottenapple7 = self.canvas.create_oval(rottenapple_x7, rottenapple_y7 , rottenapple_x7 +20, rottenapple_y7 +20, outline ="white", fill="blue")

          self.apple8 = self.canvas.create_oval(apple_x8, apple_y8, apple_x8 + 20, apple_y8 +20, outline="white", fill="red")
          self.rottenapple8 = self.canvas.create_oval(rottenapple_x8, rottenapple_y8 , rottenapple_x8 +20, rottenapple_y8 +20, outline ="white", fill="blue")

          self.apple9 = self.canvas.create_oval(apple_x9, apple_y9, apple_x9 + 20, apple_y9 +20, outline="white", fill="red")
          self.rottenapple9 = self.canvas.create_oval(rottenapple_x9, rottenapple_y9 , rottenapple_x9 +20, rottenapple_y9 +20, outline ="white", fill="blue")

          self.apple10 = self.canvas.create_oval(apple_x10, apple_y10, apple_x10 + 20, apple_y10 +20, outline="white", fill="red")
          self.rottenapple10 = self.canvas.create_oval(rottenapple_x10, rottenapple_y10 , rottenapple_x10 +20, rottenapple_y10 +20, outline ="white", fill="blue")
          
          self.basket = self.canvas.create_rectangle(20, 460, 100, 470, fill = "Gray")
          
          self.root.after(0, self.animation)
          self.root.bind("<Escape>", self.close)
          self.root.mainloop()
   
     def right(self, event):
          x_vel = 15
          y_vel = 0
          self.canvas.move(self.basket, x_vel, y_vel)

     def left(self, event):
          x_vel = -15
          y_vel = 0
          self.canvas.move(self.basket, x_vel, y_vel)

     def hello(self):
          startfile("Instructions.txt")

     def animation(self):
          global applesCollected
          global Lives
          applesCollected = 0
          Lives = 5
          self.root.bind("<Right>", self.right)
          self.root.bind("<Left>", self.left)
          AppleText = self.canvas.create_text(295, 15, text="Apples: 0", font=("", 16))
          LifeText = self.canvas.create_text(180, 15, text="Lives: 5", font=("", 16))
          LifeCounter = self.canvas.create_text(220, 15, font=("", 16))
          AppleCounter = self.canvas.create_text(335, 15, font=("", 16))
          track=0
          onScreen = 1
          #Animate Apples
          while Lives > 0:
               y = 1.5
               if track == 0:
                    for i in range(0, 1):
                         time.sleep(0.0125)
                         self.canvas.move(self.apple, 0, y)
                         self.canvas.move(self.rottenapple, 0, y)
                         self.canvas.move(self.apple2, 0, y)
                         self.canvas.move(self.rottenapple2, 0, y)
                         self.canvas.move(self.apple3, 0, y)
                         self.canvas.move(self.rottenapple3, 0, y)
                         self.canvas.move(self.apple4, 0, y)
                         self.canvas.move(self.rottenapple4, 0, y)
                         self.canvas.move(self.apple5, 0, y)
                         self.canvas.move(self.rottenapple5, 0, y)
                         self.canvas.move(self.apple6, 0, y)
                         self.canvas.move(self.rottenapple6, 0, y)
                         self.canvas.move(self.apple7, 0, y)
                         self.canvas.move(self.rottenapple7, 0, y)
                         self.canvas.move(self.apple8, 0, y)
                         self.canvas.move(self.rottenapple8, 0, y)
                         self.canvas.move(self.apple9, 0, y)
                         self.canvas.move(self.rottenapple9, 0, y)
                         self.canvas.move(self.apple10, 0, y)
                         self.canvas.move(self.rottenapple10, 0, y)
                         self.canvas.update()
               #Coordinates of Apple
               position=[]
               positions = self.canvas.coords(self.apple)
               position.extend(positions)
               position.append(positions)
               #Coordinates of Apple2
               position2=[]
               positions2 = self.canvas.coords(self.apple2)
               position2.extend(positions2)
               position2.append(positions2)
               #Coordinates of Apple3
               position3=[]
               positions3 = self.canvas.coords(self.apple3)
               position3.extend(positions3)
               position3.append(positions3)
               #Coordinates of Apple4
               position4=[]
               positions4 = self.canvas.coords(self.apple4)
               position4.extend(positions4)
               position4.append(positions4)
               #Coordinates of Apple5
               position5=[]
               positions5 = self.canvas.coords(self.apple5)
               position5.extend(positions5)
               position5.append(positions5)
               #Coordinates of Apple6
               position6=[]
               positions6 = self.canvas.coords(self.apple6)
               position6.extend(positions6)
               position6.append(positions6)
               #Coordinates of Apple7
               position7=[]
               positions7 = self.canvas.coords(self.apple7)
               position7.extend(positions7)
               position7.append(positions7)
               #Coordinates of Apple8
               position8=[]
               positions8 = self.canvas.coords(self.apple8)
               position8.extend(positions8)
               position8.append(positions8)
               #Coordinates of Apple9
               position9=[]
               positions9 = self.canvas.coords(self.apple9)
               position9.extend(positions9)
               position9.append(positions9)
               #Coordinates of Apple10
               position10=[]
               positions10 = self.canvas.coords(self.apple10)
               position10.extend(positions10)
               position10.append(positions10)
               #Coordinates of Rotten Apple
               posRapple=[]
               posRapples = self.canvas.coords(self.rottenapple)
               posRapple.extend(posRapples)
               posRapple.append(posRapples)
               #Coordinates of Rotten Apple2
               posRapple2=[]
               posRapples2 = self.canvas.coords(self.rottenapple2)
               posRapple2.extend(posRapples2)
               posRapple2.append(posRapples2)
               #Coordinates of Rotten Apple3
               posRapple3=[]
               posRapples3 = self.canvas.coords(self.rottenapple3)
               posRapple3.extend(posRapples3)
               posRapple3.append(posRapples3)
               #Coordinates of Rotten Apple4
               posRapple4=[]
               posRapples4 = self.canvas.coords(self.rottenapple4)
               posRapple4.extend(posRapples4)
               posRapple4.append(posRapples4)
               #Coordinates of Rotten Apple5
               posRapple5=[]
               posRapples5 = self.canvas.coords(self.rottenapple5)
               posRapple5.extend(posRapples5)
               posRapple5.append(posRapples5)
               #Coordinates of Rotten Apple6
               posRapple6=[]
               posRapples6 = self.canvas.coords(self.rottenapple6)
               posRapple6.extend(posRapples6)
               posRapple6.append(posRapples6)
               #Coordinates of Rotten Apple7
               posRapple7=[]
               posRapples7 = self.canvas.coords(self.rottenapple7)
               posRapple7.extend(posRapples7)
               posRapple7.append(posRapples7)
               #Coordinates of Rotten Apple8
               posRapple8=[]
               posRapples8 = self.canvas.coords(self.rottenapple8)
               posRapple8.extend(posRapples8)
               posRapple8.append(posRapples8)
               #Coordinates of Rotten Apple9
               posRapple9=[]
               posRapples9 = self.canvas.coords(self.rottenapple9)
               posRapple9.extend(posRapples9)
               posRapple9.append(posRapples9)
               #Coordinates of Rotten Apple10
               posRapple10=[]
               posRapples10 = self.canvas.coords(self.rottenapple10)
               posRapple10.extend(posRapples10)
               posRapple10.append(posRapples10)
               #Coordinates of Basket
               posBasket = []
               posBaskets = self.canvas.coords(self.basket)
               posBasket.extend(posBaskets)
               posBasket.append(posBaskets)
               #distance of Apple to Basket
               try:
                    distance = (((posBaskets[0] + 40) -(positions[2] - 15))**2+(posBasket[1]-positions[3])**2)**0.5
               except IndexError:
                    distance = 100
                    pass
               #distance of Rotten Apple to Basket
               try:
                    distancerb = ((posBaskets[0] + 40 -(posRapples[2] -15))**2+(posBasket[1]-posRapples[3])**2)**0.5
               except IndexError:
                    distancerb = 100
                    pass
               #distance of Apple2 to Basket
               try:
                    distance2 = (((posBaskets[0] + 40) -(positions2[2] - 15))**2+(posBasket[1]-positions2[3])**2)**0.5

               except IndexError:
                    distance2 = 100
                    pass
               #distance of Apple3 to Basket
               try:
                    distance3 = (((posBaskets[0] + 40) -(positions3[2] - 15))**2+(posBasket[1]-positions3[3])**2)**0.5
               except IndexError:
                    distance3 = 100
                    pass
               #distance of Apple4 to Basket
               try:
                    distance4 = (((posBaskets[0] + 40) -(positions4[2] - 15))**2+(posBasket[1]-positions4[3])**2)**0.5
               except IndexError:
                    distance4 = 100
                    pass
               #distance of Apple5 to Basket
               try:
                    distance5 = (((posBaskets[0] + 40) -(positions5[2] - 15))**2+(posBasket[1]-positions5[3])**2)**0.5
               except IndexError:
                    distance5 = 100
                    pass
               #distance of Apple6 to Basket
               try:
                    distance6 = (((posBaskets[0] + 40) -(positions6[2] - 15))**2+(posBasket[1]-positions6[3])**2)**0.5
               except IndexError:
                    distance6 = 100
                    pass
               #distance of Apple7 to Basket
               try:
                    distance7 = (((posBaskets[0] + 40) -(positions7[2] - 15))**2+(posBasket[1]-positions7[3])**2)**0.5
               except IndexError:
                    distance7 = 100
                    pass
               #distance of Apple8 to Basket
               try:
                    distance8 = (((posBaskets[0] + 40) -(positions8[2] - 15))**2+(posBasket[1]-positions8[3])**2)**0.5
               except IndexError:
                    distance8 = 100
                    pass
               #distance of Apple9 to Basket
               try:
                    distance9 = (((posBaskets[0] + 40) -(positions9[2] - 15))**2+(posBasket[1]-positions9[3])**2)**0.5
               except IndexError:
                    distance9 = 100
                    pass
               #distance of Apple10 to Basket
               try:
                    distance10 = (((posBaskets[0] + 40) -(positions10[2] - 15))**2+(posBasket[1]-positions10[3])**2)**0.5
               except IndexError:
                    distance10 = 100
                    pass
               #distance of Rotten Apple2 to Basket
               try:
                    distancerb2 = ((posBaskets[0] + 40 -(posRapples2[2] -15))**2+(posBasket[1]-posRapples2[3])**2)**0.5
               except IndexError:
                    distancerb2 = 100
                    pass
               #distance of Rotten Apple3 to Basket
               try:
                    distancerb3 = ((posBaskets[0] + 40 -(posRapples3[2] -15))**2+(posBasket[1]-posRapples3[3])**2)**0.5
               except IndexError:
                    distancerb3 = 100
                    pass
               #distance of Rotten Apple4 to Basket
               try:
                    distancerb4 = ((posBaskets[0] + 40 -(posRapples4[2] -15))**2+(posBasket[1]-posRapples4[3])**2)**0.5
               except IndexError:
                    distancerb4 = 100
                    pass
               #distance of Rotten Apple5 to Basket
               try:
                    distancerb5 = ((posBaskets[0] + 40 -(posRapples5[2] -15))**2+(posBasket[1]-posRapples5[3])**2)**0.5
               except IndexError:
                    distancerb5 = 100
                    pass
               #distance of Rotten Apple6 to Basket
               try:
                    distancerb6 = ((posBaskets[0] + 40 -(posRapples6[2] -15))**2+(posBasket[1]-posRapples6[3])**2)**0.5
               except IndexError:
                    distancerb6 = 100
                    pass
               #distance of Rotten Apple7 to Basket
               try:
                    distancerb7 = ((posBaskets[0] + 40 -(posRapples7[2] -15))**2+(posBasket[1]-posRapples7[3])**2)**0.5
               except IndexError:
                    distancerb7 = 100
                    pass
               #distance of Rotten Apple8 to Basket
               try:
                    distancerb8 = ((posBaskets[0] + 40 -(posRapples8[2] -15))**2+(posBasket[1]-posRapples8[3])**2)**0.5
               except IndexError:
                    distancerb8 = 100
                    pass
               #distance of Rotten Apple9 to Basket
               try:
                    distancerb9 = ((posBaskets[0] + 40 -(posRapples9[2] -15))**2+(posBasket[1]-posRapples9[3])**2)**0.5
               except IndexError:
                    distancerb9 = 100
                    pass
               #distance of Rotten Apple10 to Basket
               try:
                    distancerb10 = ((posBaskets[0] + 40 -(posRapples10[2] -15))**2+(posBasket[1]-posRapples10[3])**2)**0.5
               except IndexError:
                    distancerb10 = 100
                    pass
               #if Apple and Basket touch
               try:
                    if distance < 35:
                         self.canvas.delete(self.apple)
                         applesCollected = applesCollected + 1
                         print("+1 Point")
                         print("Score:", applesCollected)
                         self.canvas.itemconfig(AppleCounter, text=applesCollected)
                         self.canvas.itemconfig(AppleText, text="Apples: ")
               except IndexError:
                    pass
               #if Apple2 and Basket touch
               try:
                    if distance2 < 35:
                         self.canvas.delete(self.apple2)
                         applesCollected = applesCollected + 1
                         print("+1 Point")
                         print("Score:", applesCollected)
                         self.canvas.itemconfig(AppleCounter, text=applesCollected)
                         self.canvas.itemconfig(AppleText, text="Apples: ")
               except IndexError:
                    pass
               #if Apple3 and Basket touch
               try:
                    if distance3 < 35:
                         self.canvas.delete(self.apple3)
                         applesCollected = applesCollected + 1
                         print("+1 Point")
                         print("Score:", applesCollected)
                         self.canvas.itemconfig(AppleCounter, text=applesCollected)
                         self.canvas.itemconfig(AppleText, text="Apples: ")
               except IndexError:
                    pass
               #if Apple4 and Basket touch
               try:
                    if distance4 < 35:
                         self.canvas.delete(self.apple4)
                         applesCollected = applesCollected + 1
                         print("+1 Point")
                         print("Score:", applesCollected)
                         self.canvas.itemconfig(AppleCounter, text=applesCollected)
                         self.canvas.itemconfig(AppleText, text="Apples: ")
               except IndexError:
                    pass
               #if Apple5 and Basket touch
               try:
                    if distance5 < 35:
                         self.canvas.delete(self.apple5)
                         applesCollected = applesCollected + 1
                         print("+1 Point")
                         print("Score:", applesCollected)
                         self.canvas.itemconfig(AppleCounter, text=applesCollected)
                         self.canvas.itemconfig(AppleText, text="Apples: ")
               except IndexError:
                    pass
               #if Apple6 and Basket touch
               try:
                    if distance6 < 35:
                         self.canvas.delete(self.apple6)
                         applesCollected = applesCollected + 1
                         print("+1 Point")
                         print("Score:", applesCollected)
                         self.canvas.itemconfig(AppleCounter, text=applesCollected)
                         self.canvas.itemconfig(AppleText, text="Apples: ")
               except IndexError:
                    pass
               #if Apple7 and Basket touch
               try:
                    if distance7 < 35:
                         self.canvas.delete(self.apple7)
                         applesCollected = applesCollected + 1
                         print("+1 Point")
                         print("Score:", applesCollected)
                         self.canvas.itemconfig(AppleCounter, text=applesCollected)
                         self.canvas.itemconfig(AppleText, text="Apples: ")
               except IndexError:
                    pass
               #if Apple8 and Basket touch
               try:
                    if distance8 < 35:
                         self.canvas.delete(self.apple8)
                         applesCollected = applesCollected + 1
                         print("+1 Point")
                         print("Score:", applesCollected)
                         self.canvas.itemconfig(AppleCounter, text=applesCollected)
                         self.canvas.itemconfig(AppleText, text="Apples: ")
               except IndexError:
                    pass
               #if Apple9 and Basket touch
               try:
                    if distance9 < 35:
                         self.canvas.delete(self.apple9)
                         applesCollected = applesCollected + 1
                         print("+1 Point")
                         print("Score:", applesCollected)
                         self.canvas.itemconfig(AppleCounter, text=applesCollected)
                         self.canvas.itemconfig(AppleText, text="Apples: ")
               except IndexError:
                    pass
               #if Apple10 and Basket touch
               try:
                    if distance10 < 35:
                         self.canvas.delete(self.apple10)
                         applesCollected = applesCollected + 1
                         print("+1 Point")
                         print("Score:", applesCollected)
                         self.canvas.itemconfig(AppleCounter, text=applesCollected)
                         self.canvas.itemconfig(AppleText, text="Apples: ")
                         if applesCollected == 10:
                              global reset
                              print("You Won!")
                              WinText = self.canvas.create_text(250, 200, text="Congratulations!", font=("", 16))
                              Start = self.canvas.create_text(250, 240, text="Great Work! You have acquired all 10 apples, not many people can ", font=("", 12))
                              Continued = self.canvas.create_text(250, 265, text="do what you just did there. Jack the farmer ", font=("", 12))
                              Again = self.canvas.create_text(250, 290, text=" who is impressed, decides to give you a job on the farm!", font=("", 12))
                              reset = Button(self.root, text="Go Again!", command = self.restart)
                              reset.place(x=225, y=322)
                              self.canvas.delete(self.rottenapple10)
                              break
               except IndexError:
                    pass
               #if Rotten Apple and Basket touch
               try:
                    if distancerb < 35:
                         self.canvas.delete(self.rottenapple)
                         Lives = Lives - 2
                         print ("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple2 and Basket touch
               try:
                    if distancerb2 < 35:
                         self.canvas.delete(self.rottenapple2)
                         Lives = Lives - 2
                         print ("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple3 and Basket touch
               try:
                    if distancerb3 < 35:
                         self.canvas.delete(self.rottenapple3)
                         Lives = Lives - 2
                         print ("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple4 and Basket touch
               try:
                    if distancerb4 < 35:
                         self.canvas.delete(self.rottenapple4)
                         Lives = Lives - 2
                         print ("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple5 and Basket touch
               try:
                    if distancerb5 < 35:
                         self.canvas.delete(self.rottenapple5)
                         Lives = Lives - 2
                         print ("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple6 and Basket touch
               try:
                    if distancerb6 < 35:
                         self.canvas.delete(self.rottenapple6)
                         Lives = Lives - 2
                         print ("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple7 and Basket touch
               try:
                    if distancerb7 < 35:
                         self.canvas.delete(self.rottenapple7)
                         Lives = Lives - 2
                         print ("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple8 and Basket touch
               try:
                    if distancerb8 < 35:
                         self.canvas.delete(self.rottenapple8)
                         Lives = Lives - 2
                         print ("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple9 and Basket touch
               try:
                    if distancerb9 < 35:
                         self.canvas.delete(self.rottenapple9)
                         Lives = Lives - 2
                         print ("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple10 and Basket touch
               try:
                    if distancerb10 < 35:
                         self.canvas.delete(self.rottenapple10)
                         Lives = Lives - 2
                         print ("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Apple goes off screen
               try:
                    if positions[3] > 470:
                         self.canvas.delete(self.apple)
                         Lives = Lives - 1
                         print("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple goes off screen
               try:
                    if posRapples[3] > 470:
                         self.canvas.delete(self.rottenapple)
                         print("Deleted")
               except IndexError:
                    pass
               #if Apple2 goes off screen
               try:
                    if positions2[3] > 470:
                         self.canvas.delete(self.apple2)
                         Lives = Lives - 1
                         print("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple2 goes off screen
               try:
                    if posRapples2[3] > 470:
                         self.canvas.delete(self.rottenapple2)
                         print("Deleted")
               except IndexError:
                    pass
               #if Apple3 goes off screen
               try:
                    if positions3[3] > 470:
                         self.canvas.delete(self.apple3)
                         Lives = Lives - 1
                         print("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple3 goes off screen
               try:
                    if posRapples3[3] > 470:
                         self.canvas.delete(self.rottenapple3)
                         print("Deleted")
               except IndexError:
                    pass
               #if Apple4 goes off screen
               try:
                    if positions4[3] > 470:
                         self.canvas.delete(self.apple4)
                         Lives = Lives - 1
                         print("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple4 goes off screen
               try:
                    if posRapples4[3] > 470:
                         self.canvas.delete(self.rottenapple4)
                         print("Deleted")
               except IndexError:
                    pass
               #if Apple5 goes off screen
               try:
                    if positions5[3] > 470:
                         self.canvas.delete(self.apple5)
                         Lives = Lives - 1
                         print("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple5 goes off screen
               try:
                    if posRapples5[3] > 470:
                         self.canvas.delete(self.rottenapple5)
                         print("Deleted")
               except IndexError:
                    pass
               #if Apple6 goes off screen
               try:
                    if positions6[3] > 470:
                         self.canvas.delete(self.apple6)
                         Lives = Lives - 1
                         print("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple6 goes off screen
               try:
                    if posRapples6[3] > 470:
                         self.canvas.delete(self.rottenapple6)
                         print("Deleted")
               except IndexError:
                    pass
               #if Apple7 goes off screen
               try:
                    if positions7[3] > 470:
                         self.canvas.delete(self.apple7)
                         Lives = Lives - 1
                         print("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple7 goes off screen
               try:
                    if posRapples7[3] > 470:
                         self.canvas.delete(self.rottenapple7)
                         print("Deleted")
               except IndexError:
                    pass
               #if Apple8 goes off screen
               try:
                    if positions8[3] > 470:
                         self.canvas.delete(self.apple8)
                         Lives = Lives - 1
                         print("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple8 goes off screen
               try:
                    if posRapples8[3] > 470:
                         self.canvas.delete(self.rottenapple8)
                         print("Deleted")
               except IndexError:
                    pass
               #if Apple9 goes off screen
               try:
                    if positions9[3] > 470:
                         self.canvas.delete(self.apple9)
                         Lives = Lives - 1
                         print("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple9 goes off screen
               try:
                    if posRapples9[3] > 470:
                         self.canvas.delete(self.rottenapple9)
                         print("Deleted")
               except IndexError:
                    pass
               #if Apple10 goes off screen
               try:
                    if positions10[3] > 470:
                         self.canvas.delete(self.apple10)
                         Lives = Lives - 1
                         print("Lives Remaining:", Lives)
                         self.canvas.itemconfig(LifeCounter, text=Lives)
                         self.canvas.itemconfig(LifeText, text="Lives: ")
               except IndexError:
                    pass
               #if Rotten Apple10 goes off screen
               try:
                    if posRapples10[3] > 470:
                         self.canvas.delete(self.rottenapple10)
                         print("Deleted")
                         if applesCollected >= 0 and applesCollected < 10:
                              print("Nice Try!")
                              Effort = self.canvas.create_text(250, 200, text="Good Effort!", font=("", 16))
                              reset = Button(self.root, text="Lets Go!", command = self.restart)
                              reset.place(x=225, y=322)
                              Start = self.canvas.create_text(250, 240, text="You're getting the hang of it! A few mistakes here and ", font=("", 12))
                              Continued = self.canvas.create_text(250, 265, text="there are totally normal! Keep trying and ", font=("", 12))
                              Again = self.canvas.create_text(250, 290, text="complete Jack's Challenge!", font=("", 12))
                              break

               except IndexError:
                    pass
          #if all Lives lost
          else:
               if Lives <= 0:
                    print("You Lost!")
                    print("Your Final Score Is:", applesCollected)
                    LoseText = self.canvas.create_text(250, 200, text="Oh No!", font=("", 16))
                    Start = self.canvas.create_text(250, 240, text="You seemed overwhelmed by the amount apples ", font=("", 12))
                    Continued = self.canvas.create_text(250, 265, text="falling from the sky that you stumbled and fell! Don't ",font=("", 12))
                    Again = self.canvas.create_text(250, 290, text="worry, getting good takes practice, better luck next time!",font=("", 12))
                    reset = Button(self.root, text="Try Again", command = self.restart)
                    reset.place(x=220, y=322)
                    
     def restart(self):
          print("Restart?")
          reset.destroy()
          self.root.destroy()
          fruit()

          

fruit()

