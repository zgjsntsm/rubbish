#! /usr/bin/env python
# -*- coding: utf-8 -*-
import main
import json

a = 'EB58904D53444F53352E300002085A200200000000F800003F00FF000008000000E8FF00D33F000000000000020000000100060000000000000000000000000080012906EFD5404E4F204E414D4520202020464154333220202033C98ED1BCF47B8EC18ED9BD007C885640884E028A5640B441BBAA55CD13721081FB55AA750AF6C1017405FE4602EB2D8A5640B408CD137305B9FFFF8AF1660FB6C640660FB6D180E23FF7E286CDC0ED0641660FB7C966F7E1668946F8837E16007539837E2A007733668B461C6683C00CBB0080B90100E82C00E9A803A1F87D80C47C8BF0AC84C074173CFF7409B40EBB0700CD10EBEEA1FA7DEBE4A17D80EBDF98CD16CD196660807E02000F842000666A0066500653666810000100B4428A56408BF4CD136658665866586658EB33663B46F87203F9EB2A6633D2660FB74E1866F7F1FEC28ACA668BD066C1EA10F7761A86D68A56408AE8C0E4060ACCB80102CD1366610F8274FF81C300026640497594C3424F4F544D475220202020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000D0A4469736B206572726F72FF0D0A507265737320616E79206B657920746F20726573746172740D0A0000000000000000000000000000000000000000000000000000000000000000000000AC01B901000055AA'

def str_hex_list(str):
    '''
    :param str: 传入16进制字符串
    :return: 返回分割的16进制字符串列表，每byte=8bit为一个元素
    '''
    p = range(0,len(str),2)
    temp = []
    for i in p:
        # print(a[i:i+2])
        temp.append(a[i:i+2])
    return temp

def hex_str_to_int(temp):
    '''
    将传入16进制字符串列表转化为数值列表
    :param temp:
    :return:
    '''
    int_list = []
    for i in temp:
        num = int(i,16)
        int_list.append(num)
    return int_list

def str_to_int_list(str):
    '''
    将传入16进制字符串解析为整形数值列表，按字节大小分割存储
    :param str:
    :return:
    '''
    return hex_str_to_int(str_hex_list(str))

def Display_hex_format(temp,style='H'):
    '''
    :param temp: 传入字符串列表
    :return:
    function:格式化打印字符串
    '''
    if style == 'H':
        pass
    elif style == 'D':
        n = 1
        for i in temp:
            if n%16 == 0:
                print(i)
            elif n%8 == 0:
                print(i,end='\t\t')
            else:
                print(i,end='\t')
            n += 1



if __name__ == '__main__':
    # temp = str_hex_list(a)
    # Display_hex_format(temp)
    # Display_hex_format(hex_str_to_int(a),style='D')

    # a = str_to_int_list(a)
    # config = json.loads(open("content.json",encoding='utf-8-sig').read())
    # print(config)
    # print(config['NTFS']['config']['DBR']['mark'])
    # mark_index = config['NTFS']['config']['DBR']['mark']
    # mark_list = [a[510],a[511]]
    # Display_hex_format(mark_list,style='D')

    abc = 4652
    print(hex(abc))
    hex0 = abc%16
    hex1 = (abc-hex0)/16%16
    hex2 = ((abc-hex0)/16-hex1)/16%16
    print(hex0,hex1,hex2)

    def num_to_hexstr(num):
        hex = []
        while 1:
            if num>=16:
                ys = num%16
                if ys == 10:
                    hex.append('a')
                elif ys == 11:
                    hex.append('b')
                elif ys == 12:
                    hex.append('c')
                elif ys == 13:
                    hex.append('d')
                elif ys == 14:
                    hex.append('e')
                elif ys == 15:
                    hex.append('f')
                else:
                    hex.append(str(num%16))
                num = int(num/16)
            else:
                hex.append('1')
                break
        if len(hex)%2 != 0:
            hex.append('0')
        return '0x'+"".join(hex[::-1])

strhex = num_to_hexstr(0x12fec)
print(strhex)