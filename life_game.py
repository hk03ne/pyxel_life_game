import sys
import pyxel
import pandas
import copy

class App:
  def __init__(self):
    self.world = pandas.read_csv(sys.argv[1], header=None).values.tolist()
    pyxel.init(len(self.world[0]), len(self.world), caption="Life Game", fps = 1)
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    self.update_world()

  def draw(self):
    pyxel.cls(0)
    self.draw_world()
  
  # 世界を更新する
  def update_world(self):
    # 現在状態の保存
    snapshot = copy.deepcopy(self.world)
 
    for y, row in enumerate(snapshot):
      # 上端と下端はスキップ
      if y == 0 or y == len(snapshot) - 1:
        continue

      for x, cell in enumerate(row):
        # 左端と右端はスキップ
        if x == 0 or x == len(row) - 1:
          continue

        # 隣接する生きているセルを数える
        count = 0
        if snapshot[y-1][x-1]:
          count = count + 1
        if snapshot[y-1][x]:
          count = count + 1
        if snapshot[y-1][x+1]:
          count = count + 1
        if snapshot[y][x-1]:
          count = count + 1
        if snapshot[y][x+1]:
          count = count + 1
        if snapshot[y+1][x-1]:
          count = count + 1
        if snapshot[y+1][x]:
          count = count + 1
        if snapshot[y+1][x+1]:
          count = count + 1

        # セルの生死を判定する
        if cell == 0 and count == 3:
          # 誕生
          self.world[y][x] = 1
        elif cell and count < 2:
          # 過疎による死亡
          self.world[y][x] = 0
        elif cell == 1 and (count == 2 or count == 3):
          # 生存
          self.world[y][x] = 1
        elif cell and 3 < count:
          # 過密による死亡
          self.world[y][x] = 0

  # 世界を描画する
  def draw_world(self):
    for y, row in enumerate(self.world):
      for x, cell in enumerate(row):
        if cell:
          pyxel.pix(x, y, 3)

App()
