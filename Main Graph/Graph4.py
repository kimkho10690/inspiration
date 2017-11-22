import pygal

def graph4():
    """Export to svg"""
    line_graph = pygal.XY()
    line_graph.title = 'สัดส่วนของผู้ที่ดื่มแอลกอฮอล์เป็นประจำรวม และแยกตามกลุ่มอายุ ระหว่างปี 2544 ถึง 2557'
    line_graph.x_labels = (2544, 2546, 2548, 2550, 2552, 2554, 2556, 2558)
    line_graph.add('15-24 years' , [(2544, 28.1), (2547, 29.9), (2550, 34.98), (2554, 38.65), (2556, 32.01), (2557, 28.98)])
    line_graph.add('25-59 years', [(2544, 35.9), (2547, 40.06), (2550, 41.58), (2554, 44.9), (2556, 42.81), (2557, 44.6)])
    line_graph.add('60+ years', [(2544, 40.6), (2547, 38.01), (2550, 45.67), (2554, 47.66), (2556, 45.01), (2557, 44.05)])
    line_graph.add('Overall', [(2544, 35.08), (2547, 38.22), (2550, 40.89), (2554, 44.22), (2556, 41.45), (2557, 42.41)])
    line_graph.render_to_file('4The proportion of people who drink alcohol regularly and by age group between 2001 and 2014.svg')
graph4()
