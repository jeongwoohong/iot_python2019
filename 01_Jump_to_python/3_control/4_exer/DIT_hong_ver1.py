#coding: cp949


customer = {'����':0, '���':2000,'û�ҳ�':3000,'����':5000,'����':0}

while True:
    age = int(input("���̸� �Է��ϼ��� : "))

    if age in range(0,4):
        level = '����'

    elif age in range(4,14):
        level = '���'

    elif age in range(14,19):
        level = 'û�ҳ�'

    elif age in range(19,66):
        level = '����'

    elif age >=66 :
        level = '����'

    elif age < 0:
        print("�ٽ� �Է��ϼ���")
        continue
    print("��� %s�̰� ����� %d �Դϴ�." %(level,customer[level]))
    
    payment = int(input("���ҹ���� �����ϼ��� : (1.����),(2.����ī��)"))

    if payment == 1:
        bill = int(input("����� �Է��ϼ��� : "))
    
        if bill<customer[level]:
            print ("%d �� ���ڶ��ϴ�. �Է� �Ͻ� %d�� ��ȯ�մϴ�." %(customer[level]-bill, bill))
    
        elif bill==customer[level]:
            print("�����մϴ�. Ƽ���� �����մϴ�.")
        elif bill>customer[level]:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(bill-customer[level]))
    
    elif payment == 2 :
        print("���� �ݾ��� 10% ����, 60~65�� ����� �߰� 5% ����")
        if age in range(60,66):
            print("%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %(customer[level]*0.9*0.95))
            continue
        print("%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�."%(customer[level]*0.9))
