import matplotlib.pyplot as plt

# 1949-2016年人口总人数的折线图
def char1(year,alls):
    plt.rcParams['font.sans-serif']='SimHei' #设置中文显示
    plt.figure(figsize=(11, 7)) #设置画布大小
    plt.title("Total population") #标题
    plt.plot(year, alls,marker='o',markersize=3) #数据
    plt.xlabel('year') #横坐标
    plt.ylabel('population size') #纵坐标
    plt.show()
#1949-2016年男女比例曲线图和城乡人口比例曲线图
def char2(year,people,area):
    plt.figure(figsize=(11, 7))
    plt.title("women and percent of the country's population")
    plt.plot(year, people,label="women",color='r',markerfacecolor='r',marker='o',markersize=3)
    plt.plot(year, area,label="city's population",marker='o',markersize=3)
    plt.xlabel('year')
    plt.ylabel('percent')
    plt.legend()
    plt.show()
#2016饼状图
def char3(title,label,values):
    plt.rcParams['font.sans-serif']='SimHei' #设置中文显示
    plt.figure(figsize=(7, 7))
    plt.title(title)
    plt.pie(values,labels=label,startangle=90,shadow=3,autopct='%1.1f%%') #绘制饼图
    plt.show()
