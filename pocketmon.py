import sys

class Pocketmon:
    def __init__(self):
        self.dict_num_key={}
        self.dict_monster_key={}
    def save(self,monster, num):
        self.dict_num_key[num]=monster
        self.dict_monster_key[monster]=num
    def find(self, query):
        if query.isdigit():
            return self.dict_num_key[int(query)]
        else:
            return self.dict_monster_key[query]

def main():
    pocketmon=Pocketmon()
    parts=sys.stdin.readline().split()
    save_numbers=int(parts[0])
    find_numbers=int(parts[1])
    for i in range(save_numbers):
        num=i+1
        pocketmon.save(sys.stdin.readline().strip(), num)
    for i in range(find_numbers):
        query=sys.stdin.readline().strip()
        print(pocketmon.find(query))

if __name__=='__main__':
    main()