#실습 1 홀수단 또는 짝수단 출력하는 함수

def gugudan_even():
    for i in range(2, 10, 2):
        for j in range(1, 10):
            print(" %d x %d  = %d" % (i, j, j*i))

def gugudan_odd():
     for i in range(1, 10, 2):
        for j in range(1, 10):
            print("%d x %d = %d" % (i, j, i*j))

def check_gugudan(num):
    if num % 2 == 0:
        gugudan_even()
    else:
        gugudan_odd()


#실습 2 주어진 숫자에 따라 구구단 출력하는 함수

def check_gugu(num):
    i = 1
    while i <= num:
        for j in range(1,10):
            print("%d X %d" % (i, j))
        i += 1
