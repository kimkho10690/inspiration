import pygal

def graph1():
    """Export to svg"""
    line_graph = pygal.XY()
    line_graph.title = 'อัตราการดื่มเครื่องดื่มแอลกอฮอล์รวม และแยกตามเพศ ระหว่างปี 2544 ถึง 2557'
    line_graph.x_labels = (2544, 2546, 2548, 2550, 2552, 2554, 2556, 2558)
    line_graph.add('Man', [(2544, 55.9), (2547, 55.5), (2550, 52.3), (2554, 53.4), (2556, 54), (2557, 53)])
    line_graph.add('Woman', [(2544, 9.8), (2547, 10.3), (2550, 9.1), (2554, 10.9), (2556, 11.8), (2557, 12.9)])
    line_graph.add('Overall', [(2544, 32.7), (2547, 32.7), (2550, 30), (2554, 31.5), (2556, 32.2), (2557, 32.3)])
    line_graph.render_to_file('1Total alcohol intake by sex between 2001 and 2014.svg')
graph1()
