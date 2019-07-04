#coding: cp949


customer = {'유아':0, '어린이':2000,'청소년':3000,'성인':5000,'노인':0}

while True:
    age = int(input("나이를 입력하세요 : "))

    if age in range(0,4):
        level = '유아'

    elif age in range(4,14):
        level = '어린이'

    elif age in range(14,19):
        level = '청소년'

    elif age in range(19,66):
        level = '성인'

    elif age >=66 :
        level = '노인'

    elif age < 0:
        print("다시 입력하세요")
        continue
    print("등급 %s이고 요금은 %d 입니다." %(level,customer[level]))
    
    payment = int(input("지불방법을 선택하세요 : (1.현금),(2.공원카드)"))

    if payment == 1:
        bill = int(input("요금을 입력하세요 : "))
    
        if bill<customer[level]:
            print ("%d 이 모자랍니다. 입력 하신 %d를 반환합니다." %(customer[level]-bill, bill))
    
        elif bill==customer[level]:
            print("감사합니다. 티켓을 발행합니다.")
        elif bill>customer[level]:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %(bill-customer[level]))
    
    elif payment == 2 :
        print("결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인")
        if age in range(60,66):
            print("%d원 결제 되었습니다. 티켓을 발행합니다." %(customer[level]*0.9*0.95))
            continue
        print("%d원 결제 되었습니다. 티켓을 발행합니다."%(customer[level]*0.9))
