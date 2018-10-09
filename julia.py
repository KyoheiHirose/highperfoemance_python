"""ジュリア集合作成機　PILをつかった画像描写を除く"""
import time
import calculate  # setup.py で設定した名前
from functools import wraps

# 調査する複素空間
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -0.42193

def calc_pure_python(desired_width, max_iterations):
	"""複素数の座標リストzaと、複素数のパラメータリストcsを作り、ジュリア集合を使って表現"""
	x_step = (float(x2 - x1) / float(desired_width))
	y_step = (float(y1 - y2) / float(desired_width))
	x = []
	y = []
	ycoord = y2
	while ycoord > y1:
		y.append(ycoord)
		ycoord += y_step
	xcoord = x1
	while xcoord < x2:
		x.append(xcoord)
		xcoord += x_step

	# 座標リストを作って各点を初期条件にする
	# 初期条件は定数で用意に削除可能なので、必要ならこの関数に
	# 入力値を与えて実生活のシナリオをシミュレーションできる
	zs = []
	cs = []
	for ycoord in y:
		for xcoord in x:
			zs.append(complex(xcoord, ycoord))
			cs.append(complex(c_real, c_imag))

	print('Length of x:', len(x))
	print('Total elements:', len(zs))
	start_time = time.time()
	output = calculate.calculate_z(max_iterations, zs, cs)
	end_time = time.time()
	secs = end_time - start_time
	print('took', secs, 'seconds')

	# 1000^2のグリットを繰り返し上限を300としたときの値
	# と低入力値を使って、微小な間違いを検出するためのもの
	assert sum(output) == 33219980


# def timefn(fn):
# 	"""時間測定のデコレーター"""
# 	@wraps(fn)
# 	def measure_time(*args, **kwargs):
# 		t1 = time.time()
# 		result = fn(*args, **kwargs)
# 		t2 = time.time()
# 		print('@timefn:',fn.__name__, 'took', str(t2-t1), 'seconds')
# 		return result
# 	return measure_time
#
# @timefn
# @profile
# def calculate_z_serial_purepython(maxiter, zs, cs):
# 	"""ジュリア漸化式を用いてoutputリストを計算する"""
# 	output = [0]*len(zs)
# 	for i in range(len(zs)):
# 		n = 0
# 		z = zs[i]
# 		c = cs[i]
# 		while abs(z) < 2 and n < maxiter:
# 			z = z * z + c
# 			n += 1
# 		output[i] = n
# 	return output


if __name__ == "__main__":
	calc_pure_python(desired_width = 1000, max_iterations = 300)