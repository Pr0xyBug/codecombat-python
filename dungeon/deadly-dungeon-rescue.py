# **Equip a powerful weapon.**

# Collects near-by item.
def findItem():
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)

# Breaks down nearest door.
def findEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

# Move sequence calling definitions.
hero.moveXY(27, 82)
findItem()
hero.moveXY(8, 87)
hero.moveXY(47, 124)
findEnemy()
hero.moveXY(46, 104)
findItem()
hero.moveXY(35, 103)
findItem()
hero.moveXY(60, 102)
findItem()
hero.moveXY(44, 31)
findItem()
hero.moveXY(60, 30)
findItem()
hero.moveXY(44, 102)
hero.moveXY(83, 123)
hero.moveXY(83, 99)
findEnemy()
hero.moveXY(102, 121)
hero.moveXY(100, 99)
hero.moveXY(151, 80)
hero.moveXY(150, 27)
findEnemy()
hero.moveXY(132, 30)
findEnemy()
hero.moveXY(128, 52)
hero.moveXY(109, 56)
hero.moveXY(110, 42)
hero.say("Come with me Princess...")
hero.moveXY(150, 25)
hero.moveXY(150, 10)
hero.moveXY(47, 9)
findEnemy()
hero.moveXY(49, 114)
hero.moveXY(81, 121)
hero.moveXY(85, 100)
hero.moveXY(151, 100)
