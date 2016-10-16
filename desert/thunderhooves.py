# Get to the oasis,
# fencing off paths with randomized yaks on them as you go.

while True:
    yak = hero.findNearestEnemy()
    if yak:
        # A yak is above you if yak.pos.y is greater than your pos.y.
        if yak.pos.y > hero.pos.y:
            # If the yak is above you, build a fence 10m below it.
            hero.buildXY("fence", hero.pos.x, yak.pos.y - 10)
        if yak.pos.y < hero.pos.y:
            # If the yak is below you, build a fence 10m above it.
            hero.buildXY("fence", hero.pos.x, yak.pos.y + 10)
        pass
    else:
        # Move right 10m towards the oasis.
        hero.moveXY(hero.pos.x + 10, hero.pos.y)
        pass
