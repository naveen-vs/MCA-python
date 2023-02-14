from graphics.rectangle import*
from graphics.circle import*
from graphics.TDgraphics.cuboid import*
from graphics.TDgraphics.sphere import*

l=int(input('length of rectangle ='))
b=int(input('breadth of rectangle ='))
print('area of rectangle=',RectArea(l,b))
print('perimetr of rectangle=',RectPerimeter(l,b))

r=int(input('radius of the circle='))
print('circle area=',CirArea(r))
print('circle perimeter=',Ciperimeter(r))

l1=int(input('length of cuboid ='))
b1=int(input('breadth of cuboid ='))
h1=int(input('height of cuboid ='))
print('area of cubiod=',CuArea(l1,b1,h1))
print('perimeter of cubiod=',CuPerimeter(l1,b1,h1))

r1=int(input('radius of the sphere='))
print('sphere area=',SpArea(r))
print('sphere volume=',SpVolume(r))