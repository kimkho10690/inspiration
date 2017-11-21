import pygal

def graph2():
    """Export to svg"""
    line_graph = pygal.XY()
    line_graph.title = 'สัดส่วนของผู้ที่ดื่มแอลกอฮอล์เป็นประจำรวม และแยกตามเพศ ระหว่างปี 2544 ถึง 2557'
    line_graph.x_labels = (2544, 2546, 2548, 2550, 2552, 2554, 2556, 2558)
    line_graph.add('Man', [(2544, 37.93), (2547, 41.78), (2550, 44.36), (2554, 48.94), (2556, 46.15), (2557, 48.78)])
    line_graph.add('Woman', [(2544, 19.09), (2547, 19.55), (2550, 22.15), (2554, 22.31), (2556, 21.28), (2557, 17.94)])
    line_graph.add('Overall', [(2544, 35.08), (2547, 38.24), (2550, 40.89), (2554, 44.22), (2556, 41.45), (2557, 42.41)])
    line_graph.render_to_file('2The proportion of people who drink alcohol regularly and by sex.svg')
graph2()
