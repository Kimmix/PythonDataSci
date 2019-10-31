import pandas as pd
import numpy as np


def SelectionFeatures(n):
    x = []
    for i in range(2 ** (n)):
        if i == 0:
            print()
        else:
            x.append(format(i, '0'+str(n)+'b'))
    print('Example InitialPopulation: ', x[0], x[1])
    return x


def CrossOver(n):
    x = []
    check_length = len(n[0])/2
    for i in range(len(n)):
        for j in range(len(n)):
            if i != j:
                if check_length % 2 == 0:
                    first_child = n[i][:len(
                        n[i]) // int(check_length)] + n[j][len(n[j]) // int(check_length):]
                    secound_child = n[j][:len(
                        n[j]) // int(check_length)] + n[i][len(n[i]) // int(check_length):]
                    x.append([[first_child], [secound_child]])
                else:
                    first_child = n[i][:len(
                        n[i]) // int(check_length) + 1] + n[j][len(n[j]) // int(check_length) + 1:]
                    secound_child = n[j][:len(
                        n[i]) // int(check_length) + 1] + n[i][len(n[j]) // int(check_length) + 1:]
                    x.append([[first_child], [secound_child]])
    print('Example CrossOver: ', x[0][0], x[0][1])
    return x


def Mutation(n):
    x = []
    print(len(n))
    for i in range(len(n)):
        s1 = np.random.randint(0, len(n[0][0][0]))
        s2 = np.random.randint(0, len(n[0][0][0]))
        if i == 0:
            print("Before: ", n[i][0][0], n[i][1][0], "Index random: ", s1, s2)

        temp1 = list(n[i][0][0])
        temp1[s1] = "1" if n[i][0][0][s1] == "0" else "0"
        n[i][0][0] = "".join(temp1)

        temp2 = list(n[i][1][0])
        temp2[s2] = "1" if n[i][1][0][s2] == "0" else "0"
        n[i][1][0] = "".join(temp2)
        if i == 0:
            print("After: ", n[i][0][0], n[i][1][0], "\n")
        x.append([[n[i][0][0]], [n[i][1][0]]])
    return x


def ChangeToDataSet(n):
    index = []
    x = []
    l = []
    print(len(n))
    for i in range(len(n)):
        for j in range(2):
            for k in range(len(n[i][j][0])):
                if str(n[i][j][0])[k] == str(1):
                    index.append(k)
            dataSet = np.array(df.iloc[0:, index])
            dataSet = dataSet.transpose()
            dataSetClass = np.array(df.iloc[0:, (df.shape[1]) - 1])
            if index != []:
                test = computeMI(dataSet[0], dataSetClass)
                x.append(test)
                l.append(n[i][j])
            index = []
    print('Maximam MI => ', np.amax(x))
    result = np.where(x == np.amax(x))
    print('Data set => ', l[result[0][0]])


def computeMI(x, y):
    sum_mi = 0.0
    x_value_list = np.unique(x)
    y_value_list = np.unique(y)
    Px = np.array([len(x[x == xval])/float(len(x))
                   for xval in x_value_list])  # P(x)
    Py = np.array([len(y[y == yval])/float(len(y))
                   for yval in y_value_list])  # P(y)
    for i in range(len(x_value_list)):
        if Px[i] == 0.:
            continue
        sy = y[x == x_value_list[i]]
        if len(sy) == 0:
            continue
        pxy = np.array([len(sy[sy == yval])/float(len(y))
                        for yval in y_value_list])  # p(x,y)
        t = pxy[Py > 0.]/Py[Py > 0.] / Px[i]  # log(P(x,y)/( P(x)*P(y))
        # sum ( P(x,y)* log(P(x,y)/( P(x)*P(y)) )
        sum_mi += sum(pxy[t > 0]*np.log2(t[t > 0]))
    return sum_mi


df = pd.read_csv("./iris.csv")
col_n = (df.shape[1] - 1)
result_selection = SelectionFeatures(col_n)
result_crossOver = CrossOver(result_selection)
result_mutation = Mutation(result_crossOver)
ChangeToDataSet(result_mutation)
