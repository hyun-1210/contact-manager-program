import sys
import collections

class SpinQueue:
    def __init__(self):
        self.queue=collections.deque()

    def make_queue(self, queue_size):
        for i in range(queue_size):
            self.queue.append(i+1)

    def find_nums(self, find_list):
        answer=0
        for num in find_list:
            num= int(num)
            location=self.queue.index(num)
            if location<len(self.queue)/2:
                answer+=location
                self.queue.rotate(-location)
            else:
                location=len(self.queue)-location
                answer+=(location)
                self.queue.rotate(location)
            self.queue.popleft()
# "파이썬 for/while 루프를 최소화하고, 가능한 한 많은 작업을 최적화된 내장 함수에게 한 번에 맡기는 것
# 반성할 점: 사고 과정에서 인덱스 내장 함수가 있을 거라 생각을 안하고 안찾아봄
        return answer


def main():
    spin_queue=SpinQueue()
    NM_list=sys.stdin.readline().split()

    queue_size=int(NM_list[0])

    find_list=sys.stdin.readline().split()

    spin_queue.make_queue(queue_size)
    print(spin_queue.find_nums(find_list))



if __name__=='__main__':
    main()


