import pygal

def graph1():
    pie_chart = pygal.Pie()
    pie_chart.title = 'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2544'
    pie_chart.add('ดื่มนานๆ ครั้ง', [64.87])
    pie_chart.add('ดื่มสม่ำเสมอ', [{'value': 7.96, 'label': 'ดื่มทุกวัน'}, {'value': 9.9, 'label': '3-4 วันต่อสัปดาห์'}, {'value': 17.27, 'label': '1-2 วันต่อสัปดาห์'}])
    pie_chart.render_to_file('Pie chart 2544.svg')
graph1()

def graph2():
    pie_chart = pygal.Pie()
    pie_chart.title = 'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2547'
    pie_chart.add('ดื่มนานๆ ครั้ง', [61.7])
    pie_chart.add('ดื่มสม่ำเสมอ', [{'value': 9.5, 'label': 'ดื่มทุกวัน'}, {'value': 10.2, 'label': '3-4 วันต่อสัปดาห์'}, {'value': 18.6, 'label': '1-2 วันต่อสัปดาห์'}])
    pie_chart.render_to_file('Pie chart 2547.svg')
graph2()

def graph3():
    pie_chart = pygal.Pie()
    pie_chart.title = 'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2550'
    pie_chart.add('ดื่มนานๆ ครั้ง', [59.11])
    pie_chart.add('ดื่มสม่ำเสมอ', [{'value': 12.81, 'label': 'ดื่มทุกวัน'}, {'value': 9, 'label': '3-4 วันต่อสัปดาห์'}, {'value': 19.08, 'label': '1-2 วันต่อสัปดาห์'}])
    pie_chart.render_to_file('Pie chart 2550.svg')
graph3()

def graph4():
    pie_chart = pygal.Pie()
    pie_chart.title = 'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2554'
    pie_chart.add('ดื่มนานๆ ครั้ง', [55.8])
    pie_chart.add('ดื่มสม่ำเสมอ', [{'value': 11.38, 'label': 'ดื่มทุกวัน'}, {'value': 6.87, 'label': '5-6 วันต่อสัปดาห์'}, {'value': 8.85, 'label': '3-4 วันต่อสัปดาห์'}, {'value': 17.1, 'label': '1-2 วันต่อสัปดาห์'}])
    pie_chart.render_to_file('Pie chart 2554.svg')
graph4()

def graph5():
    pie_chart = pygal.Pie()
    pie_chart.title = 'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2556'
    pie_chart.add('ดื่มนานๆ ครั้ง', [58.56])
    pie_chart.add('ดื่มสม่ำเสมอ', [{'value': 9.72, 'label': 'ดื่มทุกวัน'}, {'value': 7.04, 'label': '5-6 วันต่อสัปดาห์'}, {'value': 7.73, 'label': '3-4 วันต่อสัปดาห์'}, {'value': 16.95, 'label': '1-2 วันต่อสัปดาห์'}])
    pie_chart.render_to_file('Pie chart 2556.svg')
graph5()

def graph6():
    pie_chart = pygal.Pie()
    pie_chart.title = 'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2557'
    pie_chart.add('ดื่มนานๆ ครั้ง', [57.6])
    pie_chart.add('ดื่มสม่ำเสมอ', [{'value': 11.12, 'label': 'ดื่มทุกวัน'}, {'value': 5.12, 'label': '5-6 วันต่อสัปดาห์'}, {'value': 8.85, 'label': '3-4 วันต่อสัปดาห์'}, {'value': 17.31, 'label': '1-2 วันต่อสัปดาห์'}])
    pie_chart.render_to_file('Pie chart 2557.svg')
graph6()
