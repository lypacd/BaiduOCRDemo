

import re

#查找字符串在文件中的次数
def findStr(file_name,str):
    with open("./test.doc",'r',encoding='utf-8') as f:
        counts = 0
        for line in f.readlines():
            time = line.count(str)
            counts += time
        print("%s出现的次数：%d"%(str,counts))

# file_name="./test.doc"
# string='【临床表现】'
# times=findStr(file_name,string)

#提取疾病信息
def extractDiseaseInfos(times):
    pattern=re.compile('第.*节\s([\u4E00-\u9FA5]+)\s(【.+?】)([^】【]+)\s(【.+?】)([^】【]+)\s(【.+?】)([^】【]+)\s(【.+?】)([^】【]+)')
    with open('./test.doc','r',encoding='utf-8') as fp:
        string=fp.read()
    result = pattern.findall(string)
    print(type(result))
    print(len(result))
    for i in range(4):
        print(result[i])
        print('\n')

extractDiseaseInfos(137)
    # for i in range(times):
    #     dis_type=''
    #     disid=''
    #     dis_name=''
    #     dis_common_name=''
    #     dis_cause=''
    #     susceptible_population=''
    #     propagation_mode=''
    #     clinical_manifestations=''
    #     clinical_manifestations=''


    # disease_infos={}
    # diseases=[]

#提取药品信息