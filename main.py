from Player import Player

from functions import si, fight

import random as rand

if __name__ == "__main__" or "__android__":
	player = ["GamePlayer", rand.randint(1, 100), 20]
	bot = ["Bot", rand.randint(1, 100), 20]

	print("PLAYER INFO")

	si(player)

	p1 = Player(player[0], player[1], player[2])
	p2 = Player(bot[0], bot[1], bot[2])

	fight(p1, p2)
