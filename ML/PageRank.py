import numpy as np
import pandas as pd
import os

path = './result-csv'
try:
    os.mkdir(path)
except FileExistsError:
    pass

class PageRank:
    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser
        self.players = []
        self.df = pd.DataFrame()
        self.damping_factor = 0.85

        for i,j in zip(self.winner, self.loser):
            if i not in self.players:
                self.players.append(i)
            if j not in self.players:
                self.players.append(j)

        self.n = len(self.players)
        self.initial = 1.000000 / self.n

    def makeMap(self):
        
        self.df['player'] = self.players
        
        for i in self.players:
            self.df[i] = 0

        self.df['node'] = 0.0

        for i,j in zip(self.winner, self.loser):
            idx1 = self.df[self.df['player'] == i].index.tolist()
            idx2 = self.df[self.df['player'] == j].index.tolist()
            self.df[j][idx1] += 1
            self.df['node'][idx2] += 1.0

        self.df['div'] = self.initial / self.df['node']

        ##### 수정하고 싶은데.... 더 깔끔하게
        data = np.array(self.df)
        lst = []

        for i in range(0,self.n):
            result = 0
            if data[i][self.n+1] == 0:
                result += self.initial # 정규화가 안되서 무패자 페이지랭크 추가
            for j in range(1,self.n+1):
                if i+1 == j:
                    pass
                if data[i][j] > 0:
                    result += data[j-1][self.n+2] * data[i][j]
            pgrk = (1-self.damping_factor)/self.n + self.damping_factor*result
            lst.append(pgrk)
        #####

        self.df['pagerank'] = lst

        return self.df
    
    def tocsv(self):
        dtc = pd.DataFrame()
        dtc['player'] = self.df['player']
        dtc['pagerank'] = self.df['pagerank']
        
        dtc.to_csv(f'{path}/pagerank.csv', encoding='UTF-8-sig')

    def tocsv_df(self):
        self.df.to_csv(f'{path}/df.csv', encoding='UTF-8-sig')
