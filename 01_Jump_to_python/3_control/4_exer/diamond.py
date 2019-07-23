start = 1
while True:
    diamond = int(input("홀수를 출력하세요(0 <-종료)"))
    if diamond==0:
        break
    elif diamond%2==0:
        continue
    else:
        while diamond > start:
            print(" "*((diamond-start)//2-1)+('*'* start)+" "*((diamond-start)//2-1))
            start += 2
