# CameraForWendy
ウェンディ、私を覚えて！

 - ラズパイ設定
```
sudo raspi-config
```
Use the cursor keys to select and open 「Interfacing Options」, and then select 「Camera」 and follow the prompt to 「enable」 the camera.
https://www.raspberrypi.org/documentation/configuration/camera.m

 - cameraを認識させる
```
sudo apt-get update
sudo apt-get upgrade
vcgencmd get_camera
```
supported=1 detected=1と表示されたら、カメラが認識されている  

 - 写真を撮る
```
sudo raspistill -o @@@@.jpg
```

 - 撮った写真をCUIで見る  
https://iot-plus.net/make/raspi/raspistill-continuous-shooting-displays-on-cui-using-frame-buffer-with-ssh-connection/
