# 二进制转换为十进制
a = int('11111',2)# 第一个表示几进制数，第二个数表示几进制
print(a)

b = bin(10)
print(b)#0b开头，把十进制转换为对应的二进制数

c = oct(10)
print(c)#0o开头，把十进制数转换为对应的八进制数

d = hex(16)
print(d)#0x开头，把十进制数转换为对应的十六进制数