import sys
from support import print_func
from http.server import HTTPServer,BaseHTTPRequestHandler
import json
import pymysql
from functools import reduce
from multiprocessing import Process, Queue
import os, time, random,threading
from datetime import datetime
from collections import namedtuple,deque,Counter
from tkinter import *
import tkinter.messagebox as messagebox
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import asyncio
from aiohttp import web

print_func("import哈哈哈")
for i in sys.argv:
	print(i)

if True:
	print("True")
else:
	print("False")
#String
str="This is a python file"
print(str[0:10])
print(str[0])
print(str[3:])
print(str*2)
print(type(str))
#List
lists = ['abcd', 786 , 2.23, '123', 70.2]
print(lists[1:3])
print(lists[2:])
print(type(lists))
#Tuple
tuple = ('abcd', 786 , 2.23, '123', 70.2)
print(tuple[1:3])
print(tuple[2:])
print(type(tuple))
#Set
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student) # 输出集合，重复的元素被自动去掉
#Dictionary
tinydict = {'name': 'Rossy1','code':1, 'age':24}
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
#迭代器
newlist=[1,2,3,4,5]
it=iter(newlist)
print(next(it)) #1
print(next(it)) #2
print(next(it)) #3
print(next(it)) #4
print(next(it)) #5
#函数
def sum(arg1,arg2):
	total=arg1*arg2
	print(total)
	return total
sum(10,20)
#类
class People:
	def __init__(self, name,age=10):
		self.name=name
		self.age = age
x=People("Rossy1",24)
print(x.name,x.age)

#map
array=[1, 2, 3, 4, 5, 6, 7, 8, 9]
def func_list(x):
	return x*x
newArray=map(func_list,array)
print(list(newArray))
#reduce
def add(x,y):
	return x+y
addArray=reduce(add,array)
print(addArray)
#filter
def is_odd(x):
	return x%2==1
oddArray=filter(is_odd,array)
print(list(oddArray))
#匿名函数，关键字lambda lambda
lambda x:x*x
#读文件
#1
try:
	f=open("123.txt" ,'r', encoding='gbk', errors='ignore')
	print("文件内容：",f.read())
finally:
	if f:
		f.close()
#2
with open("123.txt","r") as f:
	print(f.read())
#写文件
#1
f2=open("123.txt","w")
f2.write("this is a hahahha file")
f2.close()
#2
with open("123.txt","w") as f2:
	f2.write("this is a hahahha file")
#操作文件目录
#查看当前目录的绝对路径:
print(os.path.abspath("."))
#创建一个目录:
#os.mkdir('Users')
#删掉一个目录:
#os.rmdir('Users')

#多进程
# def write(q):
# 	print('Process to write: %s' % os.getpid())
# 	for value in ["A","B","C"]:
# 		print('Put %s to queue...' % value)
# 		q.put(value)
# 		# time.sleep(random.random())
# def read(q):
# 	print('Process to read: %s' % os.getpid())
# 	while True:
# 		value=q.get(True)
# 		print("Get %s from queue." % value)
# if __name__=='__main__':
#     #父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     #启动子进程pw，写入:
#     pw.start()
#     #启动子进程pr，读取:
#     pr.start()
#     #等待pw结束:
#     pw.join()
#     #pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

#多线程
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         # time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

#协程
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('Consuming %s...' % n)
#         r = '200 OK'
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('Producing %s...' % n)
#         r = c.send(n)
#         print('Consumer return: %s' % r)
#     c.close()
# c = consumer()
# produce(c)

#时间模块
now=datetime.now()
print("当前时间：",now)
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
stamp=dt.timestamp()
print(stamp)
t = 1429417200.0
print("时间戳转时间:",datetime.fromtimestamp(t))
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print("格式化:",cday)

#collections集合模块
point=namedtuple("Point",["x","y"])
p=point(1,2)
print("collections:",p.x)
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
c = Counter() #统计字符出现的个数
for ch in 'programming':
     c[ch] = c[ch] + 1
print(c)

#图像处理库Pillow
im = Image.open('curry.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

#排序
data=[6,3,1,2,4,5]
# data.sort()
data2=sorted(data)
print(data)
print(data2)
#推导列表
data3=[m*3 for m in data2]
print(data3)
#用集合删除重复项
distances={10,8,11,10,8,"one",7,"two","one"}
newdis=set(distances)
print(newdis)





# async def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     await asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# async def index(request):
#     await asyncio.sleep(0.5)
#     return web.Response(body=b'<h1>Index</h1>')

# async def hello(request):
#     await asyncio.sleep(0.5)
#     text = '<h1>hello, %s!</h1>' % request.match_info['name']
#     return web.Response(body=text.encode('utf-8'))

# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     app.router.add_route('GET', '/hello/{name}', hello)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
#     print('Server started at http://127.0.0.1:8000...')
#     return srv

# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()



# #链接数据库
# db=pymysql.connect(
# 	host="192.168.1.95",
# 	port=3306,
# 	user="root",
# 	passwd="123456",
# 	db="school",
# 	charset="utf8"
# )
# cursor=db.cursor()
# sql = "select * from student"
# cursor.execute(sql)
# results=cursor.fetchall()
# resData=[]
# for row in results:
# 	res={
# 		"id":row[0],
# 		"name":row[1],
# 		"subject":row[2]
# 	}
# 	resData.append(res)
# print("数据：",resData)
# #http.server
# host=("localhost",8888)
# class Resquest(BaseHTTPRequestHandler):
# 	def do_GET(self):
# 		self.send_response(200)
# 		self.send_header("Content-type","application/json")
# 		self.end_headers()
# 		self.wfile.write(json.dumps(resData).encode())
# if __name__ == '__main__':
# 	server=HTTPServer(host,Resquest)
# 	print("Starting server, listen at: %s:%s" % host)
# 	server.serve_forever()
