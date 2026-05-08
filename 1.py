# account = input("Enter your account: ")
# password = input("Enter your password: ")   
# if account == "18888888" and password == "123456":
#     print("Login successful!")
# else:
#     print("Login failed!")





# num = input("Enter a number: ")
# if int(num) > 0:
#     print(f"{num} is a positive number.")
# elif int(num) < 0:
#     print(f"{num} is a negative number.")
# else:    print(f"{num} is zero.")

# account = input("Enter your account: ")
# password = input("Enter your password: ")   
# if account == "123" and password == "123":
#     print("Login successful!")
# elif account == "234" and password == "234":
#     print("Login successful!")
# elif account == "345" and password == "345":
#     print("Login successful!")  
# else:
#     print("Login failed!")



# total = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         total += i
# print(f"The sum of numbers from 1 to 100 is: {total}")

# m = int(input("Enter the length of the rectangle: "))
# n = int(input("Enter the width of the rectangle: "))
# for i in range(n):
#     for j in range(m):
#         print("*", end=" ") #内层循环打印星号，end=""表示不换行
#     print()

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} * {i} = {i * j}", end="\t") #内层循环打印乘法表，end="\t"表示用制表符分隔
#     print()

# while True:
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")

#     if username == "" or password == "":
#         print("Username and password cannot be empty. Please try again.")
#     elif username == "admin" and password == "666888":
#         print("Login successful!")
#         break
#     elif username == "zhangsan" and password == "123456":
#         print("Login successful!")
#         break
#     elif username == "taoge" and password == "888666":
#         print("Login successful!")
#         break
#     else:       
#         print("Login failed! Please try again.")
        
    
# import random
# random_number = random.randint(1, 100) #生成一个1到100之间的随机整数


# while True:
#     num = input("Guess a number between 1 and 100: ")
#     if int(num) == random_number:
#         print("Congratulations! You guessed the number!")
#         break
#     elif int(num) < random_number:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")

# print(f"The random number was: {random_number}")

# s = [12,14,151,616,167]
# s[2] = 2 #将索引为2的元素替换为2
# print(s) #输出修改后的列表

# for item in s:
#     print(item) #输出列表中的每个元素

# s.append(100) #在列表末尾添加元素100
# s.insert(1, 50) #在索引为1的位置插入元素50
# s.remove(616) #删除列表中的元素616
# s.pop(3) #删除索引为3的元素
# s.pop() #删除列表中的最后一个元素
# s.sort() #对列表进行排序
# s.sort(reverse=True) #对列表进行降序排序
# s.reverse() #将列表反转
# print(s) #输出修改后的列表

# num_list = []
# for i in range(10):
#     num = int(input("Enter a number: "))
#     num_list.append(num) #将输入的数字添加到列表中
# print(num_list) #输出列表中的所有元素

# num_list.sort() #对列表进行排序
# num_sort = num_list[:5] #取出排序后的前5个元素
# print(num_sort) #输出排序后的前5个元素
# print(num_list[0]) #输出排序后的第一个元素
# print(num_list[-1]) #输出排序后的最后一个元素
# sum_num = sum(num_list) #计算列表中所有元素的和
# average = sum_num / len(num_list) #计算列表中所有元素的平均值
# print(f"The sum of the numbers is: {sum_num}")
# print(f"The average of the numbers is: {average}")

# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# for num in num_list2: #遍历num_list2中的每个元素
#         num_list1.append(num) #将num_list1中的元素添加到num_list1中
#         print("total:" , num_list1) #输出修改后的num_list1列表

# new_list = []
# for num in num_list1: #遍历num_list1中的每个元素
#     if num not in new_list: #如果num不在new_list中
#         new_list.append(num) #将num添加到new_list中

# print("Unique elements:" , new_list) #输出去重后的列表


# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# # 合并列表
# num_list1.extend(num_list2)
# print("total:", num_list1)

# # 去重
# unique_list = list(set(num_list1))
# print("Unique elements:", unique_list)

# generate a list of squares from 0 to 20
# num_list = []
# for i in range(0,21):
#     num_list.append(i**2)
# print(num_list)

# num_list = [12,42,25,63,747,47,86,999,52]
# new_list = [i**2 for i in num_list if i % 2 == 0] #使用列表推导式生成一个新的列表，包含num_list中所有偶数元素
# print(new_list)
# l =len(new_list) #计算新列表的长度
# print(f"The length of the new list is: {l}")

# s = "hello-python"
# print(s[0]) #输出字符串s的第一个字符
# print(s[-1]) #输出字符串s的最后一个字符

# s.find("o") #查找字符串s中第一个出现的字符"o"的位置
# s.count("o") #统计字符串s中字符"o"出现的次数
# s.upper() #将字符串s转换为大写字母
# s.lower() #将字符串s转换为小写字母
# s.replace("o", "0") #将字符串s中的字符"o"替换为字符"0"
# s.split("-") #将字符串s按照"-"分割成一个列表
# s.strip("h") #去掉字符串s开头和结尾的字符"h

# t1 = (5,7,9,10)
# t2 = 12,14,16,1
# a,b,c,d = t1 #将元组t1中的元素分别赋值给变量a、b、c、d
# print(a) #输出变量a的值
# x,*y,z = t2 #将元组t2中的第一个元素赋值给变量x，最后一个元素赋值给变量z，中间的元素赋值给变量y（以列表的形式）
# print(x) #输出变量x的值
# print(y) #输出变量y的值


# for s in students:
#     total = s[2]+ s[3] + s[4] #计算学生的总分
#     avg = total / 3 #计算学生的平均分
#     print(f"{s[0]} {s[1]} Total: {total} Average: {avg:.2f}") #输出学生的姓名、总分和平均分，平均

# chinese_scores = [s[3] for s in students]
# math_scores = [s[4] for s in students]
# english_scores = [s[5] for s in students]
# chinese_avg = sum(chinese_scores) / len(chinese_scores) #计算语文
# chinese_min = min(chinese_scores) #计算语文最低分
# chinese_max = max(chinese_scores) #计算语文最高分
# math_avg = sum(math_scores) / len(math_scores) #计算数学平均分
# math_min = min(math_scores) #计算数学最低分
# math_max = max(math_scores) #计算数学最高分 
# english_avg = sum(english_scores) / len(english_scores) #计算英语平均分
# english_min = min(english_scores) #计算英语最低分
# english_max = max(english_scores) #计算英语最高分
# print(f"Chinese Average: {chinese_avg:.2f} Min: {chinese_min} Max: {chinese_max}") #输出语文平均分、最低分和最高分
# print(f"Math Average: {math_avg:.2f} Min: {math_min} Max: {math_max}") #输出数学平均分、最低分和最高分
# print(f"English Average: {english_avg:.2f} Min: {english_min} Max: {english_max}") #输出英语平均分、最低分和最高分  


# # 选修足球学生名单
# football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# # 选修篮球学生名单
# basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# # 选修法语学生名单
# french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# # 选修艺术学生名单
# art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# s1 = french_set.intersection(art_set) #选修法语和艺术的学生名单
# print(f"选修法语和艺术的学生名单: {s1}")

# all_set = football_set & basketball_set & french_set & art_set #选修足球、篮球、法语和艺术的学生名单
# print(f"选修足球、篮球、法语和艺术的学生名单: {all_set}")

# s2 = football_set.difference(basketball_set) #选修足球但不选修篮球的学生名单
# print(f"选修足球但不选修篮球的学生名单: {s2}")

# all_set = football_set | basketball_set | french_set | art_set #选修足球、篮球、法语或艺术的学生名单
# all_list = [*football_set , *basketball_set , *french_set , *art_set] #将选修足球、篮球、法语或艺术的学生名单合并成一个列表，包含重复的学生姓名
# for s in all_set:
#     print(f"{s} xuanxiule {all_list.count(s)} menke") #输出选修足球、篮球、法语或艺术的学生名单以及他们选修的课程数量 


# d1 = {"wang": 600, "yang": 500, "li": 400} #创建一个字典，包含学生的姓名和成绩

# d1["zhang"] = 700 #向字典d1中添加一个新的键值对
# d1.pop("li") #从字典d1中删除键为"li"的键值对
# del d1["yang"] #从字典d1中删除键为"yang"的键值对
# d1["wang"] = 650 #修改字典d1中键为"wang
# d2 = d1.keys()
# d3 = d1.values()
# print(d1.get("zhang")) #输出字典d1中键为"zhang"的值
# print(d1.items()) #输出字典d1中所有的键值对
# print(d1)
# print(d2)
# print(d3)

# for k in d1.keys():
#     print(f"{k} xuexi le {d1[k]} fenshu") #输出字典d1中每个键及其对应的值


# shopping_cart = {}

# print("Welcome to the shopping cart system!")
# menu = """
# ##### shopping cart system #####
# #            1.add             #
# #            2.modify          #
# #            3.del             #
# #            4.search          #
# #            5.exit            #
# ################################
# """

# while True:
#     print(menu)

#     choice = input("Please enter your choice(1-5): ")
#     match choice:
#         case "1": #添加商品
#             goods_name = input("Please enter the goods name: ")
#             goods_price = float(input("Please enter the goods price: "))
#             goods_num = int(input("Please enter the goods number: "))
#             if goods_name in shopping_cart:
#                 print(f"{goods_name} has been existed in the shopping cart.")
#             else:            
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num} #如果商品不在购物车中，则添加新的键值对
#                 print(f"{goods_name} has been added to the shopping cart.")
#             pass
#         case "2": #修改商品
#             goods_name = input("Please enter the goods name: ")
#             if goods_name not in shopping_cart:
#                print(f"{goods_name} is not in the shopping cart.")
#                continue

#             goods_price = float(input("Please enter the newest goods price: "))
#             goods_num = int(input("Please enter the newest goods number: "))
#             shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print(f"{goods_name} has been updated in the shopping cart.")
            
#             pass
#         case "3": #删除商品
#             goods_name = input("Please enter the goods name: ")
#             if goods_name not in shopping_cart:
#                 print(f"{goods_name} is not in the shopping cart.")
#             else:
#                 del shopping_cart[goods_name]
#                 print(f"{goods_name} has been removed from the shopping cart.")
#             pass
#         case "4": #搜索商品 
#             for goods_name in shopping_cart.keys():
#                 print(f"{goods_name}  {shopping_cart[goods_name]['price']}  {shopping_cart[goods_name]['num']} ") #输出购物车中每个商品的名称、价格和数量
#             pass
#         case "5": #退出
#             print("bye")
#             break
#         case _:
#             print("Invalid choice! Please enter a number between 1 and 5.")




# def reg_stu(name, age, gender="male", city="beijing"):
#     print(f"successfully! Name: {name}, age: {age}, gender: {gender}, city: {city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}

# s1 = reg_stu("zhangsan", 20) #调用函数reg_stu，传入参数name和age，使用默认值gender和city
# print(s1)

# def calc_data(*args, **kwargs):
#     min_data = min(args) #计算args中的最小值
#     max_data = max(args) #计算args中的最大值
#     avg_data = sum(args) / len(args) #计算args中的平均值

#     if kwargs.get("round") is not None: #如果kwargs中有键"round"，则将avg_data四舍五入到指定的小数位数
#         avg_data = round(avg_data, kwargs["round"])
#     if kwargs.get("print"):
#         print(f"Min: {min_data}, Max: {max_data}, Avg: {avg_data}") #如果kwargs中有键"print"，则输出min_data、max_data和avg_data的值
#     return {"min": min_data, "max": max_data, "avg": avg_data} #返回一个字典，包含min、max、avg以及kwargs中的键值对

# print(calc_data(2,8,129.63,76.6,87,round=3)) #调用函数calc_data，传入多个位置参数和关键字参数

# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def calc(x, y, oper):
#     return oper(x, y) #调用oper函数，传入参数x和y

# result = calc(19,5,add)
# print(result) #输出result的值

# data_list =  ["c++", "python", "java", "c#", "javascript"]
# data_list.sort(key=len, reverse=True) #按照字符串长度排序
# print(data_list) #输出排序后的列表

#计算n的阶乘
def jc(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * jc(n - 1) #递归调用函数jc，传入参数n-1，直到n等于0或1时返回1

print(jc(0)) #调用函数jc，传入参数5，输出5的阶乘

from abc import my_fun

my_fun.log_separator1() #调用模块my_fun中的函数log_separator1，输出分隔线

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.") #输出学生的姓名和年龄