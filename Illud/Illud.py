import contextlib
with contextlib.redirect_stdout(None):
    import pygame as game
import random
game.init()


### IMPORTANT VARS

life = 3
numbers = [1,2,3,4,5,6,7,8,9,10]

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (50,50,50)
screenWidth = 1216
screenHeight = 640
win = game.display.set_mode((screenWidth, screenHeight))
game.display.set_caption("Illud")


### SOUND

game.init()
game.mixer.init()
#game.mixer.music.load('wacht.mp3')
#game.mixer.music.play(-1)

death = game.mixer.Sound('audio/death.wav')
pickupgem = game.mixer.Sound('audio/pickupgem.wav')
menu = game.mixer.Sound('audio/menu.wav')
###IMAGES
link = game.image.load ("images/link.icns")
link1 = game.image.load("images/link1.icns")
bar1 = game.image.load("images/bar1.icns")
link2 = game.image.load("images/link2.icns")
#rocks
gravel = game.image.load("images/gravel.icns")
rockruby = game.image.load("images/rockruby.icns")
rock = game.image.load("images/rock.icns")
rocktopaz = game.image.load("images/rocktopaz.icns")
rocksapphire = game.image.load("images/rocksapphire.icns")
rockemerald = game.image.load("images/rockemerald.icns")
emeraldempty = game.image.load("images/emeraldempty.icns")
rubyempty = game.image.load("images/rubyempty.icns")
sapphireempty = game.image.load("images/sapphireempty.icns")
topazempty = game.image.load("images/topazempty.icns")
#gems
ruby1 = game.image.load("images/ruby1.icns")
ruby2 = game.image.load("images/ruby2.icns")
topaz1 = game.image.load("images/topaz1.icns")
topaz2 = game.image.load("images/topaz2.icns")
sapphire1 = game.image.load("images/sapphire1.icns")
sapphire2 = game.image.load("images/sapphire2.icns")
emerald1 = game.image.load("images/emerald1.icns")
emerald2 = game.image.load("images/emerald2.icns")
#heart
heart = game.image.load("images/heart.icns")
emheart = game.image.load("images/emheart.icns")
#enemys
bois = game.image.load("images/boi.icns")
boiattack = game.image.load("images/boiarrow.icns")
#screens
title = game.image.load("images/title.icns")
title2 = game.image.load("images/title2.icns")
title3 = game.image.load("images/title3.icns")
title4 = game.image.load("images/title4.icns")
#other
collection = game.image.load("images/collection.icns")
collection2 = game.image.load("images/collection2.icns")

def protag(x,y):
    win.blit(link,(x,y))
class gamegen():
    def wincheck(hasruby,hassapphire,hastopaz,hasemerald,gamewon,collection,collectionco):
        if hasruby and hassapphire and hastopaz and hasemerald:
            if  (x,y) == (collectionco):
                return True
            else:
                return False
        else:
            return False
    def backgroundgen(allset,rockset,gravel,rock,win,usedrock):
        for i in allrotations:
            win.blit(game.transform.rotate(gravel,allrotations[i]),(i))
            
        for i in rockset:
            if i not in usedrock:
                win.blit(rock,(i))
    def backgroundgengravel(allset,rockset,gravel,rock,win):
        for i in allrotations:
            win.blit(game.transform.rotate(gravel,allrotations[i]),(i))
    def onceagame(win,allset,xset,yset):
        rockset = list()
        yset = sorted(yset)
        for i in xset:
            for z in yset:
                rockset.append((i,z))

        setnum = random.choice(numbers)
        while setnum != 35:
            rockset = list(rockset)
            rockset.remove(random.choice(rockset))
            rockset= set(rockset)
            setnum += 1

        nonrocklist = allset
        for coords in rockset:
            if coords in allset:
                nonrocklist.remove(coords)
        nonrockset = set()
        for i in nonrocklist:
            nonrockset.add(i)
        nonrocklist = list()
        for i in nonrockset:
            nonrocklist.append(i)
        possiblerotation = [0,90,180,270]
        allrotations = {}
        for i in nonrockset:
            currotation = random.choice(possiblerotation)
            win.blit(game.transform.rotate(gravel,currotation),(i))
            allrotations[i] = currotation
        for i in rockset:
            currotation = random.choice(possiblerotation)
            win.blit(game.transform.rotate(gravel,currotation),(i))
            allrotations[i] = currotation
        return nonrocklist, rockset, allrotations
    
##BOI CLASS
class boi():
    def boimove(boiposlist, win,bois):

        boinum = 0
        for boilistsmall in boiposlist:
            if boilistsmall[3] == 0:
                if boilistsmall[0] == boilistsmall[2]:
                    boilistsmall[8] = "left"
                elif boilistsmall[0] == boilistsmall[2]-256:
                    boilistsmall[8] = "right"
                if boilistsmall[8] == "left":
                    boilistsmall[0] -= 32
                    win.blit(bois,(boilistsmall[0],boilistsmall[1]))
                elif boilistsmall[8] == "right":
                    boilistsmall[0] += 32
                    win.blit(bois,(boilistsmall[0],boilistsmall[1]))
                boilistsmall[3] = boilistsmall[4]
            else:
                boilistsmall[3] -= 1
                win.blit(bois,(boilistsmall[0],boilistsmall[1]))
            boiposlist[boinum] = [boilistsmall[0],boilistsmall[1],boilistsmall[2],boilistsmall[3],boilistsmall[4],boilistsmall[5],boilistsmall[6],boilistsmall[7],boilistsmall[8]]
            boinum += 1
        return boiposlist
    def boigen(boiposx,boiposy,nonrocklist):
        (boiposx,boiposy) = random.choice(nonrocklist)
        while True:
          if (boiposx, boiposy) in nonrocklist and (boiposx-64,boiposy) in nonrocklist and (boiposx-128,boiposy) in nonrocklist and (boiposx-192,boiposy) in nonrocklist and (boiposx-256,boiposy) in nonrocklist:
            if boiposy != 576 and boiposx != 1216 and (boiposx-256,boiposy) != (0,64) and boiposy != 640:

                        if (boiposx,boiposy) in usedboico:
                            (boiposx,boiposy) = random.choice(nonrocklist)
                        else:
                            boipos = 0
                            usedboico.append((boiposx,boiposy+64))
                            usedboico.append((boiposx,boiposy-64))
                            while boipos != 256+64:
                                usedboico.append((boiposx-boipos,boiposy))
                                usedboico.append((boiposx+boipos,boiposy))
                                boipos += 64
                            return boiposx, boiposy
            else:
                    (boiposx,boiposy) = random.choice(nonrocklist)
          else:
                (boiposx,boiposy) = random.choice(nonrocklist)
    def boiattack(x,y,boiposlist,life,invincible,death):
        for smallboilist in boiposlist:
            #print(smallboilist)
            if (x,y) == (smallboilist[0],smallboilist[1]) or (x,y) == (smallboilist[0]-32,smallboilist[1]) or (x,y) == (smallboilist[0]+32, smallboilist[1]) or (x,y) == (smallboilist[0], smallboilist[1]+32) or (x,y) == (smallboilist[0], smallboilist[1]-32):
                life -= 1
                invincible = 16

                death.play()
        return life, invincible
    def boishoot(boiattack,boiposlist,rockset):
##        boinum = 0
##        ### smallboilist[5] is y pos of attack 6 is x pos and 7 is timer
##        for smallboilist in boiposlist:
##
##
## #           print(smallboilist[7])
##            if (smallboilist[0],smallboilist[5]+64) in rockset:
##                        smallboilist[5] = 0
##                        smallboilist[6] = 0
##            elif smallboilist[7] == 0: ### if the timer equals zero
##                if smallboilist[5] == 0: ### if the y position of attack equals zero
##
##                        
##                    
##                        smallboilist[6] = smallboilist[0] ### x position of attack will equal current x pos of enemy
##                        win.blit(boiattack,(smallboilist[6],smallboilist[1]-64)) ### Create an attack one tile above the enemy
##                        smallboilist[5] = smallboilist[1]-128 ### the y position of the attack will now be the y position of the enemy two tiles up
##                elif smallboilist[5] != 0: ### if the y position of the attack isnt zero
##                    if smallboilist[5] == smallboilist[1]-128: ### If its two tiles up
##                        win.blit(boiattack,(smallboilist[6],smallboilist[5])) ###Blit it
##                        smallboilist[5] = smallboilist[1]-192 ### it now equals the y position -192 (3x64)
##                    elif smallboilist[5] == smallboilist[1]-192: ### if it equals the y position -192 (3x64)
##                        win.blit(boiattack,(smallboilist[6],smallboilist[5])) ### Blit it
##                        smallboilist[5] = smallboilist[1]-256 ### it now equals the y position -256 (4x64)
##                    elif smallboilist[5] == smallboilist[1]-256: ### if it equals the y position -256 (4x64)
##                        win.blit(boiattack,(smallboilist[6],smallboilist[5])) ### Blit it
##                        smallboilist[5] = 0 ### y pos of attack is now 0
##                        smallboilist[6] = 0 ### x attack is zero
##                smallboilist[7] = 6
##            
##            else:#elif smallboilist[7] < 0:
##                ### NEED TO CHECK IF OR ISNT  smallboilist[5] IS ZERO, I.E OVER
##                if smallboilist[5] != 0:
##                    win.blit(boiattack,(smallboilist[6],smallboilist[5]))
##                smallboilist[7] -= 1
##            boiposlist[boinum] = [smallboilist[0],smallboilist[1],smallboilist[2],smallboilist[3],smallboilist[4],smallboilist[5],smallboilist[6],smallboilist[7]]
##            boinum +=1
##
##
##        return boiposlist


        for smallboilist in boiposlist:
            if (smallboilist[0],smallboilist[5]-64) in rockset:
                smallboilist[5] == smallboilist[1]
            for enemy in boiposlist:
                if (smallboilist[0],smallboilist[5]-64) == (enemy[0],enemy[1]):
                    smallboilist[5] == smallboilist[1]

                    
            if smallboilist[7] == 0:
                if smallboilist[5] == smallboilist[1]:
                    pass
                elif smallboilist[5] <= smallboilist[1]:
                    if smallboilist[5] == smallboilist[1]-64:
                        smallboilist[5] = smallboilist[1]-64
                        win.blit(boiattack,(smallboilist[6],smallboilist[5]))
                    if smallboilist[5] == smallboilist[1]-128:
                        smallboilist[5] = smallboilist[1]-64
                        win.blit(boiattack,(smallboilist[6],smallboilist[5]))
            else:
                smallboilist[7] -= 1
                if smallboilist[5] != smallboilist[1]:
                    win.blit(boiattack,(smallboilist[6],smallboilist[5]))




        boinum = 0
        for smallboilist in boiposlist:
           boiposlist[boinum] = [smallboilist[0],smallboilist[1],smallboilist[2],smallboilist[3],smallboilist[4],smallboilist[5],smallboilist[6],smallboilist[7],smallboilist[8]]
           boinum +=1
            
        return boiposlist




class bar():

    def points(points):
        if points > 999:
            points = 999
        if points < 0:
            points = 0

        helve = game.font.SysFont("American Typewriter",60)
        mypoints = helve.render("Points: "+str(points), True, (0, 0, 0))
        win.blit(mypoints,(640-64,576))
#        curpoints = list(str(points))
#        for i in range(3):
#            locvar = int((i*64))
#            curpoints[i] = int(curpoints[i])
#            print(type(curpoints[i]))
#            win.blit(dicnumbers[curpoints[i]],(704+locvar,576))
        

        
    def genbar(win,bar1):
        barsize = 0
        while barsize != 1152+64:
            win.blit(bar1,(barsize,576))
            barsize +=64


    def life(heart,emheart,win,gamelost):
        if life == 3:
            win.blit(heart,(960,576))
            win.blit(heart,(1024,576))
            win.blit(heart,(1088,576))
            return False
        elif life == 2:
            win.blit(emheart,(960,576))
            win.blit(heart,(1024,576))
            win.blit(heart,(1088,576))
            return False
        elif life == 1:
            win.blit(emheart,(960,576))
            win.blit(emheart,(1024,576))
            win.blit(heart,(1088,576))
        elif life == 0:
            return True

    def gems(hasruby,ruby1,ruby2,rubyco, hastopaz,topaz1,topaz2,topazco , hassapphire , sapphire1 ,sapphire2 ,sapphireco ,hasemerald , emerald1 ,emerald2 ,emeraldco ,  win,topazempty,rubyempty,emeraldempty,sapphireempty,collection,collectionco):

        if hasruby == True:
            win.blit(rubyempty,(rubyco))
            win.blit(ruby1,(64,576))
        elif hasruby == False:

            win.blit(rockruby,(rubyco))
            win.blit(ruby2,(64,576))

        if hastopaz == True:
            win.blit(topazempty,(topazco))
            win.blit(topaz1,(64+128,576))
        elif hastopaz == False:
            win.blit(rocktopaz,(topazco))
            win.blit(topaz2,(64+128,576))
        if hassapphire == True:
            win.blit(sapphireempty,(sapphireco))
            win.blit(sapphire1,(64+128+128,576))
        elif hassapphire == False:
            win.blit(rocksapphire,(sapphireco))
            win.blit(sapphire2,(64+128+128,576))
        if hasemerald == True:
            win.blit(emeraldempty,(emeraldco))
            win.blit(emerald1,(64+128+128+128,576))
        elif hasemerald == False:
            win.blit(rockemerald,(emeraldco))
            win.blit(emerald2,(64+128+128+128,576))
        if hasemerald == True and hasruby == True and hassapphire == True and hastopaz == True:
            win.blit(collection2,(collectionco))

        else:
            win.blit(collection,(collectionco))
life = 3
points = 0

def idk():
    move = "s"
    xvar = 0
    xset = set()
    yvar = 0
    yset = set()
    while xvar < 1217:
        xset.add(xvar)
        xvar = xvar+128
    while yvar < 577:
        yset.add(yvar)
        yvar = yvar+128
    yvar = 0
    yallset = set()
    while yvar < screenHeight+1:
        yallset.add(yvar)
        yvar = yvar+64
    xvar = 0
    xallset = set()
    while xvar < screenWidth+1:
        xallset.add(xvar)
        xvar = xvar+64

    allset = list()
    for i in yallset:
        for z in xallset:
            allset.append((z,i))
    rockset = list()
    x = 0
    y = 64
    direction = "left"
    usedboico = []
    enemynum = 0
    return move, allset, x, y, usedboico, enemynum,xset,yset
    
while True:

    move, allset, x, y, usedboico, enemynum,xset,yset = idk()
 
    nonrocklist, rockset, allrotations = gamegen.onceagame(win,allset,xset,yset)
    usedrock = []
    rockset = list(rockset)


    
    rubyco = random.choice(rockset)
    topazco = random.choice(rockset)
    sapphireco = random.choice(rockset)
    emeraldco = random.choice(rockset)
    collectionco = random.choice(rockset)


    usedrock.append(rubyco)
    while topazco in usedrock:
        topazco = random.choice(rockset)
    usedrock.append(topazco)
    while sapphireco in usedrock:
        sapphireco = random.choice(rockset)
    usedrock.append(sapphireco)
    while emeraldco in usedrock:
        emeraldco = random.choice(rockset)
    usedrock.append(emeraldco)
    while collectionco in usedrock:
        collectionco = random.choice(rockset)
    usedrock.append(collectionco)
    rockset.remove(collectionco)


    rockset = set(rockset)
    hasruby = False
    hastopaz = False
    hassapphire = False
    hasemerald = False
    gamewon = False
    gamelost = False
    enemynum = 0
    
    runtitle = True
    rungame = False
    allowmove = 0
    invincible = 0
    while runtitle == True:



        game.time.delay(10)

        easy = game.draw.rect(win, (0, 0, 0),(32, 448, 304, 160))
        medium = game.draw.rect(win, (0, 0, 0),(350, 448, 434, 160))
        hard = game.draw.rect(win, (0, 0, 0),(800, 448, 304, 160))

        gamegen.backgroundgengravel(allset,rockset,gravel,rock,win)
        #for i in allset:
#            win.blit(gravel,(i))
        if easy.collidepoint(game.mouse.get_pos()):
            win.blit(title2,(0,0))
        elif medium.collidepoint(game.mouse.get_pos()):
            win.blit(title3,(0,0))
        elif hard.collidepoint(game.mouse.get_pos()):
            win.blit(title4,(0,0))
        else:
            win.blit(title,(0,0))

        
        win.blit(emerald1,(1136,544))
        win.blit(topaz1,(1136,16))
        win.blit(ruby1,(1136,16+181))
        win.blit(sapphire1,(1136,544-181))

        helve = game.font.SysFont("American Typewriter",60)
        mypoints = helve.render("Points: "+str(points), True, (200, 250, 0))
        win.blit(mypoints,(640-64-64-32-16,576-128-64-32))

        left, middle, right = game.mouse.get_pressed()

        if easy.collidepoint(game.mouse.get_pos()) and left:
            enemynum = 5
            gamespeed = 70
            mode = "easy"
            menu.play()
            rungame = True
            runtitle = False
        if medium.collidepoint(game.mouse.get_pos()) and left:
            enemynum = 7
            mode = "medium"
            gamespeed = 70
            menu.play()
            rungame = True
            runtitle = False
        elif hard.collidepoint(game.mouse.get_pos()) and left:
            enemynum = 10
            gamespeed = 70
            mode = "hard"
            menu.play()
            rungame = True
            runtitle = False



        for event in game.event.get():
            if event.type == game.QUIT:
                rungame = False
                runtitle = False





        game.display.update()
    if rungame == True:
        x = 0
        y = 64
        ### CHOOSE HOW MANY!
        boiposx = 0
        boiposy = 0
        boiposlist = []
        for i in range(enemynum):
            
            boiposx, boiposy = boi.boigen(boiposx,boiposy,nonrocklist)
            originalboiposx = boiposx
            possiblespeeds = [4,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3]
            boispeed = random.choice(possiblespeeds)
            originalboispeed = boispeed
            boisattacky = boiposy
            boiattackx = boiposx
            timecheck = 6
            direction = "left"

            boiposlist.append([boiposx, boiposy, originalboiposx, boispeed, originalboispeed, boisattacky,boiattackx,timecheck,direction])
    while rungame == True:
        game.time.delay(int(gamespeed/4)-20)
        for event in game.event.get():
            if event.type == game.QUIT:
                runtitle = False
                rungame = False
        if allowmove != 0:
            allowmove = allowmove - 0.25
            if allowmove in [1,2,3]:
                allowmove = int(allowmove)
        keys = game.key.get_pressed()
        if allowmove <= 0:
            if keys[game.K_a] and x > 63:
                if ((x - 64),y) in rockset:

                    pass
                else:
                    move = "a"
                    allowmove = 2
            if keys[game.K_d] and x < screenWidth - 129 + 64:
                if ((x + 64),y) in rockset:
                    pass
                else:
                    move = "d"
                    allowmove = 2
            if keys[game.K_w] and y > 63:
                if (x,(y-64)) in rockset:
                    pass
                else:
                    move = "w"
                    allowmove = 2
            if keys[game.K_s] and y < screenHeight-64 - 64 - 64+ 1:
                if (x,(y+64)) in rockset:
                    pass
                else:
                    move = "s"
                    allowmove = 2

        if keys[game.K_m]:
            if rubyco == (x-64,y) or rubyco == (x+64,y) or rubyco == (x,y-64) or rubyco == (x,y+64):
                if hasruby == False:
                    hasruby = True
                    pickupgem.play()
            if topazco == (x-64,y) or topazco == (x+64,y) or topazco == (x,y-64) or topazco == (x,y+64):
                if hastopaz == False:
                    hastopaz = True
                    pickupgem.play()
            if sapphireco == (x-64,y) or sapphireco == (x+64,y) or sapphireco == (x,y-64) or sapphireco == (x,y+64):
                if hassapphire == False:
                    hassapphire = True
                    pickupgem.play()
            if emeraldco == (x-64,y) or emeraldco == (x+64,y) or emeraldco == (x,y-64) or emeraldco == (x,y+64):
                if hasemerald == False:
                    hasemerald = True
                    pickupgem.play()
        gamegen.backgroundgen(allset,rockset,gravel,rock,win,usedrock)
        bar.genbar(win,bar1)


        boiposlist = boi.boimove(boiposlist, win,bois)


        boiposlist = boi.boishoot(boiattack,boiposlist,rockset)

        
        

        bar.gems(hasruby,ruby1,ruby2,rubyco, hastopaz,topaz1,topaz2,topazco , hassapphire , sapphire1 ,sapphire2 ,sapphireco ,hasemerald , emerald1 ,emerald2 ,emeraldco ,  win,topazempty,rubyempty,emeraldempty,sapphireempty,collection,collectionco)


        if allowmove == 0:
            if move == "s":
                win.blit(link,(x,y))
            if move == "w":
                win.blit(link,(x,y))
            if move == "d":
                win.blit(link,(x,y))
            if move == "a":
                win.blit(link,(x,y))

        elif allowmove == 1:
            if move == "s":
                y += 32
                win.blit(link2,(x,y))
            if move == "w":
                y -= 32
                win.blit(link2,(x,y))
            if move == "d":
                x += 32
                win.blit(link2,(x,y))
            if move == "a":
                x -= 32
                win.blit(link2,(x,y))


        elif allowmove == 2:
            if move == "s":
                y+=32
                win.blit(link1,(x,y))
            if move == "w":
                y-=32
                win.blit(link1,(x,y))
            if move == "d":
                x+=32
                win.blit(link1,(x,y))
            if move == "a":
                x-=32
                win.blit(link1,(x,y))
        elif allowmove in [0.25,0.5,0.75,1.25,1.5,1.75,2.25,2.5]:
            win.blit(link1,(x,y))
        gamewon = gamegen.wincheck(hasruby,hassapphire,hastopaz,hasemerald,gamewon,collection,collectionco)



        if invincible == 0:
            life,invincible = boi.boiattack(x,y,boiposlist,life,invincible,death)

        gamelost = bar.life(heart,emheart,win,gamelost)
        if invincible != 0:
            invincible -= 1
        bar.points(points)
        
        game.display.update()
        if gamewon == True or gamelost == True:
            if gamelost == True:
                life = 3
                points = 0
            if gamewon == True:
                if mode == "easy":
                    points += 1
                if mode == "medium":
                    points +=3
                if mode == "hard":
                    points +=5
            runtitle = True
            rungame = False
        
    if runtitle == False and rungame == False:
        break
game.quit()
