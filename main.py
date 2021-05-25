import pyxel

class Main:
    def __init__(self):
        pyxel.init(128, 128, caption="Master Robot", fps=60)
        pyxel.load('assets/tilemap.pyxres', True, True, False, False)
        pyxel.run(self.update, self.draw)

    def update(self):
        print("aaa")

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 16, 16)

if __name__ == '__main__':
    Main()