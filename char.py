import requests
from chardetail import char1,char2,char3

r = requests.get(url='http://192.168.1.213/study/media/人口年度数据.txt')
r.encoding = 'gb2312'

arr = r.text.split("#")
arr3 = arr[3]
arr4 = arr[4]
newArr = arr3.split("\n")
newArr2 = arr4.split("\n")
del newArr[0]
del newArr2[0]
newArr.pop()
newArr2.pop()
newArr.extend(newArr2)
List = []
for item in newArr:
    each_item = {
        "Year": int(item.split(",")[0][0:4]),
        "All": int(item.split(",")[1]),
        "Man": int(item.split(",")[2]),
        "Woman": int(item.split(",")[3]),
        "City": int(item.split(",")[4]),
        "Village": int(item.split(",")[5])
    }
    List.append(each_item)
# 按照Year升序
newList = sorted(List, key=lambda i: i['Year'])
year=[]
alls=[]
man=[]
woman=[]
city=[]
country=[]
people=[] #男女比例
area=[] #城乡人口比例
for detail in newList:
    year.append(detail["Year"])
    alls.append(detail["All"])
    man.append(detail["Man"])
    woman.append(detail["Woman"])
    city.append(detail["City"])
    country.append(detail["Village"])
    people.append(detail["Man"]/detail["Woman"])
    area.append(detail["City"]/detail["Village"])
man2016=man[-1]
woman2016=woman[-1]
city2016=city[-1]
village2016=country[-1]
#绘图
char1(year,alls)
char2(year,people,area)
char3("2016年男女比例饼状图",['female','male'],[woman2016,man2016])
char3("2016年城乡人口比例的饼状图",['city','country'],[city2016,village2016])