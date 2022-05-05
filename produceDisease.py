# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

# 利用正则对test.doc文档目录产生disease.txt,运行过一次不用再运行
pattern = re.compile(r"第.*节([\u4E00-\u9FA5]+)")

# regex = r"第.*节([\u4E00-\u9FA5]+)"

test_str = ('''第一章常见妇科疾病…1
第一节女性内生殖器基础解剖及生理知识…1
第二节滴虫性阴道炎…2
第三节念珠菌性阴道炎…4
第四节细菌性阴道病…7
第五节萎缩性阴道炎…
86
第六节慢性宫颈炎
10
第七节盆腔炎性疾病
11
第八节子宫内膜异位症
14
第九节子宫腺肌病
15
第十节子宫肌瘤
16
第十一节月经病
17
第十二节带下病
42
第十三节癥瘕…。
47
第十四节女性日常保健与避孕药物的使用
47
附录：妇女常见乳腺疾病…
53
第十五节妇科疾病问诊及联合用药思维
61
第十六节妇科常见疾病测试题及参考答案
63
第二章常见呼吸系统疾病
67
第一节呼吸系统基本解剖知识
67
第二节急性上呼吸道感染
68
第三节呼吸系统其他疾病
73
第四节感冒
81
第五节咳嗽
83
第六节鼻室
…86
第七节鼻鼽
87
第八节喉痹
88
1
常见病
中西医诊断及合理用药·药店专用版
第九节常见呼吸系统疾病测试题及参考答案
91
第三章常见消化系统疾病
94
第一节消化系统基础解剖知识
94
第二节功能性消化不良…
95
第三节肠易激综合征
97
第四节胃食管反流病…
100
第五节慢性胃炎……
102
第六节消化性溃疡…。
104
第七节腹泻及急性肠炎…
106
第八节痔疮…
108
第九节脂肪性肝病…
109
第十节慢性乙型肝炎…
113
第十一节胆囊炎及胆结石
116
第十二节便秘…
120
第十三节胃痛与泄泻…
122
第十四节胁痛…
126
第十五节常见消化系统疾病测试题及参考答案
128
第四章常见循环系统疾病…
132
第一节循环系统的基本组成及常见疾病症状…
132
第二节原发性高血压…
134
附录：社区高血压健康知识普及…
145
第三节低血压
151
第四节血脂异常和异常脂蛋白血症…
154
第五节动脉粥样硬化和冠状动脉粥样硬化性心脏病…
158
第六节脂浊…
166
第七节眩晕…
168
第八节胸痹
170
第九节常见循环系统疾病测试题及参考答案
173
第五章常见神经系统疾病…
177
第一节脑血管疾病
177
第二节头痛
180
第三节失眠及神经衰弱…
184
附录：社区健康讲座睡眠情况自我诊断表…
188
第四节中风…
191
第五节头痛…
193
2
目
录
第六节不寐及健忘…196
第七节常见神经系统疾病测试题及答案
199
第六章常见血液系统疾病…
202
第一节贫血…
202
第二节血劳…
205
第三节常见血液系统测试题及参考答案
207
第七章常见代谢与营养性疾病…
209
第一节糖尿病…
209
附录：2型糖尿病防治指南…
222
第二节低血糖症…
230
第三节代谢综合征及肥胖症…
230
第四节骨质疏松症…
236
附录：正确认识补钙…
238
第五节高尿酸血症和痛风…
240
第六节消渴
243
第七节常见代谢及营养性疾病试题及参考答案
245
第八章常见泌尿系统疾病…
250
第一节泌尿系统的知识点概要
250
第二节尿路感染
251
第三节淋菌性尿道炎…。
253
第四节尿石症…
254
第五节前列腺疾病…259
附录：社区健康教育或公益活动…
269
第六节阳痿…
270
第七节常见泌尿系统疾病测试题及参考答案…
272
第九章常见风湿性疾病及骨关节等疾病…
276
第一节风湿性疾病概述……
276
第二节类风湿关节炎…
278
第三节原发性骨关节炎…
281
第四节肩周炎…
290
第五节腰肌劳损…
291
第六节扭伤。
292
第七节痹症…
…292
第八节腰痛…。
…295
第九节常见风湿骨病测试题及参考答案…
…296
3
常见病
中西医诊断及合理用药·药店专用版
第十章常见皮肤疾病…300
第一节真菌性皮肤病…301
第二节
细菌性皮肤病…
304
第三节病毒性皮肤病…
305
第四节皮炎与湿疹…
310
第五节皮肤附属器疾病
315
第六节荨麻疹与药疹
323
第七节物理性皮肤病
328
第八节银屑病…
332
第九节瘙痒性皮肤病…
334
第十节色素障碍性皮肤病
336
第十一节毛周角化病…
337
第十二节常见皮肤疾病测试题及参考答案…
338
第十一章常见耳鼻喉疾病…
343
第一节分泌性中耳炎
344
第二节急性化脓性中耳炎…
345
第三节梅尼埃病…
346
第四节耳聋…
348
第五节鼻部常见症状…
350
第六节鼻窦炎及急性鼻炎与过敏性（变应）鼻炎
350
第七节酒渣鼻…
354
第十二章常见口腔疾病。
356
第一节口角炎、唇炎及舌炎
356
第二节口腔念珠菌病…
357
第三节复发性口腔溃疡…
358
第四节急性化脓性腮腺炎…
359
第五节牙体牙髓病及牙周疾病…
360
第十三章常见眼科疾病…
363
第一节眼的解剖基础知识及眼部疾病常见症状…
363
第二节眼睑病…
364
第三节结膜疾病。
366
第四节屈光不正
369
第五节白内障…
369
第六节其他眼病…
371
第七节常见五官科疾病测试题及参考答案…373
A
目录
第十四章常见儿科疾病…
…376
第一节鹅口疮…
376
第二节疱疹性口腔炎…
376
第三节手足口病…37门
第四节小儿腹泻…377
第五节小儿细菌性痢疾…378
第六节小儿急性上呼吸道感染…379
第七节急性支气管炎…
379
第八节小儿缺铁性贫血…
380
第九节儿童多动症…
381
第十节水痘…
381
第十一节流行性腮腺炎…
382
第十二节肠蛔虫病…
382
第十三节蛲虫病…
383
第十四节小儿消化不良…
383''')

result = pattern.findall(test_str)

file_name = './data/disease.txt'


# 将列表写入文件
def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a', encoding='utf-8')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")


text_save(file_name,result)


