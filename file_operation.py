import numpy as np
import matplotlib as matplot
def get_locationData():
    input = open("/Users/liuqirui/PycharmProjects/Commu_software_class/beijingdata.txt")
    # 将文件中数据加载到data数组里
    # input.split('/t')  # 按指定的分界符
    # data = np.loadtxt(input)
    #for line in input:
    #    print(line)
    """
    list=[]
    for line in input:
        list.append(line)
        #这样第一行就是a[0]要取出第一行第二个字
    a=list[0].split('\t')[1]
    print(a)
    """
    # 总行数
    List_row = input.readlines()
    # 原始数据列表list_source,二维列表，第一个维度是行数，第二个维度是列数
    list_source = []
    for i in range(len(List_row)):
        # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
        # column_list = List_row[i].strip().split('\t')  # 每一行split后是一个列表
        column_list = List_row[i].split('\t')
        list_source.append(column_list)  # 加入list_source

    # 将数字数据转换为FLOAT类型，存入list_new
    list_new = []
    list_buildings = []
    list_basestation = []
    for i in range(len(List_row)):  # 行数

        if (list_source[i][1] == ' buildings ') or (list_source[i][1] == 'basestation\n'):
            list_new.append(list_source[i])
        else:
            list_new.append(list(map(float, list_source[i])))
            # for j in range(len(list_source[i])):  # 列数
            # 不能这样写，列表元素只能用APPEND写入
            # list_source[i][j] = float(list_source[i][j])
            # print(list_source[i][j])  # 输出每一项

    """
    print(type(list_new[0][0]), type(list_new[0][1]), type(list_new[0][2]))
    print()
    print(type(list_new[1][0]), type(list_new[1][1]))
    """

    for i in range(len(List_row)):
        if (list_source[i][1] == ' buildings '):
            # 本来的数据构成是' 5\n'前有空格，后有回车，所以掐头去尾，留下来中间的数字，但不能只用第二个数字，因为可能有两位数三位数，
            # 获取多边形的顶点数，第i行下面的point行都是这个多边形的顶点坐标
            point = int(list_source[i][2].strip())
            temp_location = np.zeros((point, 2))
            for j in range(point):
                # j是从0开始的，所以i + 1 + j行开始读取第i行所描述的建筑信息
                temp_location[j, 0] = list_new[i + 1 + j][0]
                temp_location[j, 1] = list_new[i + 1 + j][1]
            list_buildings.append(temp_location)

        elif(list_source[i][1] == 'basestation\n'):
            # 处理基站数据，由于涉及多个属性，因此使用字典数据结构存储
            # 只有一行数据，因此不用判断往下读几行
            temp_basestation = {}
            # list_basestation[0]['x']这样读取数据
            temp_basestation = {'x': list_new[i+1][0], 'y': list_new[i+1][1], 'height':list_new[i+1][2],
                                'power': list_new[i+1][3]}
            list_basestation.append(temp_basestation)
    return list_buildings, list_basestation
