import pandas as pd

filename = 'pusanHospitalExcel.csv'
myframe = pd.read_csv(filename, encoding='utf-8')
print(myframe.info())
print('-'*30)

print(myframe.columns)
print('-'*30)

print(myframe['instit_kind'].unique())
print('-'*30)

mygrouping = myframe.groupby(['instit_kind'])['instit_kind']
print(type(mygrouping))
print('-'*30)

chartdata = mygrouping.count()
print(type(chartdata))
print(mygrouping)
print('-'*30)

newdata = chartdata[chartdata > 1000]
print(newdata)
print('-'*30)

import matplotlib.pylab as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure()
newdata.plot(kind='pie', legend=True, autopct='%6.3f%%')
savefilename = 'getHospitalInfo01.png'
plt.savefig(savefilename, dpi=400)
print(savefilename + '파일이 저장되었습니다')

mycolor = ['r', 'g', 'b', 'm']
plt.figure()
newdata.plot(kind='bar', legend=False, title='부산 지역 병의원 현황 top4', color=mycolor, rot=0)
savefilename = 'getHospitalInfo02.png'
plt.savefig(savefilename, dpi=400)
print(savefilename + '파일이 저장되었습니다')



