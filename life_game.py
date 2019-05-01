import pyxel

class App:
    def __init__(self):
        pyxel.init(150, 120, caption="Life Game")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(1, 1, "frame_count: " + str(pyxel.frame_count), 1)
        pyxel.circ(30, pyxel.frame_count % 100, 5, 2)

App()
