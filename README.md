# mml2beep
Converts MML to beep music score. 转换MML乐谱到beep谱

MML(Music Macro Language)是一些在线游戏（如洛奇）的乐谱代码

beep谱指以`[频率, 持续时间]`表示一个音符的乐谱，用于蜂鸣器播放音乐

## 用法
将Python代码中的“改成MML乐谱”换成事先准备好的单音轨乐谱。到代码的这个网址或者最下边的网址粘贴并运行。（直接运行需要安装Python 3）

DOS: 使用```master```分支。将输出结果复制，保存为```TMP.H```，放到```PLAY.CPP```同一目录。用Turbo C++打开```PLAY.CPP```，编译之即可（注意编译前要设置File-Change Directory到CPP的文件夹，不然会找不到粘贴过来的头文件）。

Linux: 使用```linux```分支。需要准备好TCC编译器。将输出结果复制，保存为```tmp.h```，放到```play.c```同一目录。执行```tcc play.c -o 可执行文件名```。然后运行这个可执行文件名即可。

可选参数：

```
  -h, --help            show this help message and exit
  -t TRACK, --track TRACK
                        输出第几个音轨，默认为1
  -f {json,cpp}, --format {json,cpp}
                        输出格式，默认为json
```

## 链接
* [MML语法参考](https://mabinogi.fws.tw/ac_com_annzyral.php)
* [获取MML乐谱](https://mabinogi.fws.tw/ac_comproser.php)
* [在线编译Python 3](https://c.runoob.com/compile/9)
