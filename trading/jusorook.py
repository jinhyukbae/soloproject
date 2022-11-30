class Contact:

    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name      #이름
        self.phone_number = phone_number #전화번호
        self.e_mail = e_mail #이메일
        self.addr = addr #어드레스 주소

    def print_info(self): #사용자의 정보를 불러오는 함수
        print("name: {0}".format(self.name))
        print("phone number: {0}".format(self.phone_number))
        print("email: {0}".format(self.e_mail))
        print("addres: {0}".format(self.addr))

def set_contact(): #사용자가 정보 입력하는 함수
    name = input("name: ")
    phone_number = input("phone_number: ")
    e_mail = input("e_mail: ")
    addr = input("addr: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact
    #Contact 클래스의 인스턴스인 객체 contact 생성


def print_contact(contact_list):
    for contact in contact_list: #리스트에 저장된 요소를 순환함
        contact.print_info()# 순환하면서 print_info를 호출함

# contact = set_contact() #set_contact라는 메뉴 불러오는 함수를 contact에 넣고
# contact_list.append(contact) contact를 contact_list라는 리스트에 저장함
# print_info 는 이름 전화번호 이메일 집주소 출력해주는 함수


def delete_contact(contact_list, name): #연락처 리스트 contact_list와 삭제할 이름인 name을 인자로 받음
    for i, contact in enumerate(contact_list): #enumerate 리스트의 원소에 순서값을 부여해줌
        if contact.name == name: #저장된 연락처 리스트 안에 삭제하고자 하는 이름이 있으면 확인후 삭제
            del contact_list[i] #

def load_contact(contact_list): #연락처를 로드하는 함수
    f = open("contact_db.txt", "rt") #연락처를 저장하는 txt을 읽기 텍스트 모드로 오픈
    lines = f.readlines() #파일 전체를 읽는 함수를 lines에 지정 연락처 하나당 4줄의 데이터가 존재함 이름 폰번호 이메일 집주소
    num = len(lines) / 4 #lines의 요소 / 4 를 num에 넣음 전체라인수를 4로나눔
    num = int(num) #num를 정수화

    #연락처 하나당 4줄의 데이터가 존재하므로 파일에서 읽어 들인 전체 라인수를 4로 나누어 몇개의 데이터가 존재하즌지 확인
    #나눗셈 연산을 하면 num이 실수가 되므로 int로 정수

    for i in range(num): #num를 i에 담으면서 num의 요소만큼 반복
        name = lines[4*i].rstrip('\n')  # name은 제일 첫번째 이므로 line[4*i]
        phone = lines[4*i+1].rstrip('\n') # phone은 name 다음이므로 +1
        email = lines[4*i+2].rstrip('\n') # rstrip 오른쪽 공백 제거
        addr = lines[4*i+3].rstrip('\n') #\n
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact) # #contact_list에 추가
    f.close()

# for 문에서는 num의 개수만큼 루프를 돌면서 lines 리스트에 저장된 데이터를 읽어 들여
# Contact 클래스의 인스턴스를 생성하고 생성한 인스턴스를 contact_list에 추가합니다.



#contact_db 텍스트 파일을 쓰기 텍스트 모드로 열고
#사용자가 input 하면 contact_db 텍스트 파일에 작성하고 저장

def store_contact(contact_list):
    f = open("contact_db.txt", "wt") #wt = write text 쓰기 텍스트 모드
    for contact in contact_list: #사용자 입력값을 contact에 넣고 반복
        f.write(contact.name + '\n') #
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')



def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)


def run():
    contact_list = [] #빈 리스트
    load_contact(contact_list) #load_contact 함수 호출
    # 파일로 저장된 연락처를 불러오는 것은 연락처 관리 프로그램이 실행 될 때 이뤄져야 하므로 run 함수 시작하는 부분에 load_contact를 써줌
    while 1:
        menu = print_menu()
        if menu == 1: #메인 메뉴 에서 1번을 입력하면
            contact = set_contact() #객체 contact = set_contact(
            contact_list.append(contact) #contact의 값을 contact_list(빈리스트)에 넣기
        elif menu == 2: #사용자가 2번을 눌렀을 때
            print_contact(contact_list) #사용자가 입력한 값을 출력
        elif menu == 3: # 사용자가 3번을 눌렀을 때
            name = input("name: ") #이름을 입력받음
            delete_contact(contact_list, name) #딜리트 함수가 실행됨
        elif menu ==4: # 사용자가 4번을 눌렀을 때
            store_contact(contact_list)# 연락처 저장 함수
            break
if __name__ == "__main__":
    run()



