----------------------
Name: mteval_sbp
----------------------
Function: automatic evaluation tool for machine translation . The scores of the metrics such as NIST, BLEU, BLEU_SBP, GTM, mWER, mPER and ICT can be obtained by it.
-----------------------
Usage:
	mteval_sbp [-c] -r ref_file -s src_file -t tst_file > result file
		-c case sensitive
		-r reference file
		-s source file
		-t output file of machine translation

	#重新编译后的使用方法
	./mteval_sbp.linux -r /home/sunyy/篇章翻译/score/篇章-en-urheen.xml -s /home/sunyy/篇章翻译/score/test-篇章-urheen-1.xml -t /home/sunyy/篇章翻译/score/test-篇章-分句-trslt-1-join.xml >/home/sunyy/篇章翻译/score/score-huagong-1.txt

1.About the format of input files, please refer to the guidelines of CWMT2011 MT Evaluation;

2.In the result file, for BLEU and BLEU-SBP, if the target language is Chinese, we'll use the 5-gram scores in the table of "Cumulative N-gram scoring", and if the target language isn't Chinese, we'll use the 4-gram scores instead.

e.g.
For the scoring of translation from Chinese to English:
	
	NIST=6.4965  BLEU=0.2999 BLEU_SBP=0.2911 GTM=0.7704 mWER=0.6922 mPER=0.4734 ICT=0.3662

	
	Cumulative N-gram scoring
	            1-gram   2-gram   3-gram   4-gram   5-gram   6-gram   7-gram   8-gram   9-gram
	            ------   ------   ------   ------   ------   ------   ------   ------   ------
	 NIST:      5.2564   6.2473   6.4300   6.4749   6.4965   6.5023   6.5063   6.5083   6.5105 ""
	
	 BLEU:      0.7705   0.5680   0.4129   0.2999   0.2170   0.1607   0.1231   0.0947   0.0747 ""
	 BLEU_SBP:  0.7481   0.5515   0.4009   0.2911   0.2107   0.1561   0.1195   0.0919   0.0726 ""


