def binalize_image(im_array):
	import sys
	import serial
	import numpy as np

	width = im_array.shape[1]
	height = im_array.shape[0]

	# ポートを開く
	port = serial.Serial("COM7", 115200)

	# 画像を一次元配列化
	raveled = np.ravel(im_array)

	# 二値化された画像用の配列
	binalized = np.zeros(height * width)

	print("Converting...")
	for i, item in enumerate(raveled):
		# 転送
		port.write(chr(item).encode())

		# 受信
		value = ord(port.read())
		binalized[i] = value

		# 進捗表示
		percent = round(float(i) * 100.0 / float(len(raveled)))
		sys.stdout.write("\r%d%% [%d / %d]" % (percent, i + 1, len(raveled)))
		sys.stdout.flush()
	sys.stdout.write("\n")

	print("Finished!")

	# 二値化された配列を二次元化
	binalized[:] *= 255
	reshaped = np.reshape(binalized, (height, width))
	return reshaped


def process_image():
	from PIL import Image
	import numpy as np

	path = "logo"
	ext = ".jpg"
	# 画像を読み込み & グレースケール化 & 二次元配列化
	im_array = np.array(Image.open(path + ext).convert("L"), 'f')

	# 全ピクセルを6bit長に
	im_array[:, :] /= 4.0

	binalized = binalize_image(np.uint8(im_array))

	# 配列から画像に変換
	pil_img = Image.fromarray(np.uint8(binalized))
	# 保存
	pil_img.save(path + "_1" + ext)


if __name__ == "__main__":
	process_image()
