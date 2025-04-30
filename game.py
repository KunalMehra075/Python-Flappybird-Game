import pygame as pg 
import sys,time
from bird import Bird


pg.init()


class Game:
    def __init__(self):
        # setting the window configurations
        self.width = 600 
        self.height = 768 
        self.scale_factor = 1.5
        self.win = pg.display.set_mode((self.width,self.height))
        self.clock = pg.time.Clock()
        self.move_speed = 200
        
        self.bird =Bird(self.scale_factor)
        
        self.is_enter_pressed = False
        self.setupBgAndGround()
        self.gameLoop()
    
    def gameLoop(self):
        last_time = time.time()
        while True:
            # Calculating Delta Time
            new_time = time.time()
            dt = new_time - last_time 
            last_time = new_time
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    break
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.is_enter_pressed = True
                    elif event.key == pg.K_SPACE and self.is_enter_pressed:
                        self.bird.flap(dt)
            self.updateEverything(dt)
            self.drawEverything()
            pg.display.update()
            self.clock.tick(60)

    def updateEverything(self,dt):
        if self.is_enter_pressed:
            self.ground1_rect.x -= int(self.move_speed*dt)
            self.ground2_rect.x -= int(self.move_speed*dt)

            if self.ground1_rect.right<=0:
                self.ground1_rect.x = self.ground2_rect.right
            if self.ground2_rect.right<=0:
                self.ground2_rect.x = self.ground1_rect.right 

            self.bird.update(dt)
    
        
        
    def drawEverything(self):
      # blit method is used for showing something on screen buffer
        self.win.blit(self.bg_img,(0,-280))
        self.win.blit(self.ground1_img,self.ground1_rect)
        self.win.blit(self.ground2_img,self.ground2_rect)
        self.win.blit(self.bird.image,self.bird.rect)
    
    def setupBgAndGround(self):
        # Loading the basic background images
        self.bg_img = pg.transform.scale_by(pg.image.load("assets/bg.png").convert(),self.scale_factor) 
        self.ground1_img = pg.transform.scale_by(pg.image.load("assets/ground.png").convert(),self.scale_factor) 
        self.ground2_img = pg.transform.scale_by(pg.image.load("assets/ground.png").convert(),self.scale_factor) 
        
        self.ground1_rect = self.ground1_img.get_rect()
        self.ground2_rect = self.ground2_img.get_rect()
        
        self.ground1_rect.x = 0
        self.ground1_rect.y = 568
        self.ground2_rect.y = 568
        self.ground2_rect.x = self.ground1_rect.right
        

             
flappy = Game()