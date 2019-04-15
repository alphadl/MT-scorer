import os
import sys
def savefile(savepath,content):
	fp = open(savepath,'wb')
	fp.write(content)
	fp.close()
fenfile="/home/sunyy/NiuTrans/Tool-minority/ISTIC-ZKY/05/nist05_plain_ref0-s.xml"
class_path = "/home/sunyy/NiuTrans/Tool-minority/ISTIC-ZKY/05/nist05_plain_ref0-s.txt"
listcontent = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<srcset setid=\"zh_en_news_trans\" srclang=\"zh\" trglang=\"en\">\n<DOC docid=\"news\"\n"
s=1
content=open(class_path,'rb')
for item in content: 
	rs = item.replace(str.encode('\n'), str.encode(''))
	listcontent = listcontent+"<seg id=\""+str(s)+"\">"+rs.decode()+"</seg>\n"
	s=s+1
listcontent=listcontent+"</DOC>\n</srcset>"
savefile(fenfile,listcontent.encode())


