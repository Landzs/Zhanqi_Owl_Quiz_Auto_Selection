import time
from time import gmtime, strftime


def write_in_txt(write_in):
    with open("record.txt", "a") as f:  # 格式化字符串还能这么用！
        f.write("\n------------------------------------------------------------------------------\n")
        for i in write_in:
            f.write(i)








str1 = "At {:.3f}s".format(time.time())
number1 = 213
str1 = str1 + ' left'+'\n' + 'A ' + str(number1)
str1 = str1 + '\n' + strftime("%H:%M:%S", time.localtime())
print(str1)
write_in_txt(str1)
# with open("record.txt" , "a") as f:  # 格式化字符串还能这么用！
#     f.write("\n------------------------------------------------------------------------------\n")
#     for i in str1:
#         f.write(i)
str1 = strftime("%d %b %Y", time.localtime()) + '\n'
write_in_txt(str1)
# with open("record.txt" , "a") as f:  # 格式化字符串还能这么用！
#     # f.write("\n------------------------------------------------------------------------------\n")
#     for i in str1:
#         f.write(i)