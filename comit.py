import os
import time
import pynput
width = 20  #размер игрового поля
height = 20
bulletsSpeed = 4 #скорость движения
boatY = 18 #расположние по У на поле
ship = {'x': 5}
bullets = [
	{'x': 5, 'y': 6},
	{'x': 10, 'y': 12}	
]
bricks = [
	{'x': 8, 'val': 9},
	{'x': 5, 'val': 9},
	{'x': 2, 'val': 9},
]