# 总目录

<details>
<summary>示例</summary>

- 目录 [toc]  
- 返回 <a href="#总目录"> 返回总目录 </a>
- 分行 <br/>
- 直来直去
```
graph LR
A>函数]
B(参数)
C(返回)
A --- B
B -.-> C

```
***
- 一分为二

```
graph LR
A(函数)
B{参数}
C((T返回))
D[F返回]
A ==> B
B -->|Trun| C
B -->|False|D
```

- 序列图
```
sequenceDiagram
loop every day
Alice->>John: Hello John,how are you?
John->>Alice: Great!
end
```
- 甘特图
```
gantt
dateFormat  YYYY-MM-DD  
title 产品计划表
section 初期阶段
明确需求: 2016-03-01,10d
section 中期阶段
跟进开发:2016-03-11,15d
section 后期阶段
走查测试:2016-03-20,9d
```
***
- 表格
使用 | 来分隔不同的单元格，使用 - 来分隔表头和其他行(分隔线:-左对齐,-:右对齐,:-:中对齐)。  

| 姓名 | 年龄 |                             身高 |
| :--- | :--: | -------------------------------: |
| t    |  1   | 1. one<br />2. two<br />3. three |
***

- 事务清单

- [ ] 已完成项目1
- - [ ] 已完成事项1
- - [x] 已完成事项2
- [ ] 待办事项

***
</details>









# 数据类型
##  数据的种类
| 数据类型 | 不可变                 | 可变         |
| -------- | ---------------------- | ------------ |
| 数值     | int<br/>folat<br/>bool |              |
| 字符     | chr                    |              |
| 序列容器 | str<br/>tuple          | list         |
| 散列容器 | frozenset              | dict<br/>set |

可变对象是指可以在其ID()保持固定的情况改变其取值

## 容器
| 类型     | dict | list  |
| -------- | ---- | ----- |
| 可变否   | 可变 | 可变  |
| 获值     | key  | index |
| 增删速度 | 快   | 一般  |
| 有序否   | 无序 | 有序  |
| 切片否   | 不可 | 可    |

- 常用容器str,tuple,list,set,frozenset,dict,
- set是只有key的字典
- frozenset是一个不能变的集合
- tuple是不可变的列表
- 容器的常用属性: 不可变(含散列)|可变;迭代;
- 容器能运算:iter,len(),max(),min(),sum(),enumerate()
- 容量判断:<,<=,>,>=,==,!=,in,not_in
- 序列容器(str,tuple,list)可进行运算: +拼接,+=,\*重复,\*=,index,slice   - 散列容器不行(dict,set)
- 切片获取数据时创建新列表浅拷贝元素;切片修改数据时(定位用)在原列表地址上改不创建新列表


### 创建

| 类型  | 形式创建(空) |        函数创建 |
| :---- | :----------: | --------------: |
| list  |      []      |      list(iter) |
| tuple |      ()      |     tuple(iter) |
| str   |      ""      |           str() |
| dict  |      {}      | dict(iter(k:v)) |
| set   |              |       set(iter) |

#### 语法变形
- 推导式 以for iter为基础,以if为条件,iter返回元素,以外框区别
- 条件表达式 以if_else分别返回True值及Flase值
- 选择使用函数写法,便于协同,多用于为他人提供功能
- 选择使用推导式|表达式,便于随用随写,多用于为自已提供功能


<details>
<summary>推导式及条件表达式代码</summary>

```python
列表推导式
list01 = [1,4,66,78,9]
list02 = []
"1:for item in list01:"
    "2:if item >= 10"
        list02.append("3:item+1")
list02 = ["3:item+1" 
          "1:for item in list01" 
          "2:if item >= 10"]

l1 = list(range(10))
l2 = list(range(10,21))
l3 = []
for i in l1:
    if i%2:
        for j in l2:
            if j%2 ==0:
                l3.append((i,j))
print(l3)
l4 = [(i,j) 
      for i in range(10) 
      for j in range(10,21) 
      if i%2 and j%2==0]
print(l4)

生成器表达式-->generator

l4 = ((i,j)
      for i in range(10)
      for j in range(10,21)
      if i%2 and j%2==0 )
for i in l4:

字典推导式

a= {i:i**2 
    for i in range(10) 
    if i %2 }
a={1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

a = set()
for i in range(10):
    if i%2:
        a.add(i**2)
a = { i**2
      for i in range(10)
      if i%2}

三目运算符-条件表达式
a=1
"1:if a%2:"
    "2:b = '奇数'"
"3:else:
    b= '偶数'"
b =2:"奇数" 1:if a%2 3:else "偶数"
```

</details>


###  添加 赋值 修改
- str.replace(old, new [, max])以旧换新N次  
- str.lstrip() 删左str或空格  
- str.rstrip() 右  
- str.strip([chars])左右 
- str.replace("old","new")-->用新换旧
- list.append(item) -->添加一个元素 str不会分解
- list.extend(iter) -->添加可迭代对象 str会分解
- list.insert(0,"x")-->插入元素
- dict.update(new_dict)-->更新或新增key:value key要可哈希
- set.update(iter) -->更新可哈希迭代对象 str会分解
- set.add(item) -->更新一个可哈希元素  str不会分解
list[index] = "x" 不可对不存在的索引赋值  
dict[key] = "value" 可对不存在的K赋值
***
-可变对象的id不变,不可变对像赋值会改变id,只有可变容器对象才谈变不变地址



### 查找

#### 返回值
- list[index]
- dict.get(key,default=None)-->T value |F defalue
- dict.setdefault(key,default=None)  -->T value |F add key:defalue
- dict.keys() -->key iter
- dict.values() -->value iter
- dict.items()-->(key,value) iter


####  iter 遍历 for item in ite
| for item         | in items:        |
| ---------------- | ---------------- |
| list[index]      | list:            |
| index            | range(len(list)) |
| tuple[index]     | tuple:           |
| str[index]       | str:             |
| item             | set:             |
| key              | dict:            |
| key              | dict.keys():     |
| value            | dict.values():   |
| tuple(key,value) | dict.items():    |
| key,value        | dict.items():    |

#### 嵌套iter
- for item1 in items1 for item2 in items2 内item2一圈 外item1 一次
for嵌套思路大多从内向外写,赋值也是先写求值表达式
- d = {"A":{a:[1,2]}} 使用d["A"] 等同筛选
- l = [[1,2],[3,4]] 二维列表以行为外层元素,同xls表 可用l[行号]筛选取出行数据,用l[index][列号]取出列数据

#### 返回索引
- list.index(value)-->False ValueError
- str.index(value)-->False ValueError
- str.find(str, beg=0 end=len(string)) 返回索引,无则-1   
- str.rfind(str, beg=0,end=len(string)) 从右找 

### 删除
- 列表的元素删除后,后面的元素用改变索引对象向前移,可使用倒序删除列表元素,range(len-1,-1,-1)

#### 按索引
- del(list[:]) del dict[key]
- List.pop([index=-1])删除索引，默认最后，返回删除元素的引用关系
- dict.pop(key) 返回value并删除与key的联系
- dict.popitem() 删除Key:value,一般是最后,返回删除的key:value
- 
#### 按值
- list.remove(value)-->False ValueError
- set.remove(value) -->False KeyError
- set.discard(value) -->False 不报错

### 清空
list.clear() 清空列表,等同于 L[:] = [] 
dict.clear() 清空字典

### 排序
- list.reverse()-->列表索引逆序
- list.sort(reverse=False)-->列表原地排序
- sorted(iter,reverse=False)-->返回排序列表

### 统计
- list.count(v) 统计次数 
- str.count(str, beg= 0,end=len(string))现N次无则0  

### 大max 小min 和sum
- max(iter)
- min(iter)
- sum(iter)

### 集合运算
- set1.union(set2)  |set1&set2 -->交集,两集合共同部分(相交)
- set1.intersection(set2) |set1|ste2 -->并集,两集合汇总(合并)
- set1.difference(set2) |set1-ste2 -->差集,剔除set2影响的只属于set1的集合
- set1.symmetric_difference(set2)  |set1^ste2 -->补集,剔除交集影响的分属于set1和set2的集合,与交集合并等于并集;也等于(set1-set2|set2-set1)
- 

### 转码
- ord(str)-->unicode  转代码  
- chr(int)-->str      转文字

### 大小写
- str.lower() 转小写  
- str.upper() 转大写  
- str.swapcase()大小写互换

### 字符串拼接与拆分
- str = "连接符".join(iter_chr)  
- list = str.split("分隔符")

### 判断
- str.isspace() 全空吗  
- str.startswith(substr, beg=0,end=len(string))  开头是这 
- str.endswith(suffix, beg=0, end=len(string))  结尾是这
- set1.issuperset(set2) | set1>set2 set2是set1的子集吗
- set1.issuperset(set2) | set1<set2 set2是set1的超集吗
- set1 == set2| set1 != set2|ste1 <= ste2|ste1 >= ste2

### 成员判断 in not_in
- chr in "str"
- item in list
- item in tuple
- item in dict
- item in set


### 二维数据容器

- 行key列key索引表  
K11-键->K1-->主键,主键的数据是否要加入子字典?  
建议加入,上层键的选择是对下层数据的抽象索引

| 字典 | 子典1   | 子典2   |
| ---- | ------- | ------- |
| k1   | k11:v11 | k12:v12 |
| K2   | k21:v21 | k22:v22 |

- 行key列index索引表

| 字典 | 列表1   | 列表2   |
| ---- | ------- | ------- |
| k1   | 0-->v11 | 1-->v12 |
| K2   | 0-->v21 | 1-->v22 |

- 行index列key索引的表

| 列表 | 字典1   | 字典2   |
| ---- | ------- | ------- |
| 0--> | k11:v11 | k12:v12 |
| 1--> | k21:v21 | k22:v22 |

- 行index列index索引 [行][列]式

| 列表 | 子列表1 | 子列表2 |
| ---- | ------- | ------- |
| 0--> | 0-->v11 | 1-->v12 |
| 1--> | 0-->v21 | 1-->v22 |

可以通过zip(*list)快速让行列互换
```python
list01 = [
    [0,1,2,3,4],
    [1,28,45,6,7],
    [20,7,3,65,2]
          ]
a = zip(*list01)

list06 = []
for column in range(len(list01[0])):
    list06.append([])
    for row in range(len(list01)):
        list06[column].append(list01[row][column])
print(list06)

# 正方形原地转换
for row in range(len(game_map)):
    for column in range(row+1,len(game_map)):
        game_map[row][column],game_map[column][row]=game_map[column][row],game_map[row][column]

```

### 元素打包 解包  
-  a,*b,c = iter -->*b[] 赋值右侧 pack -->tuple() 赋值左侧 unpack --> *list[]  使用列表接收任意数量的未匹配元素,右边可以是任何可迭代对象(list,tuple,set,dict,range,zip等)
 可迭代元素为(iter1),(iter2),只生成一次
- enumerate(iter) -->返回一个(iter_index,item)元组
- zip函数   
- - zip(iter1,iter2)-->class zip 生成可迭代元素为(item_iter1,item_iter2)
- - zip(*zip)-->将zip类型解包,生成class zip
- 函数参数  
- - para_ment定义形参时使用\*args将传入元素打包为元组数据,\**kwargs将传入的关键字参数打包为字典数据
- - argu_ment传递参数时,使用\*iter按序列解包为位置参数,\**dict将字典解包为关键字参数


### 序列容器 索引index  切片 slice 范围range

- 索引是元素前的位置标识   从0开始到len减1结束   负索引从负1标识最后一个元素到负len标识第一元素 

- 索引 iter[index]
- 切片 iter[ [start=0] : [end=len] [:setp=1] ]
- 范围 range([start=0,] end [,setp=1])
## 特殊位置
- 头[0],[-len]
- 全序列
- - 正[ : ]
- - 倒[ : :-1],(len-1,-1,-1)
- 尾[-1],[len-1]
- 去尾[ :-1]
- 去头尾[1:-1]
- 不改变对象反向接受列表name[::-1]=list
### 切片
-  是块更新
-  对可变对象的赋值(看引用改变在哪一级)  
- -  变量名重赋值变ID
- - 变量名复合赋值*=,+=是重新绑定原ID;对实例及类变量来说,会创建指向同ID的别名name
- - 对切片赋值不改变ID a[::-1]=iter可倒着反向接受序列,但只能接受原列表len()的值,a[::]=iter[::-1]可接受任意len()反序的值
- - 切片本身是新的对象 =a[:]
``` python
a = ["a","b","c","d"]
a[0:3]= [0,1]
print(a)
>>>[0, 1, 'd']
```

### 赋值= 切片[:] 深拷贝copy.deepcopy(list)
- 赋值会指向同一对象
- 切片会新建根对象,但子对象的会指向同一对象 同copy
- 深拷贝会创建全新引用,复制整个依赖的变量
### range与切片
- rannge支持正负结合的范围和步长(S环,最多两次全序列),如range(2:,-2,-1)-->[2,1,0,-1];range(-2,2,1)-->[-2,-1,0,1],索引不能大于等于len,小于-len
- 切片不支持(S环,最多一次全序列) ,但切片的索引支持大于等于len,小于-len
切片正负结合先定位位置,再定位方向
- a[index]=list 会把list只作为一个元素,a[0:0]=list 把list作为列表插入到首位,列表作为可变类型是有预留空间允许扩展
- 值上切片换新对象,对切片赋值不变对象

``` python
a=[1,2,3,4]
for i in range(-4,4,1):
    print(i,a[i])
>>>-4:1,-3:2,-2:3,-1:4,0:1,1:2,2:3,3:4
print(a[-8:8:1])
>>>[1, 2, 3, 4]
for j in range(3,-5,-1):
    print(j,a[j])
>>>3:4,2:3,1:2,0:1,-1:4,-2:3,-3:2,-4:1
print(a[8:-8:-1])   
>>>[4, 3, 2, 1]
```




# 格式化
## F"格式化字符串
f-string采用 {content:format} 设置字符串格式
其中 content 是替换并填入字符串的内容，可以是变量、表达式或函数等，format 是格式描述符。采用默认格式时不必指定 {:format}  
<左对齐（默认）>右对齐（数值默认）^居中   
0width整数width 指定宽度，开头的 0 指定高位用 0 补足宽度  
width.precision	整数 width 指定宽度，整数 precision 指定显示精度  
width.precision 用于不同格式类型的浮点数、复数时的含义也不同：用于 f、F、e、E 和 % 时 precision 指定的是小数点后的位数，用于 g 和 G 时 precision 指定的是有效数字位数（小数点前位数+小数点后位数）  
, 或 _，则f-string不使用任何千位分隔符，此为默认设置。

```
>>> a = 123.456
>>> f'a is {a:8.2f}'
'a is   123.46'
>>> f'a is {a:08.2f}'
'a is 00123.46'
>>> f'a is {a:8.2e}'
'a is 1.23e+02'
>>> f'a is {a:8.2%}'
'a is 12345.60%'
>>> f'a is {a:8.2g}'
'a is  1.2e+02'
```
## format格式
- 支持传入\*列表或\**字典
```python
x={'唐': {'年龄': '43', '性别': '男', '体重': '75'}}
for key,value in x.items():
    print("{}的年龄是{年龄}性别是{性别} 体重是{体重}".format(key,**value))
    list1=[value["年龄"],value["性别"],value["体重"]]
    print("{}的年龄是{}性别是{} 体重是{}".format(key,*list1))
```

# 命名空间 namespace
- 是名字到对象的映射
- 对象的属性集合也是一种命名空间
- 不同命名空间中的名称之间无关

## 属性
- 跟在一个.点号之后的名称都是属性,modname.funcname是一个模块对象的函数属性,此时模块的属性与模块中定义的全局名称正享相同的命名空间
- 属性可以是只读或可写,可写则能对属性赋值并可用del删除
- 在某个命名空间,若相同的标识符出现重用,无论数据类型是什么,标识符将最终与后面的对象绑定

## 生存期
- 内置名称,存在于built_in_s模块,解释器启动时创建,运行中不会删除
- 模块全局命名空间,在模块定义这被读入时创建,持续到解释器退出
- 被解释器的顶层调用执行的语名,从一个脚本文件读取或交互式地读取,被认为是__main__模块调用的一部分,其拥有自己的全局命名空间
- 函数的本地命名空间,在这个函数调用时创建,在函数返回时删除,递归调用都会有它自已的本地命名空间
- 
## 作用域
- 命名空间可直接访问(对名称的非限写引用会尝试在命名空间中查找名称),的python程序的文本区域
- 作用域被静态确定,但动态使用,程序运行时,至少三个命名空间可直接访问

- - loc_al 局部名称 函数内部   
如果不存在生效的glob_al或non_local语名,对名称的赋值总是会进入最内层的作用域   

局部作用域将引用当前函数的局部名称,函数外将引用与全局作用域一致的命名空间(模块的命名空间)  
所有引入新名称的操作都是使用局部作用域  
im_port 语句和函数定义会在局部作用域中绑定模块或函数名称  
loc_al()使用字典记录当前的key:value,可以附在return语句后返回作用域变量

- - en_closing 封闭函数的作用域 函数嵌套 使用non_local声明为非本地变量  
non_local 语句表明特定变量生存于外层作用域并且应当在其中被重新绑定

- - glob_al 全局名称  模板内部 .py  使用 glob_al声明   
声明为全局变量,所有引用和赋值将直接指向,包含模块的全局名称的中间作用域  
在一个模块内定义的函数的全局作用域就是该模块的命名空间,无论该函数从什么地方或以什么别名被调用  
glob_al 语句可被用来表明特定变量生存于全局作用域并且应当在其中被重新绑定
-- 在一个启动的模板中,glob_al是一个模板区域
- - built_in 内置名称 built_in_s.py文件

- 查找顺序 L-E-G-B 作用域是一个相对概念,loc_al与en_closing看在函数的位置
- 下级可以引用上级的不可变对象,但不能重新赋值
- 下级对上级可变对象不改变ID的行为,不会创建新命名空间
- del 语句必须指向名称所在空间,方法要在类的空间中删除
- 类定义将在局部命名空间内放置另一个命名空间
- 实际的名称搜索是在运行时动态完成的
- 赋值不会复制数据,它们只是将名称绑定到对象,删除也是如此,del x会从局部作用域所引用的命名空间中移除对x的绑定

## 透过name看引用
- built_in 启动时就在内存
- glob_al 模板引入时创建module_name;类定义时创建Class_name和global;函数定义时创建function_name,运行时创建global_name;if等条件语句运行时创建global_name
- loc_al 类定义时创建local_name及function_name,并运行非函数语句;函数定义时创建function_name,运行时创建local_name;
- 在一个启动的文件中,global是一个文件对应的namespace,引用模板会显示一个对应的py地址
- del 会切断name---object的联系


***
# 函数 
- 函数第一要务:单一职责
- 关键字 def 引入一个函数 定义。它必须后跟函数名称和带括号的形式参数列表。
- 表示一个功能
- 使用封装的方法
- 代码的可重用性
- 代码的可维护性
- 
## 命名空间
- 函数定义会把函数名引入当前的符号表中,函数名称的值具有解释器将其识别为用户定义函数的类型。这个值可以分配给另一个名称，该名称也可以作为一个函数使用。
- 函数的 执行 会引入一个用于函数局部变量的新符号表。在函数被调用时，实际参数（实参）会被引入被调用函数的本地符号表中,实参是通过 按值调用 传递的（其中 值 始终是对象 引用 而不是对象的值）。当一个函数调用另外一个函数时，将会为该调用创建一个新的本地符号表。
- 函数中所有的变量赋值都将存储在局部符号表中；而变量引用会首先在局部符号表中查找，然后是外层函数的局部符号表，再然后是全局符号表，最后是内置名称的符号表。
- 全局变量和外层函数的变量不能在函数内部直接赋值（除非是在 global 语句中定义的全局变量，或者是在 nonlocal 语句中定义的外层函数的变量），尽管它们可以被引用。

## 函数的静态与动态
- 定义的时候 形参为静态
- 调用的时候 实参为动态 是使用功能时提供的信息

## 传参 argu_ment local{:value}
1. 按位置传入参数
- 可用*接收iter参数,传入时解包为元素,最好用序列,dict现在有创建顺序,set仍是乱序
2. 关键字传入参数 "="
- 可用**接收dict参数,传入时解包为关键字参数,dict中的key需要用''包裹,否则会报未定义
3. 混合传参(位置参数在前-可用列表,后续使用关键字传参-可用字典)

``` python
#位置及关键字传参
def function4(s,t,x,y,z):
    print(s,t,x,y,z)
a = {"z":30,"y":50}
b = "t"
function4(*b,"w",**a,x=100)
>>>t w 100 50 30
def function_05(x,y=100,*args,z=50,t,**kwargs):
function_05(10,20,11,12,13,z=80,a=20,b=30,t=1)
>>>10 20 (11, 12, 13) 80 1 {'a': 20, 'b': 30}
```
```
sequenceDiagram
loop key:value绑定过程
para_ment->loc_al: 1.定义key(位置|*args-打包->tuple|key=default|name|**kwrgs-打包->dict)
argu_ment->>para_ment: 2.传value给key(位置|*iter-解包->item|key=value|**dict-解包->key=value)
para_ment->>loc_al: 3.配对形成key:value--->loc_al space
end
```

## 定义形参 para_ment local{key:}
1. 形参定义顺序:位置形参(普通,元组)-->默认形参-->关键字形参(命名,字典)
2. 位置形参  
- 单星号元组形参 *args用元组接收实参-->将不定数量的实参转化为元组,可用\*将元组拆包,无则是空元组  
- 只使用*表示不接收位置实参,只接收关键字传参
3. 默认形参"="  在不传入实参时,将使用默认值 a=100,设置初值可以为已定义的变量
4. 关键字形参   
- 命名关键字形参 只接收关键字传参
- 双星号字典形参 **kwargs 将传入的关键字转为字典,a=100-->a:100


## 文档字符串
- 第一行
- 
## 函数定义
- 函数名保存的是对应功能代码的地址
- 函数定义不会立即执行
- 定义的思路是先考虑功能,再用函数体包装,再是参数传递
- 所有函数都有返回值,通过return定义在调用位置返回一个可以让调用者用的值,如break跳出循环一样,return也会跳出本级函数,不写系统默认返回None,故函数也是一个数据类型
``` python
def function_name(para_meter):  
   """
   doc_string -->首行用于函数概述,可被代码助手提取.后接空行,再详述
   """
   pass
   
   return -->默认为None
function_name(argu_meter)-->传入实际的参数,替代定义时para_mater进行函数内工作,如同对形参赋值,并动态的决定参数的类型

```
### 函数式编程
- 可以函数名赋值给变量(实现别名绑定),函数就可以通过别名来调用val(),将调用与引用分离(arg:func)--->func()
- 函数可以作为参数传递,将函数作为参数(逻辑)传给别一个函数,目的就是灵活(定义函数不决定逻辑,执行函数才决定逻辑),
- lamdba 能生成一个函数式实参,即用作键函数,随用随删,可以有效的减少耦合度,优雅的使用一个表达式(不支持赋值词句),能提高阅读体验,lamdba 参数 : 返回的表达式
- 自定义工具函数(静态方法)有利于思考,形成自我的数据规则,并有序的重构,支持逻辑移植到多个语言,提取共同点,将函数名作为参数进行调用,  
- python支持闭包,闭包的三个要素:必须有一个内嵌函数,内嵌函数必须使用外部函数中变量,外部函数返值必须是内部函数.外部函数执行完后并不立即释放内存,而是等着内部函数使用外部嵌套变量.调用:变量=外部函数(参数)->变量(参数);闭包保留调用的内存环境,其外部函数的栈桢不销,外部变量能保持状态供多次使用,价值逻辑连续;用途:函数装饰器
- 使用闭包,传入函数为参数,内层闭包增加新功能并调用旧功能,使用重命名拦截调用(作为参数传入的函数)->可直接写成@嵌套的外部函数->以下面函数为参数增加新功能
- 定义时形参有*为合(把实参合成列表字典),调用时的实参*为分(把传入的元组字典参数分开)
- 函数装饰器如果要新增函数运行时间等,可以先使用一个变量接收函数返回值,最后再用return返回变量
- 多思索函数的单一职责,写小函数,甚至只有一个返回值的函数(贴切的名字便于阅读)







## 内置函数
- def eval(*args, **kwargs): 将一个字符串当成一句Python代码执行,只能执行一行表达式,有返回值的,不能是语句
- def exec(*args, **kwargs):将一个字符串当成一块Python代码执行,可以是语句,每行用分号(或换行符,回车)结束
- 以函数名为参数,条件筛选用筛选filter(func_condition,iterable)->generate,返回属性等用映射map(func_condition,iterable)->generate,查找最大值max(*iterable,key=func_condition)->value,查找最小值min(*iterable,key=func_condition)->value,排序sorted(iterable,key=func_condition,reverse=False)->r:iterable



<details>
<summary>内置函数</summary>

``` python
def print(self, *args, sep=' ', end='\n', file=None): # known special case of print

def input(*args, **kwargs): # real signature unknown
    Read a string from standard input.  The trailing newline is stripped.

class range(object):
    range(stop) -> range object
    range(start, stop[, step]) -> range object


```
***
</details>

# 面对对象 name--->object

- 万物皆对象 合理抽象才能生成有价值的类 object --抽象-->class
- 类也是对象 并且存储开放型数据 可以在外部按名称引用 python的所有内置数据类型都是类
- 类与类之间行为不同,对象与对象之间数据不同 
- 封装:分,继承:隔,多态:做

## 成员
- 类是一个局部空间,但不是对外封闭的空间,函数才是封闭空间
- 类与模板使用的同一数据状态,创建时就可自动执行语句初始化
- 使用类名.成员,总能正确使用,但有硬编码的问题,
- 所谓继承就是一个查找方式,即没有就找上级
- 实例-->类-->父类,数据及方法查找逐级向上 可用self.__class__指代类,super().引用父类方法
- 无论self还是cls都是一个个体概念
- 函数成员是一个用过即灭的栈桢,数据并不保存,对self及cls的修改可视为对其命名空间字典数据修改
- 实例成员(数据\方法)是实例自已的成员,类成员是同类实例共享的成员


## 命名空间字典
- 在一个namespace里最终只会存在一个name,不论是数据还是函数,后定义的后覆盖先定义
- 类定义时即创建namespace
- Class C1.C2 {'__module__': '__main__', '__qualname__': 'C1.C2', 'vc': 2, 'fc': <function C1.C2.fc at 0x00A59CD8>}
- 函数内部必须被执行才会起作用
- Class.function {'self': <__main__.C1.C2 object at 0x00870130>, 'n': 't'} 栈桢
- 实例对象
- init的locals()将创建{'self': <__main__.Wife object at 0x00000000026E3488>, 'x': 1, 'y': 2, 'z': 1, 'args': (2, 3, 4), 'kwargs': {'a': 2, 'b': 3}}等name:object字典-->传给实例很象字典嵌套
- self.__dict__ {'age': 't'}



## 类空间 Class space:

- 可以使用Class_name.__dict__调用命名空间
- 使用类名函数调用类创建实例并传入参数实始化 in_st_ance = Class_name(argu_ment)
- 可以根据__init__构造函数 用argu_ment传参
- 定义使用的是函数方法,可以参照para_ment的形式定义(self|位置参数|*元组|默认|命名|双星字典)


## 类对象
- 类对象支持两种操作 属性引用和实例化
- 属性引用标准语法: obj.name 将分别返回数据或函数对象,类属性可以被赋值
- 类的实例化使用函数表示法 实例化-->构造函数new __init__(self,para_ment)
- 

## 类变量 
- 通过在类代码中赋值实现,不是由__init__创建,不依赖in_st_ance但可被其使用
- 使用Class_name.variable调用,并且可在类代码外修改,不是funct_ion不用加(),也可使用in_st_ance调用-不推荐(查找顺序,先实例\类\父类,但改变对象的赋值会创建出新的实例副本将不再受类变量的影响)
- 可以通过in_st_ance.__class__.variable隐藏类名调用类变量(但只能至本级类,父类仍可能断链),type(instance)等价instance.__class__
- 可用于高效地实现实例变量的默认值,只需创建一个合适默认值的同名变量即可

## 类方法
- 推荐使用@classmethod再定义方法def function(cls): 类变量可使用cls.variable 同in_st_ance.__class__.variable避免硬编码类名
- 类方法不用传入代表实例的self,而是传入代表类的cls,cls也是一个个体
- Class_name.method()可调用方法


## 方法调用 in_voc_ation
- in_st_ance创建完成,可以使用in_st_ance.__dict__方法查看命名空间
- 可使用in_st_ance.met_hod(argu_ment)调用实例方法,也可使用Class_name.met_hod(in_st_ance,argu_ment)调用
- python的方法调用毫无神奇,可看成普通函数调用的简写.先在实例的命名空间查找方法名-->找不到就去找实例所属的类查找方法-->再查找父类;如果找到了方法,就会像普通的python函数一样调用,第一个参数将是in_st_ance,可用self指代,
方法调用中的其他参数则整体向右平移一个位置传入参数,因此in_st_ance.met_hod(arg1,arg2...)就会成为Class.met_hod(in_st_ance,arg1,arg2...)
- 实例方法
-- 定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；
-- 调用：用实例对象调用。instance.method()或Class.methond(instance)
- 类方法
-- 定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；
-- 调用：类对象或实例对象都可以调用。
- 静态方法
-- 定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；静态方法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中，便于使用和维护。
-- 调用：类对象或实例对象都可以调用。


## 继承
- in_st_ance.__class__表示从实例指向类,同type(instance)
- 子类对象调用父类方法，用 super(type, obj).method(arg)方法调用。
- 在子类函数中调用父类方法，可以直接用super().method(arg) 或者 父类名.method(self,arg)
- 所有的方法都是虚方法,如果当前类不存在,则会在父类中逐级搜索,并采用第一个找到的方法
- 变量也可按实例变量-类变量-父类变量查找,但若有对其改变对象引用的行为(=),将在作用域中创建新对象(+=,*=也会新建对象但重新绑定原对象),某个名称的变量在一个作用域只会存在一个,此设计可避免越级修改,
- class Class_sub(Class_super)括号内定义继承的层次结构,
- 子类没有__init__方法时,会引用父类的__init__的方法,但子类有__init__时,需写引用父类的初始化方法,否则对父类定义的数据名使用时会出错,可以使用Class_super_name.__init__()显示引用父类的初始化,可使用super().__init__()传导上级类避免硬编码,但级次复杂了,super是下级对象调用上级函数,self对象是谁调用算谁的数据空间
- 继承可以数据及方法中抽象父类实现化简,从设计的角度是先有子类再有父类,属抽象之再抽象,多个子类在概念上一致时,考虑共性抽象一个父类
- 写代码时父类要靠前
- 不向下级属性查找,实例-->类-->父类
- 使用类.__mro__可显示继承树
- 继承体系可以隔离变化,让父类的同名方法为接口(类似统一名称),可用^o快速找到父类名称,子类同名方法变得多态,父类可以是约束而非具体的行为,让子类重写出多态
- 由于list可以异构,在各子类下同名方法将使用object.mothod,使得多态的时候同一句话有不同的数据结果,这与让父类变成标准化规则是一个不错的选择
- 对于数据,要想共用(可变类数据)还是私有是一个设计思路
- 对于方法,想要继承(向上查找)还是同名(重写^o)也是一个设计思路
- 多重继承按class name(A,B)从左到右一查到object的方式查找同名方法 ,可使用type.MRO() 
- 细分市场,求同存异


### 魔法函数(自object)
- 以双下划线开头并用双下划线结尾,继承自基数object,可使用^o调用重写来实现多态
- init 初始化属性
- 将object->str
- - str 格式随意  
- - repr 返回python格式的字符串并执行,格式要求:可被eval()或exec()执行
- 算术运算符:  (不推荐重载,易造成混乱) 
- - 加add,减sub,乘mul,除truediv,整除floordiv,余mod,幂pow;
- - 反向运算符(在算术运算符前加r)将self与other对调(将对象在后面的时候使用);  
- - 复合运算符(在算术运算符前加i)同+=,-=  可以重新绑定对象
- 基类base,基类等bases,

### 基类
- A.__bases__,返回A类的基类，如果没有基类，返回<class'object'>
- 字符串str, 

## 封装
### 数据角度
- 将一些基础在数据类型复合成一些自定义数据类型, Wife(name,age),封装在一起
- 将数据与数据的操作相关联,数据以对象为意义块,用_init__初始化实例,用.属性引用数据及方法
- 像嵌套字典的升级版 dict[key]-->in_st_ance.met_hod 代码书写/可读性比容器好 更符合人的思维
### 行为角度
- 向类以外提供类型提供必要的功能,并隐藏细节 以基类扩展行为
- 通过对外不使访问,类中可访问的双下划线私有成员,name = property(getter,setter,deleter),@property def name():,@name.setter def name():



### 私有成员
- 通过__双下划线开头确认私有成员,在类外限制访问(可通过实例名._类名私有变量访问),在类中可访问
- 可通过_ClassName__variable,instance.__dict__,及dir()显示
- property() 拦截变量的读写操作 class property(fget=None, fset=None, fdel=None, doc=None) fget 是获取属性值的函数。 fset 是用于设置属性值的函数。 fdel 是用于删除属性值的函数。并且 doc 为属性对象创建文档字符串。 x = property(getx, setx, delx, "I'm the 'x' property.") 如果 c 是 C 的实例，c.x 将调用getter，c.x = value 将调用setter， del c.x 将调用deleter。
- @property 装饰器会将 voltage() 方法转化为一个具有相同名称的只读属性的 "getter"，并将 voltage 的文档字符串设置为 "Get the current voltage." 特征属性对象具有 getter, setter 以及 deleter 方法，它们可用作装饰器来创建该特征属性的副本，并将相应的访问函数设为所装饰的函数。 注意一定要给附加函数与原始的特征属性相同的名称 (在本例中为 x。) 不加@variable.setter就将不允许修改,不加@variable.deleter将不允许删除


```python
    class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```

### 设计角度
- 分而治之 将需求分解为类,分类实现功能 适当划分便于测试,因self.value是共享的,活字替换降低修改成本,功
- 能单一化
- 变则疏之 变化的地方独立封装,避免影响其他类
- 高内聚 类中的各个方法完成一项任务(单一职责的类)
- 低耦合 类与类的关联性与依赖度要低,(每个类独立),让一个类的改变减少影响其他类
- 便于分工 便于复用 可扩展性强
- 分需求,搭结构,再细节

### 类的互动
- 组合(实例变量)  
- - self.methon=Class2()实例就是一个对象,可以实现self.methon.c2methon向下扩展调用  
- 泛化(继承)  
- 依赖(参数)  
- 

### 开闭原则
- 对扩展开放,对修改关闭,即在不改原码的基础上增加新功能
- 一个类就干一件事,一个类有且只有一个改变他的原因
- 依赖倒置,客户端代码(调用的类)尽量依赖(使用)抽象,让细节再抽象为父类变成接口适用多种需求
- 
### 组合复用原则
- 减少继承滥用,实现低耦合
- 继承表示"是一种"传的是一类型,组合表示"有一个"传的是一个实例(建议是父级抽象过的)
- 通过变量(参数/实例变量)调用而不是继承


```
graph LR
A(人类/打电话)
B{通信工具/通信}
C((手机/通信))
D[座机/通信]
A ==>|组合| B
B -->|继承| C
B -->|继承|D
```
组合用来连接变化和不变化的代码,使用实例变量连接  
继承统一所有变化的代码,统一名称用来连接,重写各子类实现多态  

### 里氏替换
- 子类在写父类方法时,尽量选择扩展重写,阻止改变了功能

### 迪米特法则
- 类的交互,不要和陌生人说话,达到功能要求就行,不要多传递数据


## 遍历  

- 可迭代对象iterable（能遍历的对象,并不要求有遍历的方法如__next__）,一般定义了__iter__()方法,可使用iter()返回该对象的迭代器
    - 迭代器iterator()控制遍历的方法  
        - 生成迭代器对象 generator object 有__next__()方法来控制遍历  
            - 生成器函数 generator 使用yield表达式返回值，调用生成的对象有__next__()和__iter__()方法  
- __iter__()的价值:标志对象是可迭代的即可以被for使用,返回一个有迭代方法__next__的对象
- __next__()的价值:返回item|抛出StopIteration异常
- __next__和__iter__可以合写,也可以让__next__分设;有__iter__()的是可迭代对象,有__next__()的是迭代器;__iter__()需要返回一个有__next__()方法的迭代器;函数也可通过yield from去引用yield的专门函数来实现重构;
- object.__iter__()和iter(object)会返回iterable的一个迭代器对象,这个迭代器是一次性的
- 迭代器是循环一次,再计算一次,再返回一次,故相当节省内存
- 迭代器让使用者用一种方法(for存在必要,一招通吃),便可遍历聚合对象,而无需了解数据的结构
- yield在__iter__中步骤:1.调用__iter__()不执行;2.调用__next__()才执行;3.执行到yield语句(返回值)暂时离开;4.再次调用接着上次位置执行; __iter__()中可使用for语句,for item in items: yield item
- yield 的作用:标记;将yield以前的代码放在__next__()方法中;将yield语句求值并作为__next__()方法的返回值
- yield函数的返回值是生成器对象(可迭代对象+迭代器对象),惰性生成(函数调用时并不生成返回值只是创建迭代器),延迟操作(要用数据了才运行第一次到yield)
- yield /jiːld/出产（产品或作物）；产出（效果、收益等）；生息；最大的好处是节约内存
- 当函数只有一个返回值的时候,最佳选择是return而不是yield


``` python
items = [1,2,3]
for item in items:
    print(item)

iterator = items.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
```



# 模块
## 导入
- 导入语句集中靠文件顶部
- import module_name [ as other_module_name] 本质是用symbol(module_name)来保存模块文件的地址,不会引发重名,但对成员的引用需更多的输入  import模块只会导入一次,可执行语句也只会使用一次,可用于初始化,并有效的避免了模块互相导入触发的死循环  
- from module_name import member1,member2 [as other_memdr_name] 从模块文件中导入成员到当前作用域,不会触发模块的可执行语句
- form module_name import * 从模块文件中导入所有非私有成员到当前作用域,可能引发重名,类似重绑对象按就近原则处理  

## 模块变量(magic)
- __all__ 定义可导出成员,仅对from modul import * 语句有效,使用__all__ = [member1,member2]控制导入
- __doc__ 文档字符串(第一个出现的), 可以模块头部用三个引号包裹来表述提示,可用help()显示
- __file__ 对应文件路径名
- __name__ 模块自身名字,为主模块是绑定__main__,被导入是为模块名(无双下划线),可使用if __name__ == __main__: (判断是否在主模块运行,输入 main按Tab选定首选提示)再写可执行语句    
- 一个下划线是私有成员,两个下划线是限制访问,不设定均不用被*的方法导入

## 包
- 将多个模块以文件夹的方式管理 ,文件夹内需有__init__.py与普通文件夹区分,可以__init__.py中设置__all__ = [module1,module2] 设置from package import * 导入本地名称空间的模块(py文件,不能是子包);同时也可设置一些语句,被加载时自动运行
- import pakage.subpakage.module [as other module_name]
- from pakage import module
- alt+enter 选择导入

## 检索路径
- sys.path以列表方式储存检索路径,第一个存储主模板的目录,可以通过sys.path.append(package_path)添加起始点就可以在其它编译工具中使用
- 在文件头加 #! /usr/bin/env python3 可在提示符中直接运行文件
- 

## 内置模块
- sys
- - .path -> [,];第一个存储主模块的目录,可使用.append(x)加上级目录便于查找文件
- - .argv->[,];第一个存储文件地址,第二个开始存储输入的参数,可在文件里用sys.argv[1]接收  
- random  
- - randint(x,y) ->r:x与y间随机int
- - choice(sequence) ->r:随机元素
- - shuffle(list) -> 让list乱序
- time  
- - .time()->r:当前时间戳,以计算机元年(1970-1-1)到现在的总秒数  
- - .localtime(arg)->r:以元组(y,m,d,h...)返回当前时间,可传秒数给arg  
- - .mktime(time_tuple)->r:用元组为参数返回时间戳  
- - .strftime("%Y-%m-%d %H:%M:%s",time_tuple)->r:将元组时间转为字符串  
- - .strptime("200607 15:54:34",'%y%m%d %H:%M:%S')->将字符串转为元组时间
- - .sleep(s) 停止s秒

# 错误  
- SyntaxError 语法错误,多为格式不符



# 异常
## 常见异常
- NameError 名称异常,多为名称未定义  
- TypeError 类型异常,多为运算时不同类  
- IndexError 索引异常,多为超出序列  
- AttributeError 属性异常,多为未定义类下的属性  
- KeyError 键异常,多为没有对应的键  
- NotImplementedError 未实现的异常,多为尚未实现在的方法
- Exception  异常基类,是上述异常的基类
- class MyError(Exception):可以在基类上扩展自定义类,用__init__设定异常内容


## 处理异常  
- 语法(类似if...elif...else)try: 待运行语句 ;except 错误类型1-n: 处理语句1-n;except Exception:其它错语处理语句;else:无异常执行语句;finally:有无异常都执行语句  
- raise 手动抛出异常
- ValueError ("args")->用元组保留提示信息,可用类变量提取ValueError.args

# 内存管理
- 引用计数 如同粉丝量,缺点是僵尸互粉
- 标记清除 分代回收,分块扫描从栈桢看让有用的升代
- 优化: 减少字符串循环+拼接不可变对象会多次生成(用jion拼列表对象),多用对象缓存池(小整数池/字符串池),手动回收(.close方法等,慎重因对内存扫描可能卡顿)





</details>

# 常用单词
<details>
<summary>常用单词</summary>

- row  /rəʊ/ 行
- column /ˈkɒləm/ 列
- character /ˈkærəktə(r)/  字符
- at_tribut_e  /əˈtrɪbjuːt/ 属性    at-朝,tri_but-部落贡品,tri-三,be-存在 
- de_fin_e /dɪˈfaɪn/ vt. 定义  de-加强 fin-限制
- bound /baʊnd/ n. 跳跃；界限，边界；限制，限制范围；界；极限  2.边界，束缚，词源同bind.
- unbound /ʌn'baʊnd/ adj. 解脱束缚的；（印刷品）未装订的；（装订的书）无正式封面的；非结合的；自由的 unbind 解开；解放
- funct_ion  /ˈfʌŋkʃn/ n. 功能；[数] 函数  funct-活动 同perform -ion表名词
- met_hod /ˈmeθəd/ n. 方法；条理；类函数 来自拉丁语methodus,教育方法，来自meta-,在后，-hod,路，词源同anode,cathode,accede.字面意思即跟随，探询，找到，引申词义因材施教。后词义通用化，用以指方法，措施等。
- iter_ate /ˈɪtəreɪt/ vt. 迭代；重复；反复说；重做 iter-重复 -ate表动词
- re_sult /rɪˈzʌlt/ n. 结果；成绩；答案；re-反,向后,往回sult-跳
- re_fer_ence /ˈrefrəns/ vi. 引用 词根词缀： re-回 + -fer-拿取 + -ence名词词尾
- re_cord  /ˈrekɔːd/ n. 记录，记载；唱片；（过去的）经历，履历；纪录，最佳成绩；前科，犯罪记录 词根词缀： re-回 + -cord-心(脏) → 使回到心中 → 记录
- para_meter  /pəˈræmɪtə(r)/ 参数  para-半\类似\辅助 meter-计量\测量
- argu_ment /ˈɑːɡjumənt/ n. 论证；论据 argue辩论 -ment表名词
- element /ˈelɪmənt/ n. 元素；要素；原理；成分；自然环境 来源于拉丁语elementum, elementi, n(本源)。
- re_turn /rɪˈtɜːn/ v. 返回 re-往回\向后\相对 turn转弯\一圈\驱赶
- froze_n /ˈfrəʊzn/ adj. 冻结的；冷酷的 froze冻,-en表形容词
- weak  /wiːk/ adj. [经] 疲软的；虚弱的；无力的；不牢固的
- empt_y  /ˈempti/ adj. 空的；无意义的；无知的；徒劳的 词根词缀： -empt-拿 + -y形容词词尾
- local /ˈləʊkl/ adj. 当地的，地方性的；局部的；局域的；loc-地方,al表形容词
- glob_al  /ˈɡləʊbl/ adj. 全球的；总体的；球形的 glob-球,-al表形容词
- built-in /ˌbɪlt ˈɪn/ adj. 嵌入的；固定的 n. 内置 built 建立建筑,in 在...期间,在...之内
- struct_ure /ˈstrʌktʃə(r)/ n. 结构；构造；建筑物 词根词缀： -struct-建设,结构 + -ure
- mod_ule  /ˈmɒdjuːl/ n. [计] 模块；组件；模数 来自mode,模式，模型，方式，尺度，-ule,小词后缀。即小模型，引申词义模块，单元
- 
- pack_age  /ˈpækɪdʒ/ n. 包，包裹；套装软件，[计] 程序包 pack打包 -age名词
- load_er  /'ləʊdə/ n. 装卸工，装货机；装弹手；载入程序 load负荷\加载 -er...的人或物
- spec /spek/ n. 投机；说明书；细则
- an_not_at_ion /ˌænəˈteɪʃn/ n. 注释；注解；释文 an not -ate -ion
- de_tail 细节详情 de-从...离开,从...向下,tail=cut 剪\割
- sum_m_ary 摘要 sum=add up总结\加,-ary表形容词...的
- while /waɪl/ conj. 在……期间；在……的过程中；与……同时；（对比两件事物）……而；虽然，尽管；直到……为止
- sequ_ence /ˈsiːkwəns/ n. [数][计] 序列；顺序；续发事件 sequ-跟随=follow,-ence n.性质状态
- gener_at_or /ˈdʒenəreɪtə(r)/n. 发电机；发生器；生产者 gener-t出生产生,-ate做造成,-or施动的人或物
- e_numer_ate /ɪˈnjuːməreɪt/ vt. 列举；枚举；计算 e-从...离开,numer=number表数目,-ate表动词做造成
- item /ˈaɪtəm/ n. 条款，项目；一则；一件商品（或物品）
- in_dex  /ˈɪndeks/ n. 指标；指数；索引；指针 in在内,进入,使.. dict-,dic-=say,declare表示说话.断言
- in_st_ance /ˈɪnstəns/ n. 实例；情况；建议 词根词缀： in-向上 + -st-站立,放置 + -ance名词词尾 → 在现场站着的东西
- invocation  /ˌɪnvəˈkeɪʃn/ n. （向神或权威人士的）求助，祈祷；咒语；（仪式或集会开始时的）发言，祷文；（法院对另案的）文件调取；（计算机）调用，启用；（法权的）行使 词根词缀： in-向内 + -voc-声音,叫喊 + -ation名词词尾
- range /reɪndʒ/ n. 范围；幅度；排；山脉
- step /step/ n. 步，脚步；步骤；步伐；梯级
- slice /slaɪs/ vt. 切下；把…分成部分；将…切成薄片
- select  /sɪˈlekt/ v. 选择；（在计算机屏幕上）选定；（从菜单中）选取 词根词缀： se-分离 + -lect-采集
- key_word /ˈkiːwɜːd/ n. 密码；关键字
- string  /strɪŋ/ n. 线，弦，细绳；一串，一行
- break /breɪk/ v. 打破；n. 间断；休息
- raise /reɪz/ vt. 提高；筹集；养育；升起；饲养，种植
- import /ˈɪmpɔːt/ n. 进口，进口货；输入；意思，含义；重要性vt. 输入，进口；含…的意思
- inherit /ɪnˈherɪt/ in-,进入，使，-her,继承，词源同heir,heredity.即使继承，引申词义遗传。
- navigate /ˈnævɪɡeɪt/ v. 导航；航行，驾驶；找到正确的应对方法；词根词缀： -nav-船 + -ig-驾驶,引导 + -ate动词词尾
- name_space /'neimspeis/ n. 命名空间
- field  /fiːld/ n. 领域；牧场；旷野；战场；运动场;字段 词源同plan, plat. 引申词义田野，领域等。
- dict_ion_ary  /ˈdɪkʃənri/ n. 字典；词典 dict-说话 -ion行为动作 -ary 表名词 人.物
- sym_bol  /ˈsɪmbl/n. 象征；符号；标志 sym-,一起，一致，-bol,扔，投掷
- ex_press_ion  /ɪkˈspreʃn/ 表达，表示，措辞
词根词缀： ex-出 + -press-压 + -ion名词词尾
- err_or /ˈerə(r)/ n. 误差；错误；过失 词根词缀： -err-错误 + -or状况,行为
- en_close /ɪnˈkləʊz/ vt. 围绕；装入；放入封套 词根词缀： en-向内 + -clos- 关,闭 + -e动词词尾
- quality  /ˈkwɒləti/ n. 质量，[统计] 品质；特性；才能
- vari_able  /ˈveəriəbl/  adj. 变量的；可变的；易变的，多变的；变异的，[生物] 畸变的 词根词缀： -vari-变化 + -able形容词词尾,被动意义
- proper_ty /ˈprɒpəti/ n. 性质，性能；财产；所有权 来自proper,个人的，-ty,名词后缀。即个人或私人所有的财产或财物。
- single /ˈsɪŋɡl/ adj. 单一的；单身的；单程的 词根-sin-指“一”，-gle词源上是指小后缀
- val_ue /ˈvæljuː/ n. 值；价值；价格；重要性；确切涵义 词根词缀： -val-价值 + ue
- virtual /ˈvɜːtʃuəl/ adj. [计] 虚拟的；实质上的，事实上的 
- public /ˈpʌblɪk/ adj. 公众的；政府的；公用的；公立的 词根词缀： -publ-公众 + -ic形容词词尾
- click  /klɪk/ vt. 点击；使发咔哒声 

***

- view  /vjuː/ n. 观察；视野；意见；风景 视图  -vid-看见 → view被看见的
- control  /kənˈtrəʊl/ n. 控制；管理；抑制；操纵装置 词根词缀： contr-(contra-相反) + rol(=roll滚动) → 阻止滚动
- model /ˈmɒdl/ n. 模型；典型；模范；模特儿；样式 词根词缀： -mod-模式 + -el名词词尾
- expect /ɪkˈspekt/ vt. 期望；指望；认为；预料ex-, 向外。-spect, 看，词源同spectator, telescope. 即向外看，向前看。
- colon  /ˈkəʊlən; ˈkəʊlɒn/  n. [解剖] 结肠；冒号（用于引语、说明、例证等之前）1.冒号，来自PIE*skel, 弯，转，词源同clavicle, scoliosis. 原指分岔，分枝。
- program  /ˈprəʊɡræm/ n. 程序；计划；大纲 词根词缀： pro-前 + -gram-写,画 → 提前写好的内容
- language  /ˈlæŋɡwɪdʒ/  n. 语言；语言文字；表达能力来自拉丁语lingua,舌头，语言，词源同tongue,linguist.
- mechanism /ˈmekənɪzəm/ n. 机制；原理，途径；进程；机械装置；技巧 词根词缀： -mechan-机器,机械 + -ism名词词尾,现象
- minimum /ˈmɪnɪməm/ n. 最小值；最低限度；最小化；最小量 来自拉丁语minimus,最小的，-um,中性格。引申词义最小值，最低限度。
- syntax  /ˈsɪntæks/  n. 语法；句法；有秩序的排列
- mixture  /ˈmɪkstʃə(r)/ n. 混合；混合物；混合剂 来自mix,混合，-t,过去分词后缀，-ure,名词后缀。引申词义混合体。
- standard /ˈstændəd/ n. 标准；水准；旗；度量衡标准 来自古法语 estandart,军旗，旗帜，等同于 stand hard,字面意思即稳固站立。
- feature /ˈfiːtʃə(r)/ n. 特色，特征；容貌；特写或专题节目 词根词缀： -feat-做,作 + -ure名词词尾





***
</details>