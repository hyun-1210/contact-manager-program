# 1.출력(메뉴 제공)-생성자함수에서 while문으로 반복해서 진행
# 2. 메뉴에 따른 기능제공(1. 추가/2. 삭제/3. 검색 4. 종료 )-txt.csv에 저장할 수 있게 구현

import csv

class Contact:
    def __init__(self, name, phone_num, email):
        self.name=name
        self.phone_num=phone_num
        self.email=email
    
    def __str__(self):
        return(f'이름:{self.name}, 전화번호:{self.phone_num}, 이메일:{self.email}')
    
class ManageProgram:
    def __init__(self):
        self.contacts={}
        try:
            with open('contacts.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 3:
                        name, phone_num, email = row
                        self.contacts[name] = Contact(name, phone_num, email)
        except FileNotFoundError:
            pass 

    def start(self):
        print('연락처 관리 프로그램에 접속하셨습니다 메뉴를 골라주세요')
        while True:
            try:
                choice=int(input('1. 추가 2. 삭제 3. 검색 4. 목록 5. 종료\n'))
                if choice<=3:
                    name=input('이름을 입력하시오 ')
                    if choice==1:
                        self.add(name)
                    if choice==2:
                        self.remove(name)
                    if choice==3:
                        self.find(name)
                if choice==4:
                    self.show()
                if choice==5:
                    self.exit()
                    break
                if choice>5:
                    print('1부터 5까지의 숫자 중 하나를 입력하십시오')
            except ValueError:
                print('1부터 5까지의 숫자 중 하나를 입력하십시오')

    def add(self, name):
        if name in self.contacts:
            print('기존에 등록된 이릅입니다')
        else:
            phone_num=input('전화번호를 입력하시오 ')
            email=input('이메일을 입력하시오 ')
            self.contacts[name]=Contact(name, phone_num, email)

    def remove(self, name):
        if self.contacts.get(name)!=None:
            del(self.contacts[name])
        else:
            print('이름을 찾을 수 없습니다')
        
    def find(self, name):
        contact=self.contacts.get(name)
        if contact:
            print(contact)
        else:
            print("이름을 찾을 수 없습니다")

    def show(self):
        for contact in self.contacts.values():
            print(contact)

    def exit(self):
        with open('contacts.csv', 'w', encoding='utf-8') as f:
                writer = csv.writer(f)
                for contact in self.contacts.values():
                    writer.writerow([contact.name, contact.phone_num, contact.email])
        print('이용해주셔서 감사합니다')

    
    
def main():
    program_object=ManageProgram()
    program_object.start()

if __name__ == "__main__":
    main()
