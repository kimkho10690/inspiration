import pygal

def graph3():
    """Export to svg"""
    line_graph = pygal.XY()
    line_graph.title = 'อัตราการดื่มเครื่องดื่มแอลกอฮอล์รวม และแยกตามกลุ่มอายุ ระหว่างปี 2544 ถึง 2557'
    line_graph.x_labels = (2544, 2546, 2548, 2550, 2552, 2554, 2556, 2558)
    line_graph.add('15-24 years' , [(2544, 21.58), (2547, 23.53), (2550, 22.17), (2554, 23.67), (2556, 26.24), (2557, 25.2)])
    line_graph.add('25-59 years', [(2544, 39.22), (2547, 38.66), (2550, 35.38), (2554, 37.33), (2556, 38.15), (2557, 38.17)])
    line_graph.add('60+ years', [(2544, 20.03), (2547, 19.32), (2550, 16.44), (2554, 16.58), (2556, 16.2), (2557, 18.41)])
    line_graph.add('Overall', [(2544, 32.61), (2547, 32.69), (2550, 30.02), (2554, 31.53), (2556, 32.22), (2557, 32.29)])
    line_graph.render_to_file('3Total alcohol intake by age group between 2001 and 2014.svg')
graph3()
