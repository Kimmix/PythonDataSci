import pandas as pd
import numpy as np

# Crete population sample


def genChromosome(dataCol):
    print('List all population -------------------------------',)
    ans = []
    for i in range(2 ** dataCol):
        if i == 0:
            pass
        else:
            ans.append(format(i, '0' + str(dataCol) + 'b'))
    print('\tResult =', ans)
    print('\tTotal population =', (2 ** dataCol) - 1)
    return ans


def crossing(p1, p2):
    print('\tChrmosome 1 =', p1, '\tChrmosome 2 =', p2)
    length = int(len(p1) / 2)
    if length % 2 != 0:
        length += 1
    p11 = p1[: length]
    p12 = p1[length:]
    p21 = p2[: length]
    p22 = p2[length:]
    print('\tOffspring 1 =', p11 + p22, '\tOffspring 2 =', p21 + p12)


def crossOver(chromosome):
    print('Crossover ------------------------------------------')
    count = 1
    for i in chromosome:
        for j in chromosome:
            if i == j:
                continue
            print(' #', count, end='')
            crossing(i, j)
            print('\t---------------------------------------------')
            count += 1


def mutation(chromosome, noRound):
    print('Mutation', noRound, 'round ------------------------------------')
    for i in range(noRound):
        chromosomeSample = chromosome[np.random.randint(0, len(chromosome))]
        swapPosition = np.random.randint(0, len(chromosomeSample))
        print(' #', i, '\tChromosome =',
              chromosomeSample)
        _temp = list(chromosomeSample)
        _temp[swapPosition] = "1" if _temp[swapPosition] == "0" else "0"
        chromosomeSample = "".join(_temp)
        print('\tSwap at', swapPosition+1, '=>', chromosomeSample)


def transformChromosome(data, chromosome):
    return data.iloc[0:, [i for i, char in enumerate(chromosome) if char == '1']]


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


iris = pd.read_csv("./iris.csv")
col = len(iris.columns) - 1
irisChromosome = genChromosome(col)
crossOver(irisChromosome)
mutation(irisChromosome, 5)

# Find max MI
print('Max Mi ---------------------------------------------')
maxMi = 0
for i in irisChromosome:
    chromo = np.array(transformChromosome(iris, i)).transpose()[0]
    print(chromo)
    curMi = computeMI(chromo, iris['class'])
    if curMi >= maxMi:
        maxMi = curMi
        maxChro = i
print('\tMax MI =', maxMi, '\n\tChromosome =', maxChro)
