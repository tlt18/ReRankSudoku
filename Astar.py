import heapq
import time

end_default=[1,2,3,
             4,5,6,
             7,8,0]
end=[1,2,3,
    4,5,6,
    7,8,0]
store=[]
#calculate heuristic value
def heuristic(now_state,end):
    P,S=0,0
    #cauculate P
    for ind_s,s in enumerate(now_state.list):
        for ind_t,t in enumerate(end):
            if s == t:
                P=P+abs(ind_s%3-ind_t%3)+abs(ind_s//3-ind_t//3)
                # P=P+((ind_s%3-ind_t%3)**2+(ind_s//3-ind_t//3)**2)**0.5
                break
    #calculate S
    if now_state.list[4]!=0:
        S=S+1
    new_list=[now_state.list[0],now_state.list[1],now_state.list[2],
              now_state.list[5],now_state.list[8],now_state.list[7],
              now_state.list[6],now_state.list[3]]
    stadard_list=[end[0],end[1],end[2],
                  end[5],end[8],end[7],
                  end[6],end[3]]
    for ind_s,s in enumerate(new_list):
        if s==end[4]:
            continue
        for t in new_list[ind_s:]:
            if t==end[4]:
                continue
            origin_ind_s,origin_ind_t=-1,-1
            for n in range(len(stadard_list)):
                if stadard_list[n]==s:
                    origin_ind_s=n
                if stadard_list[n]==t:
                    origin_ind_t=n
                    #及时停止
                if (origin_ind_s!=-1)&(origin_ind_t!=-1):
                    break
            if origin_ind_s>origin_ind_t:
                S=S+2
    return P+3*S

class My_PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0
        self._num=0

    def put(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
        self._num +=1

    def pop(self):
        self._num -=1
        return heapq.heappop(self._queue)[-1]

    def empty(self):
        return True if not self._queue else False

    def len(self):
        return self._num

class state():
    def __init__(self,Qlist,father=None):
        self.list=Qlist
        self.ind_zero=0
        for n in range(len(self.list)):
            if self.list[n]==0:
                self.ind_zero=n
                break        
        if father == None :
           self.father=None
           self.given=1
           self.f=1
        else :
           self.father=father
           self.given=father.given + 1
           self.f=self.given + heuristic(self,end)

    def change_father(self,new_father):
        self.father=new_father
        self.given=new_father.given + 1
        self.f=self.given + heuristic(self,end)

    def transform_up(self):
        new_list=clone_runoob(self.list)
        new_list[self.ind_zero-3]=self.list[self.ind_zero]
        new_list[self.ind_zero]=self.list[self.ind_zero-3]
        return state(new_list,self)


    def transform_down(self):
        new_list=clone_runoob(self.list)
        new_list[self.ind_zero+3]=self.list[self.ind_zero]
        new_list[self.ind_zero]=self.list[self.ind_zero+3]
        return state(new_list,self)

    def transform_left(self):
        new_list=clone_runoob(self.list)
        new_list[self.ind_zero-1]=self.list[self.ind_zero]
        new_list[self.ind_zero]=self.list[self.ind_zero-1]
        return state(new_list,self)

    def transform_right(self):
        new_list=clone_runoob(self.list)
        new_list[self.ind_zero+1]=self.list[self.ind_zero]
        new_list[self.ind_zero]=self.list[self.ind_zero+1]
        return state(new_list,self)

def clone_runoob(li1):
    li_copy = li1[:]
    return li_copy

def solution(start):
    global store
    store=[]
    time_start=time.time()
    Start=state(start)
    Open = My_PriorityQueue()
    Close = []
    Open.put(Start,Start.f)
    End=state(end,None)
    flag=0
    while not Open.empty():
        # print("Open_times=",flag)
        flag+=1
        now_state=Open.pop()
        if now_state.list==end:
            End=now_state
            break
        x=now_state.ind_zero % 3
        y=now_state.ind_zero // 3
        if y>0:
            up=now_state.transform_up()
            if now_state.father == None or up.list != now_state.father.list:
               Open.put(up,up.f)
        if y<2:
            down=now_state.transform_down()
            if now_state.father == None or down.list != now_state.father.list:
               Open.put(down,down.f)
        if x>0:
            left=now_state.transform_left()
            if now_state.father == None or left.list != now_state.father.list:
               Open.put(left,left.f)
        if x<2:
            right=now_state.transform_right()
            if now_state.father == None or right.list != now_state.father.list:
               Open.put(right,right.f)
        Close.append(now_state)
        time_end=time.time()
        # if (time_end-time_start) > 10:
        #     return -1
    print("Open_times=",flag)
    traceback=End
    store.append(traceback.list)
    while traceback.father!=None:
          traceback=traceback.father
          store.append(traceback.list)
    # print('step',len(store))
    time_end=time.time()
    # print('totally cost',time_end-time_start)
    return time_end-time_start

def ans():
    global store
    if store == []:
        return -1
    else:
        last = store[len(store)-1]
        del store[len(store)-1]
        return last

def times():
    global store
    return len(store)
