# -*- coding:utf-8 -*-
import re
s1 = """赵丽颖，1987年10月16日出生于河北省廊坊市，中国内地影视女演员、歌手。\n
2006年，因获得《雅虎搜星》比赛冯小刚组冠军而进入演艺圈 [1]  ；同年，在冯小刚执导的广告片《跪族篇》中担任女主角 [2]  。2011年，因在古装剧《新还珠格格》中饰演晴儿一角而被观众认识 [3]  。2013年，凭借古装剧《陆贞传奇》获得更多关注。2014年10月，在第10届金鹰电视艺术节举办的投票活动中被选为“金鹰女神” [4]  ；12月，凭借都市爱情剧《杉杉来了》获得第5届国剧盛典内地最具人气女演员奖；同年，成立海润传媒赵丽颖工作室。
2015年，主演的仙侠剧《花千骨》打破中国内地周播剧收视纪录 [5]  ，而其个人则凭借该剧先后获得第6届澳门国际电视节金莲花最佳女主角奖、第6届国剧盛典最具收视号召力演员奖、第22届上海电视节白玉兰奖最佳女主角奖提名、第28届中国电视金鹰奖观众喜爱的女演员奖 [6-8]  。2017年，凭借电影《乘风破浪》获得第24届北京大学生电影节最受大学生欢迎女演员奖 [9]  ；同年主演的古装剧《楚乔传》成为中国内地首部在播期间网络播放量突破400亿次的电视剧 [10]  。2018年，主演的都市剧《你和我的倾城时光》播出 [11-12]  。2019年5月，凭借古装剧《知否知否应是绿肥红瘦》获得第25届上海电视节白玉兰奖最佳女演员提名 [13]  。2020年，主演古装武侠剧《有翡》 [14]  。
2020年8月27日，赵丽颖名列《2020福布斯中国名人榜》第7位。 [15-16]
"""

# f1 = re.findall("《.+?》",s1)
# print(f1)
# f2 = re.findall("中国",s1)
# print(f2)
# f3 = re.findall("中.|打.................",s1)
# print(f3)
# f4 = re.findall("[^ 赵]",s1)
# print(f4)
# f5 = re.findall("^[赵200]",s1)
# print(f5)
# f6 = re.findall("^[赵2]","2\n赵\n")
# print(f6)
# f7 = re.findall("[0-9]$","2\n赵\n4\n")
# print(f7)
# f8 = re.findall("^[0-9]*$","24\n")
# print(f8)
# f9 = re.findall("tw*","twhtwwwht")
# print(f9)
# f10 = re.findall("[0-9]+","小明:18,小李:19,李世民:954")
# print(f10)
# f11 = re.findall("[0-9]*","小明:18,小李:19,李世民:954")
# print(f11)
# f12 = re.findall("小[^,]*|李[^,]*"," 1号:小明, 2号:小区, 3号:李世民")
# print(f12)
# s2 = "I am a teacher, The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
# f13 = re.findall("[A-Z]+[^ ,]*",s2)
# print(f13)
# f14 = re.findall("[A-Z][^ ,]*",s2)
# print(f14)
# f15 = re.findall("[A-Z][^ ,]+",s2)
# print(f15)
# f16 = re.findall("-?[0-9]*[^ ]","12 356 -10 -4")
# print(f16)
# f17 = re.findall("-?[0-9]+","12 356 -10 -4")
# print(f17)
# f18 = re.findall("-?[0-9]{2}","12 356 -10 -4")
# print(f18)
# f19 = re.findall("-?[0-9]{1,2}","12 356 -10 -4")
# print(f19)
# f20 = re.findall("-?[0-9]{1,2}","12 356 -10 -4")
# print(f20)
# f21 = re.findall("\d{1,5}","#Mysql:唐 3306,http:80")
# print(f21)
# f22 = re.findall("\D{1,5}","#Mysql:唐 3306,http:80")
# print(f22)
# f23 = re.findall("\w{1,5}","#Mysql:唐 3306,http:80")
# print(f23)
# f24 = re.findall("\W{1,5}","#Mysql:唐 3306,http:80")
# print(f24)
# f25 = re.findall("\s{1,5}","#Mysql:唐 3306,http:\r\n\t\v\f 80")
# print(f25)
# f26 = re.findall("\S{1,5}","#Mysql:唐 3306,http:\r\n\t\v\f 80")
# print(f26)
# f27 = re.findall(r"is\b","This is a test.")
# print(f27)
# f28 = re.findall("-?[0-9.]+","12 -23 4.5 -6.7")
# print(f28)
# f29 = re.findall("-?\d+\.?\d*","12 -23 4.5 -6.7")
# print(f29)
# f30 = re.findall("\$\d+","日薪:$100")
# print(f30)
# f31 = re.findall("\$\d+","tigg@shou.com www")
# print(f31)

def fin(r,s):
    print(re.findall(r,s))

def ser(r,s):
    s = re.search(r,s)
    print(s.group())

# fin(r"\w*@\w*\.com$\b"," tigg@shou.com.cn , tan@163.com")
# fin(r"\w+@\w+\.com$"," tigg@shou.com.cn , tan@163.com")
# fin(r"\w{8,12}","13908865156 tang_wei_hua")
# fin(r"-?\d+\.?/?%?\d*"," 1 2.1 -4.3 51% 1/2 -3/4 tang")
# fin(r"-?\d+[\.%/]*\d*"," 1 2.1 -4.3 51% 1/2 -3/4 tang")
# fin(r"\b[A-Z]+[a-z]*","I am Hello iPython Twh TDF")
# fin(r"wo{3,6}?","woooooooow")
# fin(r"《.+?》",s1)
# ser(r"(ab)+","abababa")
# ser(r"(王|花)+\w{1,3}","王伟 高洪汲 李假 花午")
# ser(r"\w+@\w+(\.com(\.cn)*|\.cn)\b"," tigg@shou.com.cn , tan@163.com")
# ser(r"","")
# ser(r"","")

# reobj = re.compile(r"(\w+):(\w+):(\w+)")
# fobj = reobj.findall("Alex:1997:1,Sunny:1996:2,Mark20113",0,23)
#
# print(fobj,reobj)

# s = "热烈庆祝达内17周年，2020年至今,学生６０万"
# pattern1 = r"\w+"
# pattern2 = r"[0]+"
#
# it1 = re.finditer(pattern1,s)
# print(it1)
# for i in it1:
#     print(i)
#
# it2 = re.finditer(pattern2,s)
# print(it2)
# for i in it2:
#     print(i)
#
# print(re.fullmatch(pattern1,s))
# print(re.findall(pattern1,s))
# print(re.findall(pattern2,s))
# print(re.match(pattern1,s))
# pattern_object = re.compile(r"(ab)cd(?P<pig>pog)(?P<dog>de)(r)",flags=re.A)
# print(pattern_object)
# print(pattern_object.pattern)
# print(pattern_object.groups)
# print(pattern_object.groupindex)
# match_object = pattern_object.search("ssabcdpogder",1,13)
# print(match_object.pos)
# print(match_object.endpos)
# print(match_object.re)
# print(match_object.string)
# print(match_object.lastgroup)
# print(match_object.lastindex)
# print(match_object.span())
# print(match_object.start())
# print(match_object.end())
# print(match_object.groupdict())
# print(match_object.groups())
# print(match_object.group())

# pattern = r"(ab)cd(?P<pig>\w{1,3})"
# regex = re.compile(pattern)
# obj = regex.search("0123abcdefghi")
# print(obj)
# print(obj.pos,obj.endpos,obj.re,obj.string,obj.lastgroup,obj.lastindex)
# print(obj.span(),obj.start(),obj.end(),obj.groupdict(),obj.groups())
# print(obj.group(),obj.group(0),obj.group(1),obj.group(2),obj.group("pig"))
# print(obj.group(0,1,2,1))
# print(obj.group(0,1,2,1,"pig"))
# print(re.A,re.I,re.M,re.DEBUG,re.DOTALL,re.LOCALE)

# s = """Hello
# 北京
# """
# regex = re.compile(r"o$",flags=re.M)
# l = regex.findall(s)
# print(l)

def get_address(f):

    port = input("端口:")
    while True:
        data = ""
        for line in f:
            if line == "\n":
                break
            data += line
        obj = re.match(r"\S+",data)
        if not obj:
            return "port error"
        if obj.group()== port:
            pattern = r"(\d{1,3}\.){3}\d{1,3}/\d+"
            m = re.search(pattern,data)
            if m:
                return m.group()
            else:
                return None




if __name__ == '__main__':
    f = open("exc.txt")
    print(get_address(f))

    print(re.search(r"\d{3}$",'123\n').group())
    print(re.search(r"\d{3}\Z",'123').group())

