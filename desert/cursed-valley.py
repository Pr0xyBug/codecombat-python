# It's too hot out here! Every second you will lose health.
# You need to kill 3 enemy skeletons.
# You can only drink one potion. Choose your time wisely.
# Graverobbing is bad luck! Do not steal the coins.

while True:
    enemy = hero.findNearestEnemy()
    # Attack only skeletons AND skeletons that are on the "ogres" team.
    if enemy and enemy.team == "ogres" and enemy.type == "skeleton":
        hero.attack(enemy)
    
    item = hero.findNearestItem()
    # Take only the items with a "potion" type AND only when your health is less than a quarter of the maxHealth.
    if hero.health < hero.maxHealth * .30 and item and item.type == "potion":
        hero.moveXY(item.pos.x, item.pos.y)
