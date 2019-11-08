from xml.etree.ElementTree import parse

tree = parse("students_info.xml")
student_list = tree.getroot()

def summary_info():

    while True:
        for student in student_list.getiterator("student"):
            print(student.get("name"))
            print("성별 : %s" %student.get("sex"))
            print("전공 : %s" %student.find("major").text)
            for practicable_computer_languages in student.getiterator("practicable_computer_languages"):
                count=0
                for language in practicable_computer_languages.getiterator("language"):
                    for period in language.getiterator("period"):
                        print("사용 가능한 컴퓨터 언어 %s(학습기간: %s, Level:%s)" %(language.get("name"), period.get("value"), language.get("level")))
                    count = 1
                if count !=1:
                    print("사용 가능한 컴퓨터 언어: 없음")
        break
def data_inquiry():
    people = 0
    male = 0
    female = 0
    engineering = 0
    while True:
        for student in student_list.getiterator("student"):
            people += 1
            if student.get("sex")=='남':
                male +=1
            elif student.get("sex")=='여':
                female +=1
            elif student.get("major")=='컴퓨터 공학''통계빅데이터':
                engineering +=1
            for practicable_computer_languages in student.getiterator("practicable_computer_languages"):
                pass


def main():
    menu = '''
        1.요약정보
        2.전체 데이터 조회
        3.종료
    '''

    while True:
        print("학생정보 XML데이터 분석 시작")
        menu = int(input(menu))
        if menu == 1:
            summary_info()
        elif menu == 2:
            data_inquiry()
        elif menu == 3:
            print("학생 정보 분석 완료")
            break
        else:
            print("1~3까지의 수를 입력해주세요")

main()