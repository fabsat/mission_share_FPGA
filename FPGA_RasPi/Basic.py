def basic():
	import serial

	value1 = input(">>")
	value2 = input(">>")

	# ポートを開く
	port = serial.Serial("COM7", 115200)
	# 転送開始
	port.write((value1 + value2).encode())

	while True:
		print(port.readline())


if __name__ == "__main__":
	basic()
