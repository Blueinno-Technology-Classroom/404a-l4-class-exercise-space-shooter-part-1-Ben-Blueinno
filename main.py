import pgzrun
import random
from pgzhelper import *

WIDTH = 1024
HEIGHT = 768

player = Actor("playership2_blue")
player.pos = (WIDTH/2, HEIGHT/2)
player.hp = 100

enemies = []
lasers = []
elasers = []

def update():
    if player.hp >0:
        if random.randint(0,100)<5:
            enemy = Actor('enemygreen5')
            enemy.x = random.randint(0, WIDTH)
            enemy.point_towards(player)
            enemies.append(enemy)
               
        for e in enemies:
            e.move_forward(2)
            if e.left>WIDTH or e.right<0 or e.top>HEIGHT:
                enemies.remove(e)
                continue
            if player.colliderect(e):
                player.hp-=5
                enemies.remove(e)
                continue
            if random.randint(0,100)<2:
                elaser = Actor('laserred07')
                elaser.pos = e.pos
                elaser.point_towards(player)
                elasers.append(elaser)
            
        if keyboard.space:
            ...
            laser = Actor('laserblue01')
            laser.pos = player.pos
            if enemies:
                laser.point_towards(random.choice(enemies))
            else:
                laser.angle = 90
            lasers.append(laser)
        
        if keyboard.up:
            player.y -=5
        if keyboard.down:
            player.y +=5
        if keyboard.left:
            player.x -=5
        if keyboard.right:
            player.x +=5
        
        if player.left <= 0:
            player.left = 0
        if player.right >= WIDTH:
            player.right = WIDTH
        if player.top <= 0:
            player.top = 0
        if player.bottom >= HEIGHT:
            player.bottom = HEIGHT
            
        for l in lasers:
            l.move_forward(5)
            if l.bottom < 0:
                lasers.remove(l)
                continue
            for e in enemies:
                if l.colliderect(e):
                    lasers.remove(l)
                    enemies.remove(e)
                    break
        
        for el in elasers:
            el.move_forward(5)
            if el.top > HEIGHT:
                elasers.remove(el)
                continue
            if player.colliderect(el):
                player.hp -=1
                elasers.remove(el)
                break
    else:
        player.hp = 100
    

def draw():
    screen.clear()
    screen.draw.filled_rect(Rect((0,0), (WIDTH*player.hp/100, 20)),'green')
    for l in lasers:
        l.draw()
        
    for el in elasers:
        el.draw()
    
    player.draw()
    
    for e in enemies:
        e.draw()

pgzrun.go()