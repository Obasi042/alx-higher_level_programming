#!/usr/bin/python3
def uniq_add(my_list=[]):
        sum_num = 0
        res_list = []
        for num in my_list:
            if num in res_list:
                res_list.append(num)

        for i in res_list:
            sum_num += i
        return (sum_num)
