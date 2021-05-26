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
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_W):
            pyxel.circ(
                12,
                12,
                2,
                8
            )

    def draw(self):
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
            12,
            12,
            2,
            8
        )

if __name__ == '__main__':
    Main()