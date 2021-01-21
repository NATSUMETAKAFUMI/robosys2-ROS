# ROSを使ってUNIX時間(秒)を表示してみた

## 動作環境
---
### OS:ubuntu 20.04 server
### ROS:Noetic
---

## 実行方法
ROSのインストール後下記の手順を行ってください(端末1)
```sh
$ cd ~/catkin_ws/src
$ git clone https://github.com/NATSUMETAKAFUMI/robosys2-ROS.git
$ cd ~/catkin_ws
$ catkin_make
$ source ~/.bashrc
$ cd src
$ cd robosys2-ROS
$ cd scripts
$ roscore
```

ROSのセットアップができたら下記の通り実行してください(端末2)
```sh
$ cd ~/catkin_ws/src/robosys2-ROS/scripts
$ chmod +x time_pub.py
$ rosrun robosys2-ROS time_pub.py
```

新しい端末を開いて実行してください(端末3)
```sh
$ cd ~/catkin_ws/src/robosys2-ROS/scripts
$ chmod +x time_sub.py
$ rosrun robosys2-ROS time_sub.py
```

上記の通りに実行できたらトピックから動作確認を行ってください(端末3)
```sh
$ roslaunch robosys2-ROS date.launch
$ rostopic list　←これを入力したときに/time_searchがあればＯＫ
$ rostopic echo /time_search
```

---

## 実行動画

動画URL:https://youtu.be/v9HtUIJiV04

YouTubeにあげた実行動画はこちらになります
※この出力された数値は1970年1月1日午前0時0分0秒からの経過秒数です。

## ライセンス
[BSD 3-Clause License](https://github.com/NATSUMETAKAFUMI/robosysws2-ROS/blob/main/LICENSE)
