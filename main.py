import pyxel

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

class Main:
    def __init__(self):
        pyxel.init(
            128, 128,
            caption="Master Robot",
            fps=60
        )
        pyxel.load(
            'assets/tilemap.pyxres',
            True,
            True,
            False,
            False
        )

        self.player = Player()

        pyxel.run(self.update, self.draw)

    def update(self):
        x = self.player.x
        y = self.player.y

        if pyxel.btn(pyxel.KEY_W):
            y = y - 8
        elif pyxel.btn(pyxel.KEY_S):
            y = y + 8
        elif pyxel.btn(pyxel.KEY_A):
            x = x - 8
        elif pyxel.btn(pyxel.KEY_D):
            x = x + 8

        self.player.x = x
        self.player.y = y
        print(self.player.x, self.player.y)


    def draw(self):
        x = self.player.x
        y = self.player.y

        pyxel.cls(0)
        pyxel.bltm(
            0,
            0,
            0,
            0,
            0,
            16,
            16
        )
        pyxel.circ(
            x + 8/2,
            y + 8/2,
            2,
            8
        )

if __name__ == '__main__':
    Main()