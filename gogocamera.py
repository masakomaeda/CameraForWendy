import time
import picamera
import cv2 as cv
#import numpy as np

fn = 'my_pic'

# カメラ初期化
with picamera.PiCamera() as camera:
	# 解像度の設定
	camera.resolution = (512, 384)
	# 撮影の準備
	camera.start_preview()
	time.sleep(1.5)
  
	# 撮影して指定したファイル名で保存する
	i = 0
	while True:
		# 0.5秒おきに撮影をする
		time.sleep(0.5)
		i += 1
		name = fn + str(i) + '.jpg'
		#撮影
		camera.capture(name)
		# 撮影した写真を読み込む
		#img = cv.imread(name)
		# 結果の画像を表示する
		#cv.imshow('camera', img) err
		# Construct a numpy array from the stream
		#data = np.fromstring(name, dtype=np.uint8)
		# 何かキーが押されるまで待機する
		key = cv.waitKey(1)
		if key != -1:
			break
		if i == 20:
			break
	camera.stop_preview()
	# 表示したウィンドウを閉じる
	cv.destroyAllWindows()
