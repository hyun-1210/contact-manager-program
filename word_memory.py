# 영어 단어장
# 1. 자주 나오는 단어일수록 앞에 배치한다.
# 2. 해당 단어의 길이가 길수록 앞에 배치한다.
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.
# M보다 짧은 단어는 단어장에 넣지 않는다.

# 단어장을 dict로 만들고 key에 따라 밸류값을 추가하자->1번
# 밸류값에 따라 내림차순 sort 정렬하자 
# 밸류값이 같다면 key의 길이를 비교하자 
# 길이가 같다면 key를 알파벳 순으로 정렬하자
# 이 세가지를 따로 할 필요 없이 튜플 정렬을 활용해 한번에 할 수 있다.

import sys

class WordBook:
    def __init__(self):
        self.wordlist={}
    def fill(self, word_num, memory_standard):
        for i in range(word_num):
            word=sys.stdin.readline().strip()
            if len(word)>=memory_standard:
                self. wordlist[word]=self.wordlist.get(word, 0)+1
    def sort(self):
        sorting_list=sorted(self.wordlist.items(),key= lambda x:(-x[1], -len(x[0]), x[0]))
        return sorting_list

def main():
    word_num, memory_standard=map(int, sys.stdin.readline().split())
    wordbook=WordBook()
    wordbook.fill(word_num, memory_standard)
    answer_list=wordbook.sort()
    for ans in answer_list:
         sys.stdout.write(ans[0] + '\n')


if __name__=='__main__':
    main()