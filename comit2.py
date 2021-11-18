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

# движения пуль и разрушение цифр

def move():
	for b in bullets:
		b['y'] -= bulletsSpeed
		if b['y'] < 1:
			for brick in bricks:
				if b['x'] == brick['x']:
					brick['val'] -= 1
					bullets.remove(b)
					if brick['val'] == 0:
						bricks.remove(brick)
#задаю управление на нажатии клавиш

def press_instruction(key):
	global ship
	if key == pynput.keyboard.KeyCode.from_char('d'):
		ship['x'] += 1
	if ship['x'] <= 0:
		ship['x'] = 0
	if key == pynput.keyboard.KeyCode.from_char('a'):
		ship['x'] -= 1
	if ship['x'] >= 20:
		ship['x'] = 19
	if key == pynput.keyboard.Key.space:
		bullets.append({'x': ship['x'], 'y': height - 1})