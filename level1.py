input_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
dic = 'abcdefghijklmnopqrstuvwxyz'
dic_ad = dic[2:]+dic[:2]
# print dic_ad
output_str = ''
for i in input_str:
    if i in dic:
        output_str += dic_ad[dic.index(i)]
    else:
        output_str += i
print output_str
# map translated to ocr
