import pyxel
import random

class Generator:

    def player(self):
        u = random.choice((
            0, # Green
            16, # Blue
            32, # Red
            48 # Yellow
        ))
        x = random.randint(0, 15) * 16
        y = random.randint(0, 15) * 16
        print(u, x, y)
        return(u, x, y)

    def goal(self):
        array = [
            [1, 6],
            [2, 1],
            [2, 10],
            [4, 5],
            [4, 13],
            [5, 8],
            [6, 3],
            [6, 14],
            [9, 12],
            [10, 2],
            [10, 7],
            [11, 14],
            [12, 9],
            [13, 1],
            [14, 6],
            [14, 13],
        ]
        return random.choice(array)

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
        self.goal = generate.goal()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_R):
            self.player = generate.player()
            self.goal = generate.goal()

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

        # circb(x, y, r, col)
        pyxel.circb(
            16*self.goal[0]+8,
            16*self.goal[1]+8,
            7,
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
