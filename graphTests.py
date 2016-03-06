import pygame, sys, math, random, time
from pygame.locals import*

pygame.init()
FPS = 25
fpsClock = pygame.time.Clock()
#set up window
windowX = 1080
windowY = 720
DISPLAYSURF = pygame.display.set_mode((windowX,windowY))
pygame.display.set_caption('graphs')
font = pygame.font.SysFont('consolas',20)
#set up colors

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
points = []
formula = ['']
def graphs(mode = 0):
     for angle in range(0,1000,1):
          x,y = 0,0
          if mode == 0:
               x = int(windowX/2 + math.radians(angle)*math.cos(math.radians(angle)))
               y = int(windowY/2 - math.radians(angle)*math.sin(math.radians(angle)))
          if mode == 1:
               x = int(windowX/2 + math.radians(math.sqrt(angle*50000))*math.cos(math.radians(angle)))
               y = int(windowY/2 - math.radians(math.sqrt(angle*50000))*math.sin(math.radians(angle)))
          if mode == 2:
               x = int(windowX/2 + math.radians(angle*angle/500)*math.cos(math.radians(angle)))
               y = int(windowY/2 - math.radians(angle*angle/500)*math.sin(math.radians(angle)))
          if mode == 3:
               x = int(windowX/2 + 400*math.cos(math.radians(angle))*math.cos(math.radians(angle)))
               y = int(windowY/2 - 400*math.cos(math.radians(angle))*math.sin(math.radians(angle)))
          if mode == 4: # flower
               petals = 6 #even nmbers produce double
               x = int(windowX/2 + 2+200*math.cos(math.radians(angle*petals))*math.cos(math.radians(angle)))
               y = int(windowY/2 - 2+200*math.cos(math.radians(angle*petals))*math.sin(math.radians(angle)))
          if mode == 5: # heart
               multiplier = 10
               x = int(windowX/2 + multiplier* 16*(math.sin(math.radians(angle))**3 ))
               y = int(windowY/2 + multiplier* -13*(math.cos(math.radians(angle))) -\
                                   multiplier* -5*(math.cos(math.radians(2*angle))) -\
                                   multiplier* -2*(math.cos(math.radians(3*angle))) -\
                                   multiplier* -1*(math.cos(math.radians(4*angle))))
          if mode == 6:
               x = int(windowX/2 + 300*math.sin(math.radians(angle/20))*math.cos(math.radians(angle)))
               y = int(windowY/2 - 300*math.sin(math.radians(angle/20))*math.sin(math.radians(angle)))
          if mode == 7:
               multiplier = 300
               x = int(windowX/2 + (100 - multiplier*math.sin(math.radians(2*angle))*math.cos(math.radians(1*angle)))  *math.cos(math.radians(angle)))
               y = int(windowY/2 - (100 - multiplier*math.sin(math.radians(2*angle))*math.cos(math.radians(1*angle)))  *math.sin(math.radians(angle)))
          

          points.append([x,y])

def dynaGraph(a, mul,cosang, cosdiv, sinang, sindiv):
     for angle in range(0,5000,5):
          multiplier = 300
          
          sdiv = sindiv
          if sdiv == 0: sdiv = 1
          cdiv = cosdiv
          if cdiv == 0: cdiv = 1
          
          x = int(windowX/2 + (a - mul*math.sin(math.radians(sinang*angle/sdiv))*math.cos(math.radians(cosang*angle/cdiv)))  *math.cos(math.radians(angle)))
          y = int(windowY/2 - (a - mul*math.sin(math.radians(sinang*angle/sdiv))*math.cos(math.radians(cosang*angle/cdiv)))  *math.sin(math.radians(angle)))
          formula[0] = 'r = '+str(a)+' - ' +str(mul)+'cos('+str(cosang)+'t/'+str(cdiv)+')sin('+str(sinang)+'t/'+str(sdiv)+') [z:help]'
          points.append([x,y])
def drawPoints():
     if len(points) > 2:
          for point in points:
               color = [random.randint(50,200) for i in range(3)]
               pygame.draw.lines(DISPLAYSURF,color,False,points,2)

#graphs(2)
dyna = [50,50,2,2,2,2]
dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])
angle = 0
while True: ##main game loop
     keys = pygame.key.get_pressed()
##     if angle < 10000: angle+=20
##     else:
##          angle = 0
##          points = []
     
     #get mouse position
     #mposX, mposY = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
     
##     x = int(windowX/2 + 300*math.sin(math.radians(angle/20))*math.cos(math.radians(angle)))
##     y = int(windowY/2 - 300*math.sin(math.radians(angle/20))*math.sin(math.radians(angle)))
##     points.append([x,y])
     #time.sleep(0.2)
          
     DISPLAYSURF.fill(BLACK)
     if keys[pygame.K_z]:
          helps = 'press and hold A,S,D,F,G,H and MOUSEWHEEL to change numbers :)' 
          DISPLAYSURF.blit(font.render(helps,1,(150,150,150)),(0,20))
     drawPoints()
     DISPLAYSURF.blit(font.render(formula[0],1,WHITE),(0,0))
     for event in pygame.event.get():
          if event.type == MOUSEBUTTONDOWN:
               if event.button == 4:
                    if keys[pygame.K_a]:
                         points = []
                         dyna[0] += 10
                         dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])

                    if keys[pygame.K_s]:
                         points = []
                         dyna[1] += 10
                         dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])

                    if keys[pygame.K_d]:
                         points = []
                         dyna[2] += 1
                         dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])

                    if keys[pygame.K_f]:
                         points = []
                         dyna[3] += 1
                         dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])
                    if keys[pygame.K_g]:
                         points = []
                         dyna[4] += 1
                         dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])
                    if keys[pygame.K_h]:
                         points = []
                         dyna[5] += 1
                         dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])                         

               if event.button == 5:
                    if keys[pygame.K_a]:
                         points = []
                         dyna[0] -= 10
                         dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])

                    if keys[pygame.K_s]:
                         points = []
                         dyna[1] -= 10
                         dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])

                    if keys[pygame.K_d]:
                         points = []
                         dyna[2] -= 1
                         dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])

                    if keys[pygame.K_f]:
                         points = []
                         dyna[3] -= 1
                         dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])
                    if keys[pygame.K_g]:
                         points = []
                         dyna[4] -= 1
                         dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])
                    if keys[pygame.K_h]:
                         points = []
                         dyna[5] -= 1
                         dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])
          if event.type == KEYDOWN and event.key == K_c:
               dyna[0] = 50
               dyna[1] = 50
               dyna[2] = 1
               dyna[3] = 1
               dyna[4] = 1
               dyna[5] = 1
               points = []
               dynaGraph(dyna[0],dyna[1],dyna[2], dyna[3],dyna[4], dyna[5])

          if event.type == QUIT:
               pygame.quit()
               sys.exit()
     pygame.display.update()
     fpsClock.tick(FPS)
