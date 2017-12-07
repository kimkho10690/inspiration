###New Graph###
import pygal
###
"""2544"""
def graph1():
    gauge = pygal.SolidGauge(inner_radius=0.70, title=u'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2544')
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('ดื่มทุกวัน', 7.96)
    gauge.add('3-4 วันต่อสัปดาห์', 9.9)
    gauge.add('1-2 วันต่อสัปดาห์', 17.27)
    gauge.add('ดื่มนานๆครั้ง', 64.87)
    gauge.render_to_file('Gauge chart 2544.svg')
graph1()

"""2547"""
def graph2():
    gauge = pygal.SolidGauge(inner_radius=0.70, title=u'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2547')
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('ดื่มทุกวัน', 9.5)
    gauge.add('3-4 วันต่อสัปดาห์', 10.2)
    gauge.add('1-2 วันต่อสัปดาห์', 18.6)
    gauge.add('ดื่มนานๆครั้ง', 61.7)
    gauge.render_to_file('Gauge chart 2547.svg')
graph2()

"""2550"""
def graph3():
    gauge = pygal.SolidGauge(inner_radius=0.70, title=u'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2550')
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('ดื่มทุกวัน', 12.81)
    gauge.add('3-4 วันต่อสัปดาห์', 9)
    gauge.add('1-2 วันต่อสัปดาห์', 19.08)
    gauge.add('ดื่มนานๆครั้ง', 59.11)
    gauge.render_to_file('Gauge chart 2550.svg')
graph3()

"""2554"""
def graph4():
    gauge = pygal.SolidGauge(inner_radius=0.70, title=u'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2554')
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('ดื่มทุกวัน', 11.38)
    gauge.add('5-6 วันต่อสัปดาห์', 6.87)
    gauge.add('3-4 วันต่อสัปดาห์', 8.85)
    gauge.add('1-2 วันต่อสัปดาห์', 17.1)
    gauge.add('ดื่มนานๆครั้ง', 55.8)
    gauge.render_to_file('Gauge chart 2554.svg')
graph4()

"""2556"""
def graph5():
    gauge = pygal.SolidGauge(inner_radius=0.70, title=u'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2556')
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('ดื่มทุกวัน', 9.72)
    gauge.add('5-6 วันต่อสัปดาห์', 7.04)
    gauge.add('3-4 วันต่อสัปดาห์', 7.73)
    gauge.add('1-2 วันต่อสัปดาห์', 16.95)
    gauge.add('ดื่มนานๆครั้ง', 58.56)
    gauge.render_to_file('Gauge chart 2556.svg')
graph5()

"""2557"""
def graph6():
    gauge = pygal.SolidGauge(inner_radius=0.70, title=u'รอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จําแนกตามความถี่ในการดื่มสุราหรือเครื่องดื่มมึนเมา ปี 2557')
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('ดื่มทุกวัน', 11.12)
    gauge.add('5-6 วันต่อสัปดาห์', 5.12)
    gauge.add('3-4 วันต่อสัปดาห์', 8.85)
    gauge.add('1-2 วันต่อสัปดาห์', 17.31)
    gauge.add('ดื่มนานๆครั้ง', 57.6)
    gauge.render_to_file('Gauge chart 2557.svg')
graph6()
