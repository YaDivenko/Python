def read_file():
    with open(path_file,'r',encoding='UTF-8') as f:
        for line in f:
            print(line.strip())

def write_file():
    with open(path_file,'a',encoding='UTF-8') as f:
         f.writelines('\n'+input())


def find_file():
    find_info = input()
    with open(path_file,'r',encoding='UTF-8') as f:
         for line in f:
             if find_info.casefold() in line.casefold():
                 print(line)


def change_file():
    find_info = input()
    new_info = input()
    with open(path_file,'r+',encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)
                if input("Редактируем эту запись Y/N") == "Y":
                   print (line.strip()).split(' ')
                
                else: continue


def main():
    find_file()

path_file = r'telephone.txt'

if __name__ == '__main__':
    main()