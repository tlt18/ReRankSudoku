import Astar
import random
import time
import matplotlib.pyplot as plt
def inverse_number(range_l):
    flag=0
    for ind_s,s in enumerate(range_l):
        if s==0:
            continue
        for t in range_l[ind_s:]:
            if t==0:
                continue
            if t<s:
                flag +=1
    return flag

#超时解
list_range=[7,2,0,6,3,4,1,8,5]
# list_range=[4,7,5,3,6,0,1,8,2]    #09.3
# list_range=[4,2,6,0,8,3,5,7,1]    #70.2
# list_range=[4,0,6,7,3,2,8,1,5]    #34.0

#时间分布
# tim=[]
# list_range=[1,2,3,4,5,6,7,8,0]
# for i in range(1000):
#     print("测试编号:"+str(i))
#     flag=0
#     while True:
#         random.shuffle (list_range)
#         flag=inverse_number(list_range)
#         if flag % 2 ==0:
#             break
#     print("测试编号:"+str(i))
#     print("测试序号"+str(list_range))
#     a=Astar.solution(list_range)
#     print("交换次数"+str(Astar.times()))
#     print("用时:"+str(a))
#     print()
#     tim.append(a)

# plt.hist(tim)
# plt.show()

a=Astar.solution(list_range)
if a!=-1:
    num=0
    while True:
        num +=1
        list_range=Astar.ans()
        if list_range == -1:
            break
        else:
            # time.sleep(0.05)
            print("移动次数",str(num))
            print(list_range[0],list_range[1],list_range[2])
            print(list_range[3],list_range[4],list_range[5])
            print(list_range[6],list_range[7],list_range[8])
            print()