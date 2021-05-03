# -*- coding: utf-8 -*-
from difflib import SequenceMatcher , Differ
import time

INPUT_1 = './input/00093.txt'
INPUT_2 = './input/00093_2.txt'

def diff(input1,input2,count, average_count):
    str1 = ''
    str2 = ''
    with open(input1, mode='r') as f:
        str1 = f.read()
    with open(input2, mode='r') as f:
        str2 = f.read()

    print('average_count:', average_count, flush=True)
    print('count:', count, flush=True)
    results = []
    for i in range(0, average_count):
        start = time.time()
        for j in range(0, count):
            SequenceMatcher(None,str1,str2).ratio()
        finish = time.time()
        exec_time = finish-start

        print("time[{}]: {}".format(i, exec_time), flush=True)
        results.append(exec_time)

    print('average:', sum(results)/len(results))

if __name__ == '__main__':
    diff(INPUT_1,INPUT_2,1000, 10)
