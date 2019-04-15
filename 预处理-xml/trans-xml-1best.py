import os
import sys
def savefile(savepath,content):
	fp = open(savepath,'wb')
	fp.write(content)
	fp.close()
fenfile="/home/sunyy/篇章翻译/语言模型/bert/align-tq5-fixed/out-new-pos-istic-tq-bert-all.xml"
class_path = "/home/sunyy/篇章翻译/语言模型/bert/align-tq5-fixed/out-new-pos-istic-tq-bert-all.txt"
listcontent = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<tstset setid=\"ti_cn_news_combi\" srclang=\"zh\" trglang=\"en\">\n<system site=\"SYSTEM1\" sysid=\"1\" >\n系统描述 化工\n</system>\n<DOC docid=\"news\" >\n"
s=1
content=open(class_path,'rb')
for item in content: 
	rs = item.replace(str.encode('\n'), str.encode(''))
	listcontent = listcontent+"<seg id=\""+str(s)+"\">"+rs.decode()+"</seg>\n"
	s=s+1
listcontent=listcontent+"</DOC>\n</tstset>"
savefile(fenfile,listcontent.encode())