def fight(player, bot):
    while isAlive(player) and isAlive(bot):
        player.playerHit(bot)
        bot.botHit(player)

        siin(player)

    if isAlive(player):
        print(player.name + " WON!!")
    elif isAlive(bot):
        print(bot.name + " WON!!")
    else:
        print("TIE!!!")


def hit(power):
    a = int(input("\nСколько урона нанести? (до " + str(power) + ")\n"))

    while a > power:
        a = int(input("\nУ вас мало сил для нанесения такоего количества урона (до " + str(power) + ")\n"))
    return a


def isAlive(I):
    if I.health == 0:
        return False
    else:
        return True


# Show info
def si(p):
    print("Name: " + p[0] + ", Health: " + str(p[1]) + ", Power: " + str(p[2]))


def siin(p):
    print(p.name + " - Health: " + str(p.health) + ", Power: " + str(p.power))