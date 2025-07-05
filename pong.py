#make pong then implement AI 
import pygame as pg
pg.init() #initialized pygame

WIDTH, HEIGHT =  700, 500
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("AI Plays Pong")

#main loop of program
def main():
    run = True

    #loop constantly running handelling everything - collisions, ball movement
    while run:
        for event in pg.event.get(): #this loops through all the events that have occured such as clicking mouse keyboard and what not
            if event.type == pg.QUIT:
                run = False
                break
        
    pg.quit()

if __name__ == '__main__': #look this up later. Only running main if u run this python file and not when you import this 
    main()