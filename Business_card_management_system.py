import cards_tools

while True:
    cards_tools.Interface()
    action_str = input("请选择操作：")
    if action_str in ["1", "2", "3"]:
        if action_str == "1":#新增名片
            cards_tools.add()
        elif action_str == "2":#显示所有名片
            cards_tools.show_all()
        elif action_str == "3":#查询名片
            cards_tools.search_card()
    elif action_str == "0":
        print("欢迎下次使用，再见。\n")
        break
    else :
        print("您输入有误，请重新输入！\n")


