import time

grid_shape = (1024,1024)

@profile
def evolve(grid, dt, out, D=1.0):
	xmax, ymax = grid_shape
	for i in range(xmax):
		for j in range(ymax):
			grid_xx = grid[(i+1)%xmax][j] + grid[(i-1)%xmax][j] - 2.0 * grid[i][j]
			grid_yy = grid[i][(j+1)%ymax] + grid[i][(j-1)%xmax] - 2.0 * grid[i][j]
			out[i][j] = grid[i][j] + D * (grid_xx + grid_yy) * dt

def run_experiment(num_iterations):
	# 初期条件を設定
	xmax, ymax = grid_shape
	next_grid = [[0.0,]*ymax for x in range(xmax)]  # 要素数ymaxのlistをxmax個作成
	grid = [[0.0,]*ymax for x in range(xmax)]

	block_low = int(grid_shape[0] * 0.4)
	block_high = int(grid_shape[0] * 0.5)
	for i in range(block_low, block_high):
		for j in range(block_low, block_high):
			grid[i][j] = 0.005

	start = time.time()
	for i in range(num_iterations):
		evolve(grid, 0.1, next_grid)
		grid, next_grid = next_grid, grid
	return time.time() - start

if __name__=='__main__':
	run_experiment(10)