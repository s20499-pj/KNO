class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    value = None


class Map:
    empty = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
             [[0, None, 0], [0, None, 0], [0, None, 0]],
             [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

    renderLine = ""

    def print(self):
        for x in range(len(self.empty)):
            for y in range(len(self.empty[x])):
                for z in range(len(self.empty[x][y])):
                    self.renderLine += str(self.empty[x][y][z])
                    if z != 2:
                        if y == 0:
                            self.renderLine += "-----"
                        elif y == 1:
                            self.renderLine += "---"
                        else:
                            self.renderLine += "-"
                print(self.renderLine)
                self.renderLine = ""

if __name__ == '__main__':
    map = Map()
    map.print()
    