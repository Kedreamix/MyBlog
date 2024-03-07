import layoutparser as lp
from layoutparser.elements import Layout
from layoutparser.elements import TextBlock, Rectangle

blocks = Rectangle(1, 2, 3, 4)
print(blocks.points[1,0])
