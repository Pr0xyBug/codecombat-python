# Uh oh, a stampede! Use your cunning to make it to the oasis.

while True:
    enemy = hero.findNearestEnemy()
    xPos = hero.pos.x + 5
    yPos = 17
    if enemy:
        # You only need to shift up/down 1m to dodge the yaks!
        if enemy.pos.y > hero.pos.y:
            # If the Yak is above you, adjust yPos downwards!
            yPos -= 1
            pass
        elif enemy.pos.y < hero.pos.y:
            # If the Yak is below you, adjust yPos upwards!
            yPos += 1
            pass
    hero.moveXY(xPos, yPos)
