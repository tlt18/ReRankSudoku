# 九宫重排实验报告

<center> 陶乐天 汽83</center>

## 1 作业清单

- 实验报告:实验报告.md

- 可执行文件:main.exe

- 源代码文件夹:源代码

  

## 2 可执行文件说明

<img src=".\fig\image-20201021195546584.png" alt="image-20201021195546584" style="zoom:50%;" />

### 2.1 随机打乱模式

- 点击[随机打乱]，程序生成可解序列，右上方的显示框和拼图会发生改变；
- 点击[A*搜索]，等待，一般2s以内能够完成；
- 点击[效果展示]，拼图会随着设定速度复原，拼图速度设置需要在点击[效果展示]前。

### 2.2 手动打乱模式

- 在右上角输入0-8序列；
- 点击[手动打乱]，程序会检测拼写错误和可解性，可解序列会使拼图打乱；
- 点击[A*搜索]，等待，一般2s以内能够完成；
- 点击[效果展示]，拼图会随着设定速度复原，拼图速度设置需要在点击[效果展示]前。



## 3 算法说明

核心算法在./源代码/Astar.py中，最主要的搜索过程在函数solution()中。

将初始节点放入Open表，每一pop一个状态now_state，访问now_state所有可能的移动方式，如果和移动后的状态和now_state的父状态不一样，就把移动后的状态放入Open表，而后不断从Open表pop状态。

Open表是以f作为优先级的优先级队列，且$$f=given+heuristic$$。

其中given表示初始状态转化为现状态的变换次数，$$heuristic=P+3S$$，P表示当前状态到目标状态对应点坐标的1-范数，S由下面的方法计算得到:

- 九宫中心位不是0，S加1，否则不变；
- 检测当前状态和目标状态九宫外围顺时针序列，遍历任意非0的两个数，若两个数在两个序列中相对顺序相反，S加2，否则不变。



## 4 未响应说明

有的时候可执行文件会未响应(不知道bug在哪里，算法测试正常)，可以直接测试Astar.py。如果需要直接测试某个可行序列，可以在test.py的list_range直接输入序列，直接观察算法效果，避免图像界面的影响。



## 5 操作整理

(这部分和实验报告没有关系)

### 添加素材

```
pyrcc5 -o resource.py resource.qrc
```

其中resource.qrc写入素材路径

```
<!DOCTYPE RCC> 
<RCC version="1.0"> 
<qresource> 
<file alias="material/background">material/background.png</file> 
<file alias="material/result/1">material/result/1.png</file>
<file alias="material/result/2">material/result/2.png</file>
<file alias="material/result/3">material/result/3.png</file>
<file alias="material/result/4">material/result/4.png</file>
<file alias="material/result/5">material/result/5.png</file>
<file alias="material/result/6">material/result/6.png</file>
<file alias="material/result/7">material/result/7.png</file>
<file alias="material/result/8">material/result/8.png</file>
<file alias="material/result/0">material/result/0.png</file>
</qresource> 
</RCC>
```

### UI生成代码

```
pyuic5 -o ReRankSudoku.py ReRankSudoku.ui
```

### 文件打包

```
pyinstaller -F -i favicon.ico main.py Astar.py resource.py ReRankSudoku.py -w
```



