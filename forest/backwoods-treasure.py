# Collect 100 gold from two or three groves.
# Use a sword with Cleave.
# Move to another location with a Flag.

loop:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if flag:
        flagpos = flag.pos
        flagx = flagpos.x
        flagy = flagpos.y
        hero.moveXY(flagx, flagy)
        hero.pickUpFlag(flag)
    elif enemy:
        ready = hero.isReady("cleave")
        distance = hero.distanceTo(enemy)
        if ready and distance < 5:
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
    elif item:
        itempos = item.pos
        itemx = itempos.x
        itemy = itempos.y
        hero.moveXY(itemx, itemy)
    else:
        pass

        
    
