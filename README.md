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
$ git clone https://github.com/NATSUMETAKAFUMI/robosys2-ROS.git
$ cd ~/catkin_ws
$ catkin_make
$ source ~/.bashrc
$ cd src
$ cd robosys2-ROS
```

ROSのセットアップができたら下記の通り実行してください
```sh
$ cd scripts
$ ls -l time.py
$ chmod +x time.py
$ ls -l time.py
$ rosrun mypkg time.py
```

* プログラム６行目のhours=9の数字の部分を変えると日本以外の時間も調べることができます。 
* 例:hours=8にすると北京の時刻を調べることができる
* 例:hours=-10にするとハワイの時刻を調べることができる  

---

## 実行動画

動画URL:https://youtu.be/XlBzx8qFLNo

YouTubeにあげた実行動画はこちらになります

## ライセンス
[BSD 3-Clause License](https://github.com/NATSUMETAKAFUMI/robosysws2-ROS/blob/main/LICENSE)
