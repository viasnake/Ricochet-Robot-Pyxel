import pyxel
import random

#class Player:
#    def __init__(self):
#        self.x = 0
#        self.y = 0

class Generator:

    def player(self):
        u = random.choice((
            '0', # Green
            '16', # Blue
            '32', # Red
            '48' # Yellow
        ))
        x = random.randint(0, 15) * 16
        y = random.randint(0, 15) * 16
        print(u, x, y)
        return(u, x, y)

#    def goal(self):
class Main:
    def __init__(self):
        pyxel.init(
            256, 256,
            caption="Master Robot",
            fps=60
        )
        pyxel.load(
            'assets/tilemap_v2.pyxres',
            True,
            True,
            False,
            False
        )

        self.player = generate.player()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_R):
            self.player = generate.player()


    def draw(self):
        pyxel.cls(13)

        # bltm(x, y, tm, u, v, w, h, [colkey])
        pyxel.bltm(
            0,
            0,
            0,
            0,
            0,
            16,
            16,
            0
        )

        # bltm(x, y, tm, u, v, w, h, [colkey])
        pyxel.bltm(
            16*8,
            0,
            0,
            0,
            48,
            16,
            16,
            0
        )

        # bltm(x, y, tm, u, v, w, h, [colkey])
        pyxel.bltm(
            0,
            16*8,
            0,
            0,
            16,
            16,
            16,
            0
        )

        # bltm(x, y, tm, u, v, w, h, [colkey])
        pyxel.bltm(
            16*8,
            16*8,
            0,
            0,
            32,
            16,
            16,
            0
        )

        # blt(x, y, img, u, v, w, h, [colkey])
        pyxel.blt(
            self.player[1],
            self.player[2],
            0,
            self.player[0],
            8*2,
            16,
            16,
            0
        )

        # rectb(x, y, w, h, col)
        pyxel.rectb(
            0,
            0,
            16*16,
            16*16,
            5
        )

generate = Generator()    
Main()
