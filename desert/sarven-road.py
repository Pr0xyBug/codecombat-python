# Get to the oasis. Watch out for new enemies: ogre scouts!
# Go up and right by adding to your current X and Y position.

while True:
    # Attack any enemies you see.
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    # Or, if there are no enemies in sight, keep moving up and to the right.
    else:
        x = hero.pos.x + 5
        y = hero.pos.y + 5
        hero.moveXY(x, y)
    pass
    
