import random

class Numbers:
    def __init__(self):
        self.nums = random.sample(range(0, 10), 4)
    def count(self, arr):
        strikes=0
        balls=0
        for i in range(4):
            if self.nums[i] == arr[i]:
                strikes+=1
            else:
                for j in [x for x in range(4) if x!=i]:
                    if self.nums[i] == arr[j]:
                        balls+=1
        out=(strikes==0 and balls==0)
        return strikes, balls, out
        
def main():
    Num=Numbers()
    try_nums=0
    strikes=0

    while strikes!=4:
        try_list = list(map(int, input('0~9 사이에 4개의 숫자를 입력해주세요: ').split()))
        strikes, balls, out = Num.count(try_list)
        if out:
            print("아웃")
        else:
            print(f"{strikes} 스트라이크 {balls} 볼")
        try_nums+=1

    print(f"정답입니다! 소요횟수: {try_nums}")

if __name__ == "__main__":
    main()
            
                


        

