#coding:utf-8
import threading
from time import ctime,sleep

'''
transfer English System to Metric System

'''
def music(func):
    for i in range(2):
        print('i was listen %s. %s' %(func,ctime()))
        sleep(1)

def movie(func):
    for i in range(2):
        print('i was the movies %s. %s' %(func,ctime()))
        sleep(5)


threads = []
t1 = threading.Thread(target=music,args=('bixude',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=('wodezhongguoxin',))
threads.append(t2)








if __name__ == '__main__':
    for i in threads:
        i.setDaemon(True)
        i.start()
    i.join()
    print('all over %s' %ctime())

