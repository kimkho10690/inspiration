###เปรียบเทียบ###
import pygal
###
line_chart = pygal.HorizontalBar(print_labels=True, stack_from_top=False)
line_chart.title = 'เปรียบเทียบรอยละของประชากรอายุ 15 ปขึ้นไปที่ดื่มสุราหรือเครื่องดื่มมึนเมา จำแนกตามประเภทของสุราที่ดื่มบ่อย ปี 2544 - 2557'

line_chart.x_labels = ['อื่นๆ', 'ไวน์', 'สุราแช่พื้นบ้าน (สาโท อุ กระแช่)', 'สุราขาว, สุราสี, สุรากลั่น', 'เบียร์']
line_chart.y_labels = map(int, range(0, 70, 10))
line_chart.add('2547', [{'value': 4.36, 'label': '4.36%'}, {'value': 1.37, 'label': '1.37%'}, {'value': 10.73, 'label': '10.73%'}, {'value': 51.25, 'label': '51.25%'}, {'value': 32.39, 'label': '32.39%'}])
line_chart.add('2550', [{'value': 1.57, 'label': '1.57%'}, {'value': 0.64, 'label': '0.64%'}, {'value': 0.15, 'label': '0.15%'}, {'value': 51.97, 'label': '51.97%'}, {'value': 45.67, 'label': '45.67%'}])
line_chart.add('2554', [{'value': 0.28, 'label': '0.28%'}, {'value': 1.57, 'label': '1.57%'}, {'value': 0.73, 'label': '0.73%'}, {'value': 53.16, 'label': '53.16%'}, {'value': 42.69, 'label': '42.69%'}])
line_chart.add('2557', [{'value': 3.4, 'label': '3.4%'}, {'value': 6.93, 'label': '6.93%'}, {'value': 2.8, 'label': '2.8%'}, {'value': 51.1, 'label': '51.1%'}, {'value': 35.77, 'label': '35.77%'}])
line_chart.render_to_file('Compare Graph 2544-2557 - ประเภทสุรา.svg')
