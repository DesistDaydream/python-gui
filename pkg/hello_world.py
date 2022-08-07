import PySimpleGUI as sg

# 设置并返回窗口要使用的主题。该函数仅设置主题的 change_look_and_feel() 函数。
sg.theme('DarkAmber')

# 设置窗口布局。
# 可以设置窗口的标题、大小、位置、是否可以拖动、是否可以关闭、是否可以最小化、是否可以最大化、是否可以全屏、等等
layout = [[sg.Text('第 1 行的一些文字')],
          [sg.Text('在第 2 行输入一些内容'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('关闭')]]

# 实例化一个窗口对象时，传递一个布局。
# Window 是一个类
window = sg.Window('Window Title', layout)
# 事件处理循环。
while True:
    # read() 是 Window 类中最大的方法，这就是我们从窗口中获取所有数据的方式
    event, values = window.read()
    # 如果用户点击“关闭”按钮，将会事件处理循环
    if event == sg.WIN_CLOSED or event == '关闭':  # if user closes window or clicks cancel
        break
    print('你输入了：', values[0])

# 关闭窗口
window.close()
