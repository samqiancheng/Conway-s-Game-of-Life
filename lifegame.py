import numpy as np
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
import sys
def check_status(input):
	if input[1,1]:
		#live cell w/ < 2 neighbors dies
		#live cell w/ 2 or 3 lives
		#live cell w/ > 3 dies
		live_cells = np.where(input)[0].size - 1
		if live_cells < 2 or live_cells > 3:
			return False
		else:
			return True
	else:
		if np.where(input)[0].size == 3:
			return True
	return False

def __check_status_tester():
	_grid = np.zeros((3,3)).astype(int)

	_grid[1,1] = 1
	print(check_status(_grid),'False')

	_grid[0,0] = 1
	_grid[0,1] = 1
	print(check_status(_grid),'True')

	_grid[0,2] = 1
	print(check_status(_grid),'True')

	_grid[1,0] = 1
	print(check_status(_grid),'False')

	_grid[1,1] = 0
	print(check_status(_grid),'False')

	_grid[1,0] = 0
	print(check_status(_grid),'True')
	print(_grid)


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("Usage: python lifegame.py grid_size_in_int life_size_in_int")
		quit()
	grid_size=None
	life_size=None
	try:
		grid_size = int(sys.argv[1])
		life_size = int(sys.argv[2])
	except ValueError:
		print("Usage: python lifegame.py grid_size_in_int life_size_in_int")
		quit()

	_env = np.zeros((grid_size + 2, grid_size + 2)).astype(int)
	x = np.random.randint(grid_size,size=life_size)
	y = np.random.randint(grid_size,size=life_size)

	_env[x,y] = 1

	fig = plt.figure(figsize=[7,7])
	ax = fig.add_subplot(111)
	def update():
		while True:
			try:
				mod_x = []
				mod_y = []
				for i in range(0,grid_size):
					for j in range(0,grid_size):
						if _env[i+1,j+1] != check_status(_env[i:i+3,j:j+3]):
							mod_x.append(i+1)
							mod_y.append(j+1)
				while mod_x:
					x = mod_x.pop()
					y = mod_y.pop()
					_env[x,y] = 1 if _env[x,y] == 0 else 0
				x,y = np.where(_env[1:-1,1:-1])
				black_block.set_xdata((y*100/grid_size+1).tolist())
				black_block.set_ydata((x*100/grid_size+1).tolist())
				fig.canvas.draw()
				plt.pause(0.2)
			except KeyboardInterrupt:
				plt.close('all')
				break

	plt.ion()
	plt.axis([0,100,0,100])
	margin = 0.1
	x,y = np.where(_env[1:-1,1:-1])
	markers = ((1-2*margin) * 2.5 * 72 / (grid_size)) ** 2
	plt.axis('off')
	fig.subplots_adjust(margin,margin,1-margin,1-margin,0,0)
	black_block, = ax.plot(y*100/grid_size+1,1+ x*100/grid_size, linestyle='None',color='black',marker='s',ms=markers)
	fig.canvas.draw()
	plt.show(block=False)
	update()