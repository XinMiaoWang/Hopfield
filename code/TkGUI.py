import tkinter as tk
from functools import partial
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import globalVar
import Hopfield


# 讀檔
def load_file(cmd):
    if cmd == 'Train':
        globalVar.pathTrain_ = tk.filedialog.askopenfilename()
        pathTrain.set(globalVar.pathTrain_.split('/')[-1])
    elif cmd == 'Test':
        globalVar.pathTest_ = tk.filedialog.askopenfilename()
        pathTest.set(globalVar.pathTest_.split('/')[-1])

# 取得輸入值
def get_value():
    iteration = int(iteration_entry.get())
    noise = int(noise_entry.get())
    begin(iteration,noise)

# 建立介面
def createWidgets():
    global pathTrain, pathTest, iteration_entry, noise_entry

    # Load File ---Start
    pathTrain = tk.StringVar()
    pathTest = tk.StringVar()
    # 标签的文字、字体和字体大小、标签长宽
    trainData_label = tk.Label( window, text="訓練檔案路徑:", font=('Arial', 14), width=15, height=2 ).place(x=0, y=25, anchor='nw')
    trainData_entry = tk.Entry(window, textvariable=pathTrain)
    trainData_entry.place(x=150, y=40, anchor='nw')
    selectTrainbtn = tk.Button(window, text="選擇檔案", font=('Arial', 14), command=partial(load_file,'Train')).place(x=300, y=30, anchor='nw')

    testData_label = tk.Label(window, text="測試檔案路徑:", font=('Arial', 14), width=15, height=2).place(x=0, y=100,anchor='nw')
    testData_entry = tk.Entry(window, textvariable=pathTest)
    testData_entry.place(x=150, y=115, anchor='nw')
    selectTestbtn = tk.Button(window, text="選擇檔案", font=('Arial', 14), command=partial(load_file,'Test')).place(x=300, y=105, anchor='nw')
    # Load File ---End

    # 迭代次數設定 ---Start
    iteration_label = tk.Label( window, text='迭代次數設定:', font=('Arial', 14), width=15, height=2 ).place(x=0, y=170, anchor='nw')
    iteration_entry = tk.Entry(window)
    iteration_entry.place(x=150, y=185, anchor='nw')
    # 迭代次數設定 ---End

    noise_label = tk.Label(window, text='是否加入雜訊(0:否，1:是):', font=('Arial', 14), width=20, height=2).place(x=25, y=250,anchor='nw')
    noise_entry = tk.Entry(window)
    noise_entry.place(x=260, y=265, anchor='nw')

    # 執行 ---Start
    start = tk.Button( window, text="執行", width=15, height=2, command=get_value ).place(x=150, y=500, anchor='nw')
    # 執行 ---End

# 開始執行hopfield
def begin(iteration, add):
    trainData, row_train, col_train = Hopfield.readfile(globalVar.pathTrain_)
    testData, row_test, col_test = Hopfield.readfile(globalVar.pathTest_)
    NoiseData = Hopfield.addNoise(trainData)
    # Hopfield.hopfield(trainData, testData, row_train, col_train, iteration, progressbar)
    Hopfield.hopfield(trainData, testData, NoiseData, row_train, col_train, iteration, progressbar, add)

if __name__ == '__main__':
    globalVar.initialize()

    window = tk.Tk()
    window.title('Hw3')
    window.geometry('600x600') # 視窗大小

    # 進度條
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='salmon', background='salmon')
    bar_label = tk.Label(window, text='迭代進度', font=('Arial', 14) ).place(x=20, y=350)
    progressbar = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate",
                                  style="red.Horizontal.TProgressbar")
    progressbar.place(x=120, y=355)

    createWidgets() # 建立介面
    window.mainloop()
