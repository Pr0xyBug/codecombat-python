# Use fire-traps to defeat the ogres attacking the trading post.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.pos.x < hero.pos.x:
            # If the enemy is to the left, build a fire-trap to the left.
            x = (enemy.pos.x + hero.pos.x) / 2
            hero.buildXY("fire-trap", x, hero.pos.y)
            pass
        elif enemy.pos.x > hero.pos.x:
            # If the enemy is to the right, build a fire-trap to the right.
            x = (enemy.pos.x + hero.pos.x) / 2
            hero.buildXY("fire-trap", x, hero.pos.y)
            pass
        elif enemy.pos.y < hero.pos.y:
            # If the enemy is below the hero, build a fire-trap below.
            y = (enemy.pos.y + hero.pos.y) / 2
            hero.buildXY("fire-trap", hero.pos.x, y)
            pass
        elif enemy.pos.y > hero.pos.y:
            # If the enemy is above the hero, build a fire-trap above.
            y = (enemy.pos.y + hero.pos.y) / 2
            hero.buildXY("fire-trap", hero.pos.x, y)
    hero.moveXY(40, 34)
