from random import randint

from functions import hit


class Player:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def botHit(self, player):
        roundPower = randint(0, self.power)

        if player.health > roundPower:
            if roundPower == 1:
                print("Вам нанесли " + str(roundPower) + " урон")
            else:
                print("Вам нанесли " + str(roundPower) + " урона")
                player.health -= roundPower
        elif player.health < roundPower:
            if roundPower == 1:
                print("Вам восстановили " + str(roundPower) + " здоровье")
            else:
                print("Вам восстановили " + str(roundPower) + " здоровья")
                player.health += roundPower
        else:
            player.health = 0

    def playerHit(self, bot):

        roundPower = randint(0, self.power)
        damage = hit(roundPower)

        if bot.health >= damage:  # roundPower
            # puts(bot.health
            # Грамматика
            if damage == 1:
                print("Вы нанесли врагу " + str(damage) + " урон\n")
            else:
                print("Вы нанесли врагу " + str(damage) + " урона\n")

            bot.health -= damage
            # puts(bot.health
            # show_info(self, bot)
        elif bot.health < damage:  # roundPower
            # puts("БЕРСЕРК!!!!"
            if damage == 1:
                print("Вы восстановили врагу " + str(damage) + " здоровье \n")
            else:
                print("Вы восстановили врагу " + str(damage) + " здоровья \n")
            bot.health += damage
        else:
            print("ERROR END GAME")
            bot.health = 0