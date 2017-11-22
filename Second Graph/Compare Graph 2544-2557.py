###เปรียบเทียบ###
import pygal
###
line_chart = pygal.HorizontalBar(print_labels=True)
line_chart.title = 'เปรียบเทียบรอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2544 - 2557'

##line_chart.add('ดื่มทุกวัน', [{'value': 7.96, 'label': '2544'}, {'value': 9.5, 'label': '2547'}, {'value': 12.81, 'label': '2550'}, {'value': 11.38, 'label': '2554'}, {'value': 9.72, 'label': '2556'}, {'value': 11.12, 'label': '2557'}])
##line_chart.add('5-6 วันต่อสัปดาห์', [{'value': 6.87, 'label': '2554'}, {'value': 7.04, 'label': '2556'}, {'value': 5.12, 'label': '2557'}])
##line_chart.add('3-4 วันต่อสัปดาห์', [{'value': 9.9, 'label': '2544'}, {'value': 10.2, 'label': '2547'}, {'value': 9, 'label': '2550'}, {'value': 8.85, 'label': '2554'}, {'value': 7.73, 'label': '2556'}, {'value': 8.85, 'label': '2557'}])
##line_chart.add('1-2 วันต่อสัปดาห์', [{'value': 17.27, 'label': '2544'}, {'value': 18.6, 'label': '2547'}, {'value': 19.08, 'label': '2550'}, {'value': 17.1, 'label': '2554'}, {'value': 16.95, 'label': '2556'}, {'value': 17.31, 'label': '2557'}])
##line_chart.add('ดื่มนานๆครั้ง', [{'value': 64.87, 'label': '2544'}, {'value': 61.7, 'label': '2547'}, {'value': 59.11, 'label': '2550'}, {'value': 55.8, 'label': '2554'}, {'value': 58.56, 'label': '2556'}, {'value': 57.6, 'label': '2557'}])
##line_chart.render_to_file('Compare Graph 2544-2557.svg')

line_chart.x_labels = ['ดื่มนานๆครั้ง', '1-2 วันต่อวัปดาห์', '3-4 วันต่อสัปดาห์', '5-6 วันต่อสัปดาห์', 'ดื่มทุกวัน']
line_chart.y_labels = map(int, range(0, 71, 10))
line_chart.add('2544', [{'value': 64.87, 'label': '64.87%'}, {'value': 17.27, 'label': '17.27%'}, {'value': 9.9, 'label': '9.9%'}, None, {'value': 7.96, 'label': '7.96%'}])
line_chart.add('2547', [{'value': 61.7, 'label': '61.7%'}, {'value': 18.6, 'label': '18.6%'}, {'value': 10.2, 'label': '10.2%'}, None, {'value': 9.5, 'label': '9.5%'}])
line_chart.add('2550', [{'value': 59.11, 'label': '59.11%'}, {'value': 19.08, 'label': '19.08%'}, {'value': 9, 'label': '9%'}, None, {'value': 12.81, 'label': '12.81%'}])
line_chart.add('2554', [{'value': 55.8, 'label': '55.8%'}, {'value': 17.1, 'label': '17.1%'}, {'value': 8.85, 'label': '8.85%'}, {'value': 6.87, 'label': '6.87%'}, {'value': 11.38, 'label': '11.38%'}])
line_chart.add('2556', [{'value': 58.56, 'label': '58.56%'}, {'value': 16.95, 'label': '16.95%'}, {'value': 7.73, 'label': '7.73%'}, {'value': 7.04, 'label': '7.04%'}, {'value': 9.72, 'label': '9.72%'}])
line_chart.add('2557', [{'value': 57.6, 'label': '57.6%'}, {'value': 17.31, 'label': '17.31%'}, {'value': 8.85, 'label': '8.85%'}, {'value': 5.12, 'label': '5.12%'}, {'value': 11.12, 'label': '11.12%'}])
line_chart.render_to_file('Compare Graph 2544-2557.svg')
