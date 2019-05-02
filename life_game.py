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
  
  # 各セルの生死を判断して世界を更新する
  def update_world(self):
    pass

  # 世界を描画する
  def draw_world(self):
    for y, row in enumerate(self.world):
      for x, cell in enumerate(row):
        if cell:
          pyxel.pix(x, y + 30, 3)

App()
