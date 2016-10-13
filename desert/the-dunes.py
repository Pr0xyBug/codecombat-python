# Collect coins. Ignore sand yaks and burls. Fight throwers and ogres.

loop:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if enemy:
        if enemy.type is "sand-yak" or enemy.type is "burl":
            # Don't fight sand yaks or burls! Just keep collecting coins.
            itempos = item.pos
            itemx = itempos.x
            itemy = itempos.y
            hero.moveXY(itemx, itemy)
        elif enemy.type is "thrower" or enemy.type is "ogre":
            # But if the enemy is type "thrower" or "ogre", attack them.
            ready = hero.isReady("cleave")
            distance = hero.distanceTo(enemy)
            if ready and distance < 5:
                hero.cleave(enemy)
            else:
                hero.attack(enemy)
        else:
            pass
    elif item:
        itempos = item.pos
        itemx = itempos.x
        itemy = itempos.y
        hero.moveXY(itemx, itemy)
    else:
        pass
