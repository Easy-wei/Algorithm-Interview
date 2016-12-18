# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：选择排序
#   版本：
#   作者：WuChong
#   日期：2014-02-08
#   语言：Python 3.3 
#   说明：
#---------------------------------------

def select_sort(ary):
    n = len(ary)
    for i in range(0,n):
        for j in range(i+1,n):
            if ary[j] < ary[i] :
        ary[i],ary[j] = ary[j],ary[i]   #交换两者
    return ary
