import pyxel
import pandas
import copy

APP_WIDTH = 150
APP_HEIGHT = 120

class App:
  def __init__(self):
    self.world = pandas.read_csv("world.csv", header=None).values.tolist()
    pyxel.init(len(self.world[0]), len(self.world), caption="Life Game", fps = 1)
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    self.update_world()

  def draw(self):
    pyxel.cls(0)
    self.draw_world()
  
  # $B@$3&$r99?7$9$k(B
  def update_world(self):
    # $B8=:_>uBV$NJ]B8(B
    snapshot = copy.deepcopy(self.world)
 
    for y, row in enumerate(snapshot):
      if y == 0 or y == len(snapshot) - 1:
        continue

      for x, cell in enumerate(row):
        if x == 0 or x == len(row) - 1:
          continue

        # $BNY@\$9$k@8$-$F$$$k%;%k$r?t$($k(B
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

        # $B%;%k$N@8;`$rH=Dj$9$k(B
        if cell == 0 and count == 3:
          self.world[y][x] = 1
        elif cell and count < 2:
          self.world[y][x] = 0
        elif cell == 1 and (count == 2 or count == 3):
          self.world[y][x] = 1
        elif cell and 3 < count:
          self.world[y][x] = 0

  # $B@$3&$rIA2h$9$k(B
  def draw_world(self):
    for y, row in enumerate(self.world):
      for x, cell in enumerate(row):
        if cell:
          pyxel.pix(x, y, 3)

App()
