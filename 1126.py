a = int(input("몇단을 출력할까요?"))
def gugu(num):
    b = 1
    while(b<=9):
        print(num,"*",b,"=",num*b)
        b=b+1
gugu(a)