import pandas as pd

class Work():
    #NOW = Number of workshops
    #PPW = People per workshop
    #WSC = Workshop columns
    #IP = Input Path
    #OP = Output Path

    def __init__(self,now,ppw,wsc,ip,op):
        self.workShopList = []
        self.extras = {}
        self.dataDictionary = {}
        self.maxCapacity = ppw
        self.columns = wsc
        self.initializeWorkShops(now)
        self.file = pd.read_csv(ip)
        self.outupDirectory = op
        self.main()
    def initializeWorkShops(self, integer):
        for i in range(integer):
           self.workShopList.append({}) 

    def main(self):
        for i in range(len(self.file)):
            self.dataDictionary[self.file[self.columns[0]][i]] = []
            for j in self.columns[1:]:
                self.dataDictionary[self.file[self.columns[0]][i]].append(self.file[j][i])
        extrasVariable = 1
        for key, value in self.dataDictionary.items():
            variable = 1
            boolean = True
            count = 0
            while (boolean):
                for i in range(len(value)):
                    if value[i] == variable and len(self.workShopList[i]) < self.maxCapacity:
                        self.workShopList[i][key] = len(self.workShopList[i]) + 1
                        boolean = False
                    if i == len(value) - 1 and count == len(value) - 1:
                        boolean = False
                        self.extras[key] = extrasVariable
                        extrasVariable += 1
                count += 1
                if boolean:
                    variable += 1
        a = pd.DataFrame(data = self.file, )
        self.workShopList.append(self.extras)
        for i in range(len(self.workShopList)):
            for key in self.workShopList[i]:
                with open('{}/WORKSHOP#{}.csv'.format(self.outupDirectory,i+1),'a+') as fileAtIndex:
                    for j in a[a['#'] == key].values:
                        for k in j:
                            fileAtIndex.write(str(k))
                            fileAtIndex.write(', ')
                        fileAtIndex.write('\n')
if __name__ == '__main__':
    Work(9,20,['#','A1','A2','A3','A4','A5','A6','A7','A8','A9'],'/Users/nick/Downloads/work1.csv','/Users/nick/')