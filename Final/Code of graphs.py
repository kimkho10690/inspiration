"""
    Code of graphs #inspiration
"""
import pygal
import xlrd
file_location = "All Data.xlsx"
workbook = xlrd.open_workbook(file_location)
list_data = [[], [], []]
data_name = ["Man", "Woman", "Average"]

def graph1():
    """This graph about Alcohol consumption rate by genders"""
    sheet = workbook.sheet_by_index(0)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    for i in range(2, sheet.nrows):
        list_data[0].append((data[i][0], round((data[i][3]/data[i][1])*100, 2)))
        list_data[1].append((data[i][0], round((data[i][4]/data[i][2])*100, 2)))
        list_data[2].append((data[i][0], round(((data[i][3] + data[i][4])/(data[i][1] + data[i][2]))*100, 2)))

    line_graph = pygal.XY()
    line_graph.title = 'อัตราการดื่มเครื่องดื่มแอลกอฮอล์รวม และแยกตามเพศ ระหว่างปี 2544 ถึง 2557'
    line_graph.x_labels = (2544, 2546, 2548, 2550, 2552, 2554, 2556, 2558)
    for i in range(3):
        line_graph.add(data_name[i], list_data[i])
    line_graph.render_to_file('1Alcohol consumption rate by genders between 2001 and 2014.svg')

graph1()

list_data = [[], [], []]

def graph2():
    """This graph about Percentage of regular drinkers among drinkers by genders"""
    sheet = workbook.sheet_by_index(1)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    for i in range(3, sheet.nrows):
        list_data[0].append((data[i][0], round((sum(data[i][j] for j in range(1, 5))/sum(data[i][j] for j in range(1, 6)))*100, 2)))
        list_data[1].append((data[i][0], round((sum(data[i][j] for j in range(6, 10))/sum(data[i][j] for j in range(6, 11)))*100, 2)))
        list_data[2].append((data[i][0], round(((sum(data[i][j] for j in range(1, 10)) - data[i][5])/sum(data[i][j] for j in range(1, 11)))*100, 2)))

    line_graph = pygal.XY()
    line_graph.title = 'สัดส่วนของผู้ที่ดื่มแอลกอฮอล์เป็นประจำรวม และแยกตามเพศ ระหว่างปี 2544 ถึง 2557'
    line_graph.x_labels = (2544, 2546, 2548, 2550, 2552, 2554, 2556, 2558)
    for i in range(3):
        line_graph.add(data_name[i], list_data[i])
    line_graph.render_to_file('2Percentage of regular drinkers among drinkers by genders between 2001 and 2014.svg')

graph2()

list_data = [[], [], [], []]
data_name = ["15-24 years", "25-59 years", "60+ years", "Average"]

def graph3():
    """This graph about Alcohol consumption rate by age groups"""
    sheet = workbook.sheet_by_index(2)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    for i in range(2, sheet.nrows):
        list_data[0].append((data[i][0], round((data[i][1]/data[i][2])*100, 2)))
        list_data[1].append((data[i][0], round((data[i][3]/data[i][4])*100, 2)))
        list_data[2].append((data[i][0], round((data[i][5]/data[i][6])*100, 2)))
        list_data[3].append((data[i][0], round((sum(data[i][j] for j in range(1, 6, 2))/sum(data[i][j] for j in range(2, 7, 2)))*100, 2)))

    line_graph = pygal.XY()
    line_graph.title = 'อัตราการดื่มเครื่องดื่มแอลกอฮอล์รวม และแยกตามกลุ่มอายุ ระหว่างปี 2544 ถึง 2557'
    line_graph.x_labels = (2544, 2546, 2548, 2550, 2552, 2554, 2556, 2558)
    for i in range(4):
        line_graph.add(data_name[i], list_data[i])
    line_graph.render_to_file('3Alcohol consumption rate by age groups between 2001 and 2014.svg')

graph3()

list_data = [[], [], [], []]

def graph4():
    """This graph about Percentage of regular drinkers among drinkers by age groups"""
    sheet = workbook.sheet_by_index(3)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    for i in range(2, sheet.nrows):
        list_data[0].append((data[i][0], round((data[i][1]/data[i][2])*100, 2)))
        list_data[1].append((data[i][0], round((data[i][3]/data[i][4])*100, 2)))
        list_data[2].append((data[i][0], round((data[i][5]/data[i][6])*100, 2)))
        list_data[3].append((data[i][0], round((sum(data[i][j] for j in range(1, 6, 2))/sum(data[i][j] for j in range(2, 7, 2)))*100, 2)))

    line_graph = pygal.XY()
    line_graph.title = 'สัดส่วนของผู้ที่ดื่มแอลกอฮอล์เป็นประจำรวม และแยกตามกลุ่มอายุ ระหว่างปี 2544 ถึง 2557'
    line_graph.x_labels = (2544, 2546, 2548, 2550, 2552, 2554, 2556, 2558)
    for i in range(4):
        line_graph.add(data_name[i], list_data[i])
    line_graph.render_to_file('4Percentage of regular drinkers among drinkers by age groups between 2001 and 2014.svg')

graph4()

list_data = [[], [], [], []]
data_name = ["ดื่มทุกวัน", "3-4 วันต่อสัปดาห์", "1-2 วันต่อสัปดาห์", "ดื่มนานๆครั้ง"]

def graph5():
    """This graph about Classified by frequency of drinking in 2544"""
    sheet = workbook.sheet_by_index(4)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    for i in range(2, 3):
        list_data[0].append(round((data[i][1]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[1].append(round((data[i][3]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[2].append(round((data[i][4]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[3].append(round((data[i][5]/sum(data[i][j] for j in range(1, 6)))*100, 2))

    gauge = pygal.SolidGauge(inner_radius=0.70, title=u'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2544')
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    for i in range(4):
        gauge.add(data_name[i], list_data[i])
    gauge.render_to_file('5Classified by frequency of drinking in 2544.svg')

graph5()

list_data = [[], [], [], []]

def graph6():
    """This graph about Classified by frequency of drinking in 2547"""
    sheet = workbook.sheet_by_index(4)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    for i in range(3, 4):
        list_data[0].append(round((data[i][1]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[1].append(round((data[i][3]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[2].append(round((data[i][4]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[3].append(round((data[i][5]/sum(data[i][j] for j in range(1, 6)))*100, 2))

    gauge = pygal.SolidGauge(inner_radius=0.70, title=u'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2547')
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    for i in range(4):
        gauge.add(data_name[i], list_data[i])
    gauge.render_to_file('6Classified by frequency of drinking in 2547.svg')

graph6()

list_data = [[], [], [], []]

def graph7():
    """This graph about Classified by frequency of drinking in 2550"""
    sheet = workbook.sheet_by_index(4)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    for i in range(4, 5):
        list_data[0].append(round((data[i][1]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[1].append(round((data[i][3]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[2].append(round((data[i][4]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[3].append(round((data[i][5]/sum(data[i][j] for j in range(1, 6)))*100, 2))

    gauge = pygal.SolidGauge(inner_radius=0.70, title=u'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2550')
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    for i in range(4):
        gauge.add(data_name[i], list_data[i])
    gauge.render_to_file('7Classified by frequency of drinking in 2550.svg')

graph7()

list_data = [[], [], [], [], []]
data_name = ["ดื่มทุกวัน", "5-6 วันต่อสัปดาห์", "3-4 วันต่อสัปดาห์", "1-2 วันต่อสัปดาห์", "ดื่มนานๆครั้ง"]

def graph8():
    """This graph about Classified by frequency of drinking in 2554"""
    sheet = workbook.sheet_by_index(4)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    for i in range(4, 5):
        list_data[0].append(round((data[i][1]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[1].append(round((data[i][2]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[2].append(round((data[i][3]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[3].append(round((data[i][4]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[4].append(round((data[i][5]/sum(data[i][j] for j in range(1, 6)))*100, 2))

    gauge = pygal.SolidGauge(inner_radius=0.70, title=u'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2554')
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    for i in range(5):
        gauge.add(data_name[i], list_data[i])
    gauge.render_to_file('8Classified by frequency of drinking in 2554.svg')

graph8()

list_data = [[], [], [], [], []]

def graph9():
    """This graph about Classified by frequency of drinking in 2556"""
    sheet = workbook.sheet_by_index(4)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    for i in range(4, 5):
        list_data[0].append(round((data[i][1]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[1].append(round((data[i][2]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[2].append(round((data[i][3]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[3].append(round((data[i][4]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[4].append(round((data[i][5]/sum(data[i][j] for j in range(1, 6)))*100, 2))

    gauge = pygal.SolidGauge(inner_radius=0.70, title=u'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2556')
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    for i in range(5):
        gauge.add(data_name[i], list_data[i])
    gauge.render_to_file('9Classified by frequency of drinking in 2556.svg')

graph9()

list_data = [[], [], [], [], []]

def graph10():
    """This graph about Classified by frequency of drinking in 2557"""
    sheet = workbook.sheet_by_index(4)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    for i in range(4, 5):
        list_data[0].append(round((data[i][1]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[1].append(round((data[i][2]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[2].append(round((data[i][3]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[3].append(round((data[i][4]/sum(data[i][j] for j in range(1, 6)))*100, 2))
        list_data[4].append(round((data[i][5]/sum(data[i][j] for j in range(1, 6)))*100, 2))

    gauge = pygal.SolidGauge(inner_radius=0.70, title=u'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2557')
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    for i in range(5):
        gauge.add(data_name[i], list_data[i])
    gauge.render_to_file('10Classified by frequency of drinking in 2557.svg')

graph10()

list_data = [[], [], [], [], [], []]
data_name = ["2544", "2547", "2550", "2554", "2556", "2557"]

def graph11():
    """This graph about Compare graph of Classified by frequency of drinking in 2544 - 2557"""
    sheet = workbook.sheet_by_index(4)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    for i in range(2, sheet.nrows):
        for k in range(1, 6):
            list_data[i-2].append({'value': round((data[i][k]/sum(data[i][j] for j in range(1, 6)))*100, 2), 'label': '%.2f%s' %(round((data[i][k]/sum(data[i][j] for j in range(1, 6)))*100, 2), '%')})

    line_chart = pygal.HorizontalBar(print_labels=True, stack_from_top=False)
    line_chart.title = 'เปรียบเทียบรอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2544 - 2557'
    line_chart.x_labels = ["ดื่มทุกวัน", "5-6 วันต่อสัปดาห์", "3-4 วันต่อสัปดาห์", "1-2 วันต่อสัปดาห์", "ดื่มนานๆครั้ง"]
    line_chart.y_labels = map(int, range(0, 71, 10))
    for i in range(6):
        line_chart.add(data_name[i], list_data[i])
    line_chart.render_to_file('11Compare graph of Classified by frequency of drinking in 2544 - 2557.svg')

graph11()

list_data = [[], [], [], []]
data_name = ["2547", "2550", "2554", "2557"]

def graph12():
    """This graph about Compare graph of Classified by type og alcohol in 2544 - 2557"""
    sheet = workbook.sheet_by_index(5)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    for i in range(2, sheet.nrows):
        for k in range(1, 6):
            list_data[i-2].append({'value': round((data[i][k]/sum(data[i][j] for j in range(1, 6)))*100, 2), 'label': '%.2f%s' %(round((data[i][k]/sum(data[i][j] for j in range(1, 6)))*100, 2), '%')})

    line_chart = pygal.HorizontalBar(print_labels=True, stack_from_top=False)
    line_chart.title = 'เปรียบเทียบรอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จำแนกตามประเภทของสุราที่ดื่มบ่อย ปี 2544 - 2557'
    line_chart.x_labels = ['เบียร์', 'สุราแช่พื้นบ้าน (สาโท อุ กระแช่)', 'สุราขาว, สุราสี, สุรากลั่น', 'ไวน์', 'อื่นๆ']
    line_chart.y_labels = map(int, range(0, 61, 10))
    for i in range(4):
        line_chart.add(data_name[i], list_data[i])
    line_chart.render_to_file('12Compare graph of Classified by type og alcohol in 2544 - 2557.svg')

graph12()
