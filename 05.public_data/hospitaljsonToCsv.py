import json

jsonfile = '부산시 의료기관, 약국 운영시간 정보.json'

myfile = open(jsonfile, 'rt', encoding='utf-8')
myfile = myfile.read()

jsonData = json.loads(myfile)
print(type(jsonData))
print('-'*30)

totallist = []
mycolums = []
idx = 0
for oneitem in jsonData:
    # print(type(oneitem))
    # print(oneitem.keys())
    sublist = []
    for key in oneitem.keys():
        if idx == 0 :
            mycolums.append(key)
        sublist.append(oneitem[key])
    idx += 1
    totallist.append(sublist)
    print('-'*30)

print(totallist)

from pandas import DataFrame

# csv 파일 만들기
myframe = DataFrame(totallist, columns=mycolums)
filename = 'pusanHospitalExcel.csv'
myframe.to_csv(filename, encoding='utf-8', index=False)
print('finished')