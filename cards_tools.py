# *- coding : utf-8 -*

cards_list = []

def Interface ():
    """首页界面"""
    print("*" * 50)
    print("名片管理系统 V1.0\t")
    print("-" * 50)
    print("1、新增名片")
    print("2、显示所有名片")
    print("3、查询名片\n")
    print("0、退出系统")
    print("*" * 50)

def add():
    """新增名片界面"""
    print("-" * 50)
    print("新增名片")
    print("-" * 50)
    #输入信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ号码：")
    email_str = input("请输入邮箱：")
    #添加
    cards_dict = {"name": name_str,
                  "phone": phone_str,
                  "qq": qq_str,
                  "email": email_str}
    cards_list.append(cards_dict)
    print("添加 %s 的名片成功！" % name_str)
    print("-" * 50)

def show_all():
    """显示所有名片界面"""
    print("-" * 50)
    print("显示所有名片")
    if len(cards_list) == 0:
        print("没有名片，请添加。")
        return 
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name ,end = "\t\t")
    print("")
    print("=" * 50)
    for card in cards_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card["name"], 
                                            card["phone"], 
                                            card["qq"], 
                                            card["email"]))
    print("-" * 50)

def search_card():
    """搜索名片界面"""
    print("-" * 50)
    print("搜索名片")
    print("-" * 50)
    name_str = input("请输入姓名：")
    for name in cards_list:
        if name["name"] == name_str:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (name["name"], 
                                                name["phone"], 
                                                name["qq"], 
                                                name["email"]))
            deal_card(name)
            break
    else:
        print("查无此人")

def deal_card(find_dict):
    """修改和删除名片"""
    while True:
        action_str = input("请选择操作：1、修改  2、删除  0、返回上级菜单：")
        if action_str == "1":
            find_dict["name"] = input_card_info(find_dict["name"] ,input("姓名："))
            find_dict["phone"] = input_card_info(find_dict["phone"] ,input("电话："))
            find_dict["qq"] = input_card_info(find_dict["qq"] ,input("QQ："))
            find_dict["email"] = input_card_info(find_dict["email"] ,input("邮箱："))
            print("修改成功！")
        elif action_str == "2":
            cards_list.remove(find_dict)
            print("删除成功！")
        elif action_str == "0":
            break
        else :
            print("输入有误，请重新输入！")

def input_card_info(dict_value, tip_massage):
    """判断用户输入，有输入返回输入的值，没输入返回原来的值"""
    result_str = tip_massage
    if len(result_str) > 0:
        return result_str
    else :
        return dict_value