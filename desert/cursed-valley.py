# For the maxHealth you can use Multiplication with
# a decimal value or Division with an integer like 7.

while True:
    enemy = hero.findNearestEnemy()
    # Attack only skeletons AND skeletons that are on the "ogres" team.
    if enemy and enemy.team == "ogres" and enemy.type == "skeleton":
        hero.attack(enemy)
    
    item = hero.findNearestItem()
    # Take only the items with a "potion" type AND only when your health is less than a quarter of the maxHealth.
    if hero.health < hero.maxHealth * .35 and item and item.type == "potion":
        hero.moveXY(item.pos.x, item.pos.y)
