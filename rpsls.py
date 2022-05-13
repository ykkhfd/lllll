#第一个小项目:Rock-paper-scissors-lizard-Spock 作者:李妍瑾 日期：5月12日

def name_to_number(name):
    if name=="石头":
        return 0
    elif name=="史波克":
        return 1
    elif name=="纸":
        return 2
    elif name=="蜥蜴":
        return 3
    elif name=="剪刀":
        return 4
    else:
        return "Error：No Correct Name"
def number_to_name(number):
    if number==0:
        return "石头"
    elif number==1:
        return "史波克"
    elif number==2:
        return "纸"
    elif number==3:
        return "蜥蜴"
    elif number==4:
        return "剪刀"
    else:
        return "Error：No Correct Name"


import random
def rpsls(player_choice):
    print("您的选择是",player_choice)
    player_number=name_to_number(player_choice)#利用函数将名字转为数字
    comp_number=random.randrange(0,5)#确定范围
    com_choice=number_to_name(comp_number)#利用函数将数字转为名字
    print("计算机的选择为:%s"%com_choice)
    difference=(player_number-comp_number)%5
    if difference==1 or difference==2:
        print("您赢了")
    elif difference==3 or difference==4:
        print("计算机赢了")
    else:
        print("您和计算机出的一样呢")
        
#对程序进行测试
print("欢迎使用RPSLS游戏")
print("规则是：剪刀裁剪纸；纸包裹石头；石头砸碎剪刀；石头砸死蜥蜴；蜥蜴毒死史波克；剪刀腰斩蜥蜴；蜥蜴吃掉纸；纸反驳史波克；史波克蒸发石头")
print("----------------")
print("请输入您的选择:")
choice=input()
rpsls(choice)
    















