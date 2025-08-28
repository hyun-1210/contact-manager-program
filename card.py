import sys
import collections

class Card:
    def __init__(self, card_nums):
        self.card_queue=collections.deque()
        for i in range(card_nums):
            self.card_queue.append(i+1)

    def start(self):
        while len(self.card_queue)!=1:
            self.card_queue.popleft()
            self.card_queue.append(self.card_queue.popleft())
        print(self.card_queue[0])


def main():
    card_nums=int(sys.stdin.readline())
    card=Card(card_nums)
    card.start()

if __name__== '__main__':
    main()