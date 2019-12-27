def count():
    with open("input.txt", "r") as f:
        a = []
        for i in f.read().split('\n'):
            a += i.split()
    return(len(set(a)))

x = count()

def create(count):
    tree = [[ 0 for j in range(count)] for i in range(count)]
    unic = []
    dicUnic = {}
    f = open('input.txt','r')
    for line in f:
        main = ''
        num  = ''
        for a in line:
            if a not in (' ', '\n'):
                num += a
            else:
                if int(num) not in unic:
                    unic.append(int(num))
                    dicUnic[int(num)] = len(unic)-1
                if not main:
                    main = num
                    num = ''
                else:
                    tree[dicUnic[int(main)]][dicUnic[int(num)]] = 1
                    num = ''
    f.close()
    return tree, dicUnic, unic
tree, dicUnic, unic = create(x)
print(tree)
print(unic)

for i in range(len(tree)): 
    for j in range(len(tree)): 
        print(tree[i][j], end=' ')
    print('')
