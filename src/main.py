# PYTHON VERSION: 3.11.9

import character_class as chara
import constants as c
import core

def main():
    player = chara.Character(c.BASE_VICTORY, c.MAX_LIFE)
    goku = chara.Character(c.BASE_VICTORY, c.MAX_LIFE)

    core.play(player, goku)

if __name__ == "__main__":
    main()
