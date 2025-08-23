# 단순한 방법 시도 -> 비효율 원인 분석 -> 핵심 패턴 발견 -> 패턴에 맞는 자료구조 선택
# 정보를 반복해서 확인하지 않기 위해서 기존 정보를 저장해놓을 필요성 인지(필요하지 않은 비교는 하지 않기 위해)
# 핵심 패턴: 쌓아 두고 결국 역순으로 확인해야할 필요성 (becasue 오른쪽에서 가장 왼쪽을 노리므로 계속 첫번째 것 부터 체크하는 것 비효율)
# 약간 너 선에서 처리해 느낌 어차피 부하 선에서 처리 되면 보스까지 갈 필요가 없음.(어차피 작은 걸 안다.) 
# 이 숫자가 정말 선들을 통과했을 때 진짜 비교가 필요할 때(비교는 필요할 때만)
# 한번의 비교는 무조건 해야함. 다른 건 진짜 필요한 비교만(비교연산의 횟수를 줄이기)


import sys

class OBigNum:
    def __init__(self):
        self.N=int(sys.stdin.readline())
        self.answer=[-1]*self.N

    def start(self):
        line=sys.stdin.readline()
        numbers_list=list(map(int, line.split()))
        self.compare(numbers_list)

    def compare(self, numbers_list):
        stack=[]
        for i in range(self.N):
            number=numbers_list[i]
            while stack and numbers_list[stack[-1]]<number:
                index=stack.pop()
                self.answer[index]=number
            stack.append(i)


def main():
    o_big_num=OBigNum()
    o_big_num.start()
    for ans in o_big_num.answer:
        print(ans, end=" ")

if __name__=='__main__':
    main()
