# ROSを使って日本標準時間を表示してみた

## 動作環境
---
### OS:ubuntu 20.04 server
### ROS:Noetic
---

## 実行方法
ROSのインストール後下記の手順を行ってください
```sh
$ cd ~/catkin_ws/src
$ cd ..
$ catkin_make
$ source ~/.bashrc
$ catkin_create_pkg mypkg rospy
$ cd rospy
$ git clone https://github.com/NATSUMETAKAFUMI/robosys2-ROS.git
```

ROSのセットアップができたら下記の通り実行してください
```sh
$ ls -l time.py
$ chmod +x time.py
$ ls -l time.py
$ rosrun mypkg time.py
```
---

## 実行動画

動画URL:https://youtu.be/XlBzx8qFLNo
YouTubeにあげた実行動画はこちらになります

## ライセンス
[BSD 3-Clause License](https://github.com/NATSUMETAKAFUMI/robosysws2-ROS/blob/main/LICENSE)
