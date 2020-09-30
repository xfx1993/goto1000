def displayTable( orders):
    """
    :type orders: List[List[str]]
    :rtype: List[List[str]]
    """
    fooditem = dict()
    tableitem = dict()

    for name, tableid, food in orders:
        if tableid not in tableitem:
            tableitem[tableid] = dict()
            tableitem[tableid][food] = 1
            if food not in fooditem:
                fooditem[food] = 1
        else:
            if food not in tableitem[tableid]:
                tableitem[tableid][food] = 1
            else:
                tableitem[tableid][food] += 1
            if food not in fooditem:
                fooditem[food] = 1

    foodlist = [key for key in fooditem.keys()]
    foodlist = sorted(foodlist)
    tableitem_list = [[key, value] for key, value in tableitem.items()]
    tableitem_list.sort(key=lambda x: int(x[0]))
    order_matrix = [['Table'] + foodlist] + [['' for i in range(len(foodlist) + 1)] for j in range(len(tableitem_list))]

    for i in range(1, len(order_matrix)):
        order_matrix[i][0] = str(tableitem_list[i-1][0])
        for j, food in enumerate(foodlist):
            if food in tableitem_list[i-1][1]:
                order_matrix[i][j + 1] = str(tableitem_list[i-1][1][food])
            else:
                order_matrix[i][j + 1] = '0'

    return order_matrix


orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]


print(displayTable( orders))