import numpy as np
from utils import fuzzy_or, fuzzy_and


class EDMAP(object):
    def __init__(self, lr=1, rho=0.5, channel=2, alpha=1e-6, numCol=0):
        self.lr = lr  # learning rate
        self.rho = rho  # rho parameter
        self.channel = channel
        self.gamma = [0.5, 0.5]
        self.alpha = alpha  # parameter for node activation
        self.numCol = numCol
        self.numCell = []
        self.X = []
        self.Y = []
        self.cY = []
        self.w = []
        self.label = []

    def learningMAP(self, x, label):
        # if len(x.shape) == 1:
        #     x = np.array([x])
        normX = x
        for i in range(x.shape[0]):
            normX[i] = np.append(np.array(normX[i]), 1-np.array(normX[i]))
        self.X = normX
        self.label = np.round(label)
        label_ind = np.argmax(self.label)
        if len(self.w) < self.label.size:       # self.w.shape[0] < self.label.shape[0]
            if len(self.w) == 0:
                self.w = [[] for _ in range(label_ind+1)]
            if len(self.w) < label_ind + 1:
                self.w = list(self.w)
                for _ in range(label_ind):
                    self.w.append([])
                # self.w[label_ind].append(self.X)      # new column is added
                self.w[label_ind] = np.array([self.X])      # new column is added
                self.w = np.array(self.w)
            else:
                self.w[label_ind] = np.array([self.X])      # new column is added
                self.w = np.array(self.w)

            self.numCol += 1
            self.numCell.append(1)
        else:
            self.activateCell(label_ind)
            cell_index = np.array(self.cY).argsort()[::-1]
            for i in range(self.numCell[label_ind]):
                ind = cell_index[i]
                resonance = 0
                for j in range(self.channel):
                    m = np.sum(fuzzy_and(self.w[label_ind][ind][j], self.X[j]) / np.sum(self.X[j]))
                    if m >= self.rho:
                        resonance += 1
                    else:
                        break
                if resonance == self.channel:
                    for j in range(self.channel):
                        self.w[label_ind][ind][j] = (1-self.lr) * self.w[label_ind][ind][j] + self.lr * fuzzy_and(self.X[j], self.w[label_ind][ind][j])
                    break
                elif i+1 == self.numCell[label_ind]:
                    # self.w = np.array([np.vstack((self.w[label_ind], np.array([self.X])))])
                    wl = list(self.w)
                    wl_new = list(self.w[label_ind])
                    wl_new.append(self.X)
                    wl[label_ind] = np.array(wl_new)
                    self.w = np.array(wl)
                    self.numCell[label_ind] += 1
        self.Y = self.label

    def activateCell(self, label):
        self.cY = []
        act_k = [[] for _ in range(self.channel)]
        for i in range(self.w[label].shape[0]):
            for k in range(self.channel):
                act_k[k] = self.gamma[k] * (np.sum(fuzzy_and(self.X[k], self.w[label][i][k])) / (self.alpha + np.sum(self.w[label][i][k])))
            self.cY.append(np.sum(act_k))

    def zeroPadding(self, point):
        if len(self.w) != 0:
            # if len(np.array(self.w).shape) != 3:
            #     self.w = np.array([self.w])
            # if self.X.shape[0] < point.shape[0] * 2:
            #     numZeros = int(point.shape[0] - self.X.shape[0] / 2)
            #     self.X = np.zeros((point.shape[0]*2))
            #     new_w = np.hstack((self.w[:,:int(self.w.shape[1]/2)], np.zeros((self.w.shape[0], numZeros)), self.w[:,int(self.w.shape[1]/2):], np.ones((self.w.shape[0], numZeros))))
            #     self.w = new_w
            for i in range(self.channel):
                if self.X[i].shape[0] < point[i].shape[0] * 2:
                    numZeros = int(point[i].shape[0] - self.X[i].shape[0] / 2)
                    for j in range(self.numCol):
                        for k in range(self.numCell[j]):
                            if len(self.w[j][k][i].shape) == 1:
                                half = self.w[j][k][i].shape[0]//2
                                new_w = np.hstack((np.array([self.w[j][k][i][:half]]), \
                                                   np.zeros((np.array([self.w[j][k][i]]).shape[0], numZeros)),
                                                   np.array([self.w[j][k][i][half:]]),
                                                   np.ones((np.array([self.w[j][k][i]]).shape[0], numZeros))))
                            # else:
                            #     half = self.w[j][k][i].shape[1] // 2
                            #     new_w = np.hstack((np.array([self.w[j][k][i][0,:half]]), \
                            #             np.zeros((np.array([self.w[j][k][i]]).shape[0], numZeros)),
                            #             np.array([self.w[j][k][i][0,half:]]), np.ones((np.array([self.w[j][k][i]]).shape[0], numZeros))))
                            new_w = np.squeeze(new_w)
                            self.w[j][k][i] = new_w



    def train(self, X, label):
        self.zeroPadding(X)
        self.learningMAP(X, label)

    def test(self, X, label):
        start = 0
        pred_Y1 = []
        pred_Y3 = []
        if len(label) == 0:
            fin = self.numCol
        else:
            ind = np.argmax(label)
            start = ind
            fin = ind + 1
        T_tmp = np.zeros((3,4))
        for i in range(start, fin):
            for j in range(self.numCell[i]):
                half1 = self.w[i][j][0].shape[0]//2
                T = np.sum(fuzzy_and(X[0], self.w[i][j][0][:half1])) / np.sum(self.w[i][j][0][:half1])
                T_tmp[i][j] = T
                if T >= self.rho:
                    pY1 = np.zeros((1, self.label.size))
                    pY1[0][i] = 1
                    half2 = self.w[i][j][1].shape[0] // 2
                    if len(pred_Y1) == 0:
                        pred_Y1 = np.array([pY1])
                        pred_Y3 = np.array([[self.w[i][j][1][:half2]]])
                    else:
                        pred_Y1 = np.array(np.vstack((pred_Y1, [pY1])))
                        pred_Y3 = np.array(np.vstack((pred_Y3, [[self.w[i][j][1][:half2]]])))
        # print(T_tmp)
        return np.array(pred_Y1), np.array(pred_Y3)

    # def test(self, X, label):
    #     start = 1
    #     pred_Y1 = []
    #     pred_Y3 = []
    #     if len(label) == 0:
    #         fin = self.numCol
    #     else:
    #         ind = np.argmax(label)
    #         start = ind
    #         fin = ind
    #     T_tmp = np.zeros((3,4))
    #     for i in range(start, fin):
    #         for j in range(self.numCell[i]):
    #             T = np.sum(fuzzy_and(X[0], self.w[i][j,:int(self.w.shape[1]/2)])) / np.sum(self.w[i][j,:int(self.w.shape[1]/2)])
    #             T_tmp[i,j] = T
    #             if T >= self.rho:
    #                 pY1 = np.zeros((1, self.label.size))
    #                 pY1[i] = 1
    #                 if len(pred_Y1) == 0:
    #                     pred_Y1 = [pY1]
    #                     pred_Y3 = [self.w[i][j,: int(self.w.shape[1]/2)]]
    #                 else:
    #                     pred_Y1[] = pY1
    #                     pred_Y3[] = self.w[i][j,:int(self.w.shape[1]/2)]
    #     return pred_Y1, pred_Y3



if __name__ == '__main__':
    x = np.array([[1.0, 1.0], [1.0]])
    label = np.array([1.0])
    model = EDMAP()
    model.train(x, label)



