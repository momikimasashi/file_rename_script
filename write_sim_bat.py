# coding=utf-8

import os
import sys

argvs = sys.argv

head_ss = [ \
        "ruby aaa.rb ^\n", \
        "param\param.txt ^\n" \
        ]

# パターンの頭につける文字列を書き込む
def head_sim_s(wf):
    for head_s in head_ss:
        wf.write(head_s)

# ディレクトリ内の指定した文字列をリストに追加
def add_strlist(path):
    ss = []
    flists = os.listdir(path)
    for flist in flists:
        if (flist.find("a") != -1 and flist.find(".txt") != -1):
            ss.append(flist)

    return ss

# ファイルにリスト内の文字列を書き込む
def write_str(wf, ss):
    last_ss = ss[-1]
    for s in ss:
        wf.write(s)
        if (s != last_ss): wf.write(" ^\n")
        else: wf.write(" \n\n")

if __name__ == '__main__':
    wf_name = argvs[1]
    path = argvs[2]
    with open(wf_name, "a") as wf:
        ss = add_strlist(path)
        head_sim_s(wf)
        write_str(wf, ss)
