for a in range(1,101):
##打印输出1到100（包含1,100），不是7的倍数、且不含7的数，每行输出一个数字。
    if a % 7 == 0 or a % 10 == 7 or a // 10 == 7:
        continue
        print(a)

