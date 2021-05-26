import pyxel
import random

#class Player:
#    def __init__(self):
#        self.x = 0
#        self.y = 0

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

        self.gen()

#        self.player = Player()

        pyxel.run(self.update, self.draw)

    def update(self):
#        x = self.player.x
#        y = self.player.y
#
#        if pyxel.btn(pyxel.KEY_W):
#            y = y - 8
#        elif pyxel.btn(pyxel.KEY_S):
#            y = y + 8
#        elif pyxel.btn(pyxel.KEY_A):
#            x = x - 8
#        elif pyxel.btn(pyxel.KEY_D):
#            x = x + 8
#
#        self.player.x = x
#        self.player.y = y
#        print(self.player.x, self.player.y)
        if pyxel.btn(pyxel.KEY_R):
            self.gen()


    def draw(self):
#        x = self.player.x
#        y = self.player.y

        pyxel.cls(13)

        # bltm(x, y, tm, u, v, w, h, [colkey])
        pyxel.bltm(
            0,
            0,
            0,
            0,
            0,
            32,
            32,
            0
        )

        # blt(x, y, img, u, v, w, h, [colkey])
        pyxel.blt(
            self.x,
            self.y,
            0,
            0,
            8*2,
            16,
            16,
            0
        )
        
#        pyxel.circ(
#            x + 8/2,
#            y + 8/2,
#            2,
#            8
#        )

    def gen(self):
        self.color = random.choice((
            '3', # Green
            '5', # Blue
            '8', # Red
            '10' # Yellow
        ))
        self.x = random.randint(0, 16) * 16
        self.y = random.randint(0, 16) * 16
        print(self.color, self.x, self.y)

if __name__ == '__main__':
    Main()