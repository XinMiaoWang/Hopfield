import numpy as np
import matplotlib.pyplot as plt
import random

# 顯示完整print
# np.set_printoptions(threshold=np.inf)

# 讀檔
def readfile(filename):
    data, temp = [], []
    row , col = (0, 0)

    with open(filename) as file:
        for line in file.readlines():
            if line == '\n':
                data.append(temp)
                row = len(temp) // col
                temp = []
            for i in line:
                if i == ' ':
                    temp.append(-1) # 空白處填-1
                elif i != '\n':
                    temp.append(1)

            col = len(line)-1

        col = col + 1 # 最後一行不會有\n
        data.append(temp)
        data = np.array(data)

        return data, row, col

def addNoise(data):
    Noise = np.copy(data)
    num_files = data.shape[0]
    ratio = len(data[0])//10
    list = []
    for i in range(len(data[0])):
        list.append(i)
    random.shuffle(list)
    list = list[:ratio]

    for num in range(num_files):
        for idx in list:
            if data[num][idx] == 1:
                Noise[num][idx] = -1
            # elif data[num][idx] == -1:
            #     Noise[num][idx] = 1

    return Noise

def create_weight(x):
    p = len(x) # data長度
    I = np.identity(p) # 單位矩陣
    # weight = (1/p) * np.dot(x,x.T)- (1/p) * I
    weight = np.dot(x,x.T) - I

    return weight

def create_theta(w):
    theta = []
    for i in range(len(w)):
        value = 0
        for j in range(len(w)):
            value = value + w[i][j]
        theta.append(value)

    theta = np.array(theta).reshape(len(w),1)

    return theta

# 網路回想
def update(w, x, theta):
    for i in range(len(x)):
        u = np.dot(w[i][:], x) - theta[i]
        if u > 0:
            x[i] = 1
        elif u < 0:
            x[i] = -1

    return x

def showResult(num_files, ans, input, output):
    fig = plt.figure(figsize=(18,12))
    fig.subplots_adjust(hspace=0.4, wspace=1)
    fig.tight_layout()

    # 顯示正確答案
    index = 0
    for i in range(1, num_files+1):
        ax = fig.add_subplot(3, num_files, i)
        ax.set_title('Answer')
        ax.matshow(ans[index])
        index = index + 1

    # 顯示測試資料
    index = 0
    for i in range(num_files+1, 2*num_files+1):
        ax = fig.add_subplot(3, num_files, i)
        ax.set_title('Input')
        ax.matshow(input[index])
        index = index + 1

    # 顯示回想結果
    index = 0
    for i in range(2*num_files+1, 3*num_files+1):
        ax = fig.add_subplot(3, num_files, i)
        ax.set_title('Recall')
        ax.matshow(output[index])
        index = index + 1

    plt.show()

# hopfield 模型
def hopfield(trainData, testData, NoiseData, row, col, iteration, progressbar, add):
    num_files = trainData.shape[0]
    weight = np.zeros([len(trainData[0]), len(trainData[0])])
    p = len(trainData[0])
    # 算 weight
    if add:
        for num in range(num_files):
            if num  == 0:
                weight = create_weight(np.array([trainData[num]]).T) * (1/p)
                weight = weight + create_weight(np.array([NoiseData[num]]).T) * (1/p)
            else:
                weight = weight + create_weight(np.array([trainData[num]]).T) * (1/p)
                weight = weight + create_weight(np.array([NoiseData[num]]).T) * (1/p)
    else:
        for num in range(num_files):
            if num  == 0:
                weight = create_weight(np.array([trainData[num]]).T) * (1/p)
            else:
                weight = weight + create_weight(np.array([trainData[num]]).T) * (1/p)

    theta = create_theta(weight)



    ans, input, output = [], [], []
    progressbar["value"] = 0
    progressbar["maximum"] = iteration - 1

    # 開始回想
    for t in range(iteration):
        progressbar["value"] = t
        progressbar.update()
        for num in range(num_files):
            tmp1 = trainData[num].reshape(row,col)
            ans.append(tmp1)
            tmp2 = testData[num].reshape(row, col)
            input.append(tmp2)
            result = update(weight, np.array([testData[num]]).T, theta).reshape(row,col)
            output.append(result)

    ans = np.array(ans)
    input = np.array(input)
    output = np.array(output)
    showResult(num_files, ans, input, output)

# if __name__ == '__main__':
#     train_filename = 'C:/Users/user\Desktop\HopfielddataSet\Basic_Training.txt'
#     test_filename = 'C:/Users/user\Desktop\HopfielddataSet\Basic_Testing.txt'
#     # train_filename = 'C:/Users/user\Desktop\HopfielddataSet\Bonus_Training.txt'
#     # test_filename = 'C:/Users/user\Desktop\HopfielddataSet\Bonus_Testing.txt'
#
#     trainData, row_train, col_train = readfile(train_filename)
#     testData, row_test, col_test = readfile(test_filename)
#
#     hopfield(trainData, testData, row_train, col_train, 1)
