import pygame
import sys
from pygame.locals import *
import random
import threading
import time
MOVE_SPEED = 5

class Weltraum(object):
  size = [1000, 700]
  
  def __init__(self):
    self.fenster = pygame.display.set_mode(self.size)
    m1 = 'metgross.gif'               #2    
    m2 = 'metklein.gif'
    self.image = pygame.transform.scale(pygame.image.load('explosion.gif'), (50,50))
    self.meteorliste=[]
    self.schiff = Schiff()
    self.punkte=0
    self.verloren=False

  def generateMeteor(self,x,y,a,b):
    return Meteor(x,y,a,b)

  def schiessen(self, direction, x, y):
    return Schuss(x,y, direction)

  def generatehindernis(self):
    return Hindernis()

  def punktezaehler(self):
    self.punkte+=1

class Meteor(pygame.sprite.Sprite):
  def __init__(self, x, y,a,b ):
    super(Meteor, self).__init__()
    self.image = pygame.transform.scale(pygame.image.load("metgross.gif"), (x, y))
    #self.rect = pygame.Rect(a, b, 64, 71)
    self.rect = self.image.get_rect()
    self.speed = random.randint(1, 10)
    self.directionx = random.choice(["right", "left"])
    self.directiony = random.choice(["down", "up"])
  def update(self):
    if self.directionx == "right":
      if self.rect.x >= 1000:
        self.directionx = "left"
      else:
        self.rect.x = self.rect.x + self.speed
    elif self.directionx == "left":
      if self.rect.x <= 0:
        self.directionx = "right"
      else:
        self.rect.x = self.rect.x - self.speed
    if self.directiony == "down":
      if self.rect.y >= 700:
        self.directiony = "up"
      else:
        self.rect.y = self.rect.y + self.speed
    elif self.directiony == "up":
      if self.rect.y <= 0:
        self.directiony = "down"
      else:
        self.rect.y = self.rect.y - self.speed
##  def move(self):
##    if self.directionx == "right":
##      if self.rect.x >= 1000:
##        self.directionx = "left"
##      else:
##        self.rect.x = self.rect.x + self.speed
##    elif self.directionx == "left":
##      if self.rect.x <= 0:
##        self.directionx = "right"
##      else:
##        self.rect.x = self.rect.x - self.speed
##    if self.directiony == "down":
##      if self.rect.y >= 700:
##        self.directiony = "up"
##      else:
##        self.rect.y = self.rect.y + self.speed
##    elif self.directiony == "up":
##      if self.rect.y <= 0:
##        self.directiony = "down"
##      else:
##        self.rect.y = self.rect.y - self.speed
    
class Schiff(pygame.sprite.Sprite):
  def __init__(self):
    super(Schiff, self).__init__()
    self.image = pygame.image.load("rechts.gif")
    self.rect = self.image.get_rect()
    self.rect.y = 300
    self.speed=1
    self.direction="right"

  def update(self, direction):

    if self.rect.x>1000:
      self.rect.x=0
    if self.rect.y>700:
      self.rect.y=0
    if self.rect.x<0:
      self.rect.x=1000
    if self.rect.y<0:
      self.rect.y=700
    if direction == "left":
      self.rect.x = self.rect.x - self.speed
    if direction == "right":      
      self.rect.x = self.rect.x + self.speed
    if direction == "up":
      self.rect.y = self.rect.y + self.speed
    if direction == "down":
      self.rect.y = self.rect.y - self.speed
    #print self.rect.x, self.rect.y    

  def move(self, direction):
    self.direction=direction
    if self.rect.x>1000:
      self.rect.x=0
    if self.rect.y>700:
      self.rect.y=0
    if self.rect.x<0:
      self.rect.x=1000
    if self.rect.y<0:
      self.rect.y=700
    if direction == "left":
      self.rect.x = self.rect.x - self.speed
    if direction == "right":      
      self.rect.x = self.rect.x + self.speed
    if direction == "up":
      self.rect.y = self.rect.y + self.speed
    if direction == "down":
      self.rect.y = self.rect.y - self.speed
    #print self.rect.x, self.rect.y

class Schuss(pygame.sprite.Sprite):
  def __init__(self,x , y, direction):
    super(Schuss, self).__init__()
    self.schiff=Schiff()
    self.image = pygame.transform.scale(pygame.image.load("schuss.gif"), (20, 20))
    self.rect = pygame.Rect(x, y, 10, 10)
    self.rect.x=x
    self.rect.y=y-20
    self.richtung=direction
    self.speed=50
    
  def update(self):
    
    if self.richtung == "left":

      self.rect.x = self.rect.x - self.speed
    if self.richtung == "right":
      
      self.rect.x = self.rect.x + self.speed
    if self.richtung == "up":
      
      self.rect.y = self.rect.y - self.speed
    if self.richtung == "down":
      
      self.rect.y = self.rect.y + self.speed

class Hindernis(pygame.sprite.Sprite):
  def __init__(self):
    super(Hindernis, self).__init__()
    self.image = pygame.transform.scale(pygame.image.load("planet.gif"), (60, 60))
    self.rect = pygame.Rect(random.randint(0, 1000), random.randint(0, 700), 60, 60)
  
  
pygame.init()
clock = pygame.time.Clock()
w = Weltraum()
allmeteors = pygame.sprite.Group()  # Group objekt wird erstellt von meteors, schiff, all shoots, hindernisse ABER HIER NUR ERSTELLEN DER GRUPPE! UNTEN WIRD ZUGEFÜGT
allschiff = pygame.sprite.Group()
allshoots = pygame.sprite.Group()
allhindernis = pygame.sprite.Group()
allschiff.add(w.schiff)

for i in range(0,5):
  allhindernis.add(w.generatehindernis())
for i in range(0,7):
  w.meteorliste.append(w.generateMeteor(60,60,random.randint(500, 1000), random.randint(300, 700)))
  allmeteors.add(w.meteorliste[-1])

  
while True:
  w.fenster.fill((0,250,0))
  
  pygame.time.delay(100)
  
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()       
  
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_RIGHT]:
    #w.schiff.update("right")
    w.schiff.speed+=2

  if keys[pygame.K_LEFT]:
    w.schiff.update("left")
    w.schiff.speed-=2

  if keys[pygame.K_DOWN]:
    w.schiff.update("up")
  if keys[pygame.K_UP]:
    w.schiff.update("down")

  if keys[pygame.K_w]:   
    allshoots.add(w.schiessen("up",w.schiff.rect.x+50,w.schiff.rect.y+50))
  if keys[pygame.K_a]:
    allshoots.add(w.schiessen("left",w.schiff.rect.x,w.schiff.rect.y))
  if keys[pygame.K_s]:
    allshoots.add(w.schiessen("down",w.schiff.rect.x,w.schiff.rect.y))
  if keys[pygame.K_d]:
    allshoots.add(w.schiessen("right",w.schiff.rect.x+100,w.schiff.rect.y+100))               

  
  #allmeteors.clear(w.fenster, w.meteor1.image)
  allmeteors.update()
##  for meteor in allmeteors:
##    meteor.move()
  w.schiff.move("right")
##  if pygame.sprite.spritecollide(w.schiff, allhindernis, False):
##    w.verloren=True
##    #allschiff.clear(w.fenster, w.image)
##    allschiff.empty()
    
##    print("Boom")

  if pygame.sprite.spritecollide(w.schiff, allmeteors, False):   #Ein Schiff objekt  allmeteors ist gruppenobjekt  True beinerkollision gelöscht
    print("Collide")                                              # Erster Parameter bei collide ist objekt und zweiter ist gruppe! sprite und gruppe von sprite! nicht 2 gruppen
  
  
                  
  for schuss in allshoots:
    #schuss.update()
    if pygame.sprite.spritecollide(schuss, allmeteors, True):
      w.punktezaehler()
      for i in range(0,4):
        allmeteors.add(w.generateMeteor(30,30, 500, 350))
      print("Treffer", w.punkte)

  allshoots.update()
  allshoots.draw(w.fenster)
  allmeteors.update()
  allmeteors.draw(w.fenster)
  allschiff.update(w.schiff.direction)
  allschiff.draw(w.fenster)
  allhindernis.update()
  allhindernis.draw(w.fenster)
 
  pygame.display.flip()

