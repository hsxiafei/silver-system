#coding=utf-8
f = open('report.txt')

score_final = []
for line in f.readlines():
    score = []
    line = line.decode('GBK').encode('utf-8')
    text_int = [int(x) for x in line.split()[1:]]
    text_int.append(sum(text_int))  #个体总分
    text_int.append(text_int[-1]/(len(text_int)-1)) #个体平均分
    score.append(line.split()[0])
    score.append(text_int)  #个体名字+分数列表
    score_final.append(score)
f.close()

score_final = sorted(score_final, key=lambda x: x[-1][-1], reverse=True)
score_final = sorted(score_final, key=lambda x: x[-1][-2], reverse=True)
for a in range(1,len(score_final)+1):
    score_final[a-1].insert(0, a)  #排序并添加排名


sub_avr = []
people = len(score_final)

for num in range(11):
    sub_sum = 0
    for i in range(people):
        sub_sum += score_final[i][2][num]
    sub_avr.append(sub_sum/people)
sub_avr = [0, '平均', [x for x in sub_avr]]       #添加各学科平均分
score_final.insert(0, sub_avr)


for i in range(0, people+1):
    for h in score_final[i][2]:
        if h < 60:
            score_final[i][2][score_final[i][2].index(h)] = '不及格' #替换不及格成绩

for h in score_final:
    score_final[score_final.index(h)] = [str(h[0]), h[1]]+[str(x) for x in h[2]] #调整数据类型

with open('analysis.txt', 'w') as f:
    f.write('名次\t姓名\t语文\t数学\t英语\t物理\t'
            '化学\t生物\t政治\t历史\t地理\t总分\t平均分\n')
    for i in score_final:
        f.write('%s\n' % ('\t'.join(i)))




