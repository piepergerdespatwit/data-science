import pygame

class Ball:
    #pass
    radius = 10

    def __init__(self, x,y, xv,yv, screen, wColor, bgColor):
        self.x = x
        self.y = y
        self.screen = screen
        self.wColor = wColor
        self.xv = xv
        self.yv = yv
        self.bgColor = bgColor

    
    def show(self, bColor):
        pygame.draw.circle(self.screen, bColor, (self.x,self.y), self.radius)

    def update(self):
        self.show(self.bgColor)
        self.x = self.x + self.xv
        self.y = self.y + self.yv

        if (self.x <= 25 + Ball.radius):
            self.xv = -self.xv
            self.x = self.x + self.xv            
        elif (self.y <= 25 + self.radius or self.y >= 475 - self.radius):
            self.yv = -self.yv
            self.y = self.y + self.yv
        self.show(self.wColor)

