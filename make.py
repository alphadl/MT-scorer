#!/usr/bin/python
#coding: utf-8

__author__ = "Summer Rain"
  
from sys import argv
from time import time
from os import path, system, listdir

program         = "mteval_sbp.linux"
include_path    = "."
src_path        = "src"
lib_path        = "."

compile_flag    = "-O3"
link_flag       = ""
lib_flag        = ""

if __name__ == "__main__":
    files = [fe for fe in listdir(src_path) if fe.endswith(".cpp") or fe.endswith(".cc")]
    ofes = []
    for sfe in files:
        #print "compiling %s ..." %(sfe)
        print "%s %s %s" %("-" * 20, sfe, "-" * 20)
        ofe = "." + sfe.replace(".cpp", ".o").replace(".cc", ".o")
        time1 = path.getmtime(src_path + "/" + sfe)
        if path.isfile(ofe):
            time2 = path.getmtime(ofe)
        else:
            time2 = time1 - 1 

        if time1 > time2 or len(argv) == 2 and argv[1] == "clean":
            cmd = "g++ -c %s/%s %s -o %s -I%s" %(src_path, sfe, compile_flag, ofe, include_path)
            print cmd
            if system(cmd) != 0:
                exit(1)
        else:
            print "%s is the newest" %(ofe)
        ofes.append(ofe)    
    if files != []:
        print "-" * 40
        cmd = "g++ %s -o %s %s %s -L%s" %(" ".join(ofes), program, link_flag, lib_flag, lib_path)
        print cmd
        system(cmd)
