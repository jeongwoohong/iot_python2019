import json

def student_info_input():
    pass
def student_info_inquiry():
    with open('ITT_Student.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)

    menu = '''
        1.전체 학생정보 조회
        검색 조건 선택
        2.ID검색
        3.이름 검색
        4.나이 검색
        5.주소 검색
        6.과거 수강 횟수 검색
        7.현재 강의를 수강중인 학생
        8.현재 수강 중인 강의명
        9.현재 수강 강사
        10.이전 메뉴
        메뉴를 선택하세요 : '''
    i=0
    while True:
        menu = int(input(menu))
        if menu==1:
            while i<len(g_json_big_data):
                print("*학생 ID :%s" %g_json_big_data[i]['student_ID'])
                print("*나이 : %s" %g_json_big_data[i]['student_age'])
                print("*이름 : %s" %g_json_big_data[i]['student_name'])
                print("*주소 : %s" %g_json_big_data[i]['address'])
                print("*수강 정보")
                print(" +과거 수강 횟수 : %s"%g_json_big_data[i]['total_course_info']['num_of_course_learned'])
                print(" +현재 수강 과목")
                for course_dict in g_json_big_data[i]['total_course_info']['learning_course_info']:
                    print(" 강의 코드 : %s" % course_dict['course_code'])
                    print(" 강의명 : %s"% course_dict['course_name'])
                    print(" 강사 : %s"% course_dict['teacher'])
                    print(" 개강일 : %s"% course_dict['open_date'])
                    print(" 종료일 : %s"% course_dict['close_date'])
                i+=1
        elif menu==2:pass
        elif menu==3:pass
        elif menu==4:pass
        elif menu==5:pass
        elif menu==6:pass
        elif menu==7:pass
        elif menu==8:pass
        elif menu==9:pass
def student_info_modify():
    pass

def student_info_delete():
    pass

def main():
    menu='''
        1.학생 정보입력
        2.학생 정보조회
        3.학생 정보수정
        4.학생 정보삭제
        5.프로그램 종료
        메뉴를 입력하세요 :'''

    while True:
        menu = int(input(menu))
        if menu ==1:
            student_info_input()
        elif menu ==2:
            student_info_inquiry()
        elif menu ==3:
            student_info_modify()
        elif menu ==4:
            student_info_delete()
        elif menu ==5:
            break
        else:
            print("1~5까지의 숫자만 입력하세요")
main()