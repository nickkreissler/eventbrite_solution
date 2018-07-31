import pandas as pd

workShop1 = {}
workShop2 = {}
workShop3 = {}
workShop4 = {}
workShop5 = {}
workShop6 = {}
workShop7 = {}
workShop8 = {}
workShop9 = {}
extras = {}

peoplePerWorkShop = 50
user = 'nick'
l = ['#','A1','A2','A3','A4','A5','A6','A7','A8','A9']
l2 = [workShop1,workShop2,workShop3,workShop4,workShop5,workShop6,workShop7,workShop8,workShop9]
dataDic = {}

file = pd.read_csv('/Users/nick/Downloads/work1.csv')
y = len(file)

for i in range(len(file)):
    dataDic[file[l[0]][i]] = []
    for j in l[1:]:
      dataDic[file[l[0]][i]].append(file[j][i])
extrasVariable = 1
for key, value in dataDic.items():
  variable = 1
  boolean = True
  count = 0

  while (boolean):
    for i in range(len(value)):
      if value[i] == variable and len(l2[i]) < peoplePerWorkShop:
        l2[i][key] = len(l2[i]) + 1
        boolean = False
      if i == len(value) - 1 and count == len(value) - 1:
        boolean = False
        extras[key] = extrasVariable
        extrasVariable += 1
    count += 1
    if boolean:
      variable += 1
a = pd.DataFrame(data = file)
l2.append(extras)

for i in range(len(l2)):
  for key in l2[i]:
    with open('/Users/{}/Desktop/WORKSHOP#{}.csv'.format(user,i+1),'a+') as fileAtIndex:
      for j in a[a['#'] == key].values:
        for k in j:
          fileAtIndex.write(str(k))
          fileAtIndex.write(', ')
        fileAtIndex.write('\n')
        
        
      
      
