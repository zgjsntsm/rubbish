# -*- coding:utf-8 -*-
# by finger

def xor(x,y):
    '''
    :param x:被运算数
    :param y:运算数
    :return:x xor y   保留低8位溢出值舍弃
    '''
    # print(x,y)
    req = (x ^ y) & 0xff
    # print(req,hex(req))
    return req

def add(x,y):
    '''
    :param x:被运算数
    :param y:运算数
    :return:x add y   保留低8位溢出值舍弃
    '''
    # print(x,y)
    req = (x + y + 0x100) & 0xff
    # print(req,hex(req))
    return req

def req_function(x_list,y_list):
    '''
    穷举运算x_list 对比 y_list
    一次xor及add运算
    :param x_list:
    :param y_list:
    :return:
    '''
    num = 0
    req_list_all=[]
    for x in x_list:
        req_list = []
        add_list = range(-0xff,0xff)
        xor_list = range(0x00,0xff)
        # 先加减后异或
        for m in add_list:
            for n in xor_list:
                req1 = xor(add(x,m),n)
                if(req1 == y_list[num]):
                    req_list.append('add:{},xor:{}'.format(hex(m),hex(n)))  #存储匹配值
        # 先异或后加减
        for m in xor_list:
            for n in add_list:
                req2 = add(xor(x,m),n)
                if (req2 == y_list[num]):
                    req_list.append('xor:{},add:{}'.format(hex(m), hex(n)))
        # req_list_all.append(req_list)
        if num == 0:
            req = req_list
        else:
            req = set(req)&set(req_list)
        num = num+1
    print(req)
    # print(len(req))
    # return req_list

if __name__ == '__main__':
    x_list = [0x1e,0xa5,0xe7,0xac,0xdd]
    y_list = [0xeb,0x52,0x90,0x55,0xaa]
    req_function(x_list,y_list)
