
import pygame, simpleGE, random

"ant picnic"
"slide and catch game"
"Sabrina mahoney"

class Cookie(simpleGE.Sprite):
    def__init__(self,scene):
        super().__init__(scene)
        self.setImage("Cookie.png")
        self.setSize(25,25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        #move to top of screen
        self.y = 10
        
        #x is random 0 - screen width
        self.x = random.randint(0, self.screenWidth)
        
        #dy is random minSpeed to maxSpeed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class Ant(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ant.png")
        self.setSize(50,50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.y += self.moveSpeed
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("blanket.png")
        
        self.sndCookie = simpleGE.Sound("apple_bite.wav")
        self.numCookies = 10
        self.ant = Ant(self)
        
        self.cookies = []
        for i in range(self.numCookies):
            self.cookies.append(Cookie(self))
        
        self.sprites = [self.ant,
                        self.cookie]
        
    def process(self):
        for cookie in self.cookies:
        if cookie.collidesWith(self.cookie):
            cookie.reset()
            self.sndCookie.play()
        
def main():
    game = Game()
    game.start()
    
if __name__=="__main__":
    main()