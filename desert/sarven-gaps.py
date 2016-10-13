# Get to the Oasis by moving down 10m at a time.
# Build fences 20m to the left of each ogre.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Build fences 20 units to the enemy's left.
        hero.buildXY("fence", enemy.pos.x - 20, enemy.pos.y)
        pass
    else:
        # Move down 10 units at a time.
        hero.moveXY(hero.pos.x, hero.pos.y - 10)
        pass
