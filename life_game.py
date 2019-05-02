import pyxel
APP_WIDTH = 150
APP_HEIGHT = 120

class App:
  def __init__(self):
    self.world = [[1, 0, 1, 0, 0, 1],
                  [0, 0, 0, 0, 1, 0],
                  [1, 0, 1, 1, 0, 0]]
    pyxel.init(APP_WIDTH, APP_HEIGHT, caption="Life Game")
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    self.update_world()

  def draw(self):
    pyxel.cls(0)
    self.draw_world()
  
  # $B3F%;%k$N@8;`$rH=CG$7$F@$3&$r99?7$9$k(B
  def update_world(self):
    pass

  # $B@$3&$rIA2h$9$k(B
  def draw_world(self):
    for y, row in enumerate(self.world):
      for x, cell in enumerate(row):
        if cell:
          pyxel.pix(x, y + 30, 3)

App()
