def tankFactory(tank:"function")->"function":
    def powerTank(*params:tuple,**kvParams:dict):
        tank(*params,**kvParams)
        print("已加装反应装甲")
        print("已加装反导弹装置")
        print("已加装红外干扰仪")
    return powerTank

@tankFactory
def tank(player1:'驾驶员',player2:'装填手',player3:'车长',player4:'炮长'):
    print("这是一个裸奔的坦克")
    print("该坦克有四名成员")

@tankFactory
def mordenTank(player1,player2,player3):
    print("这是一个3成员的现代坦克")

tank("tom","jerry","robot1","robot2")
mordenTank("tom","jerry","robot")
# 这是一个裸奔的坦克
# 该坦克有四名成员
# 已加装反应装甲
# 已加装反导弹装置
# 已加装红外干扰仪
# 这是一个3成员的现代坦克
# 已加装反应装甲
# 已加装反导弹装置
# 已加装红外干扰仪