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

print('_______________')

def deleting_a_node(x, tree, unic):
    for i in range(len(unic)):
        if unic[i] == x:
            break
    for j in range(len(tree[i])):
        if tree[i][j] == 1:
            tree[i][j] = 0
            if 1 in tree[j]:
                deleting_a_node(unic[j], tree, unic)

def new(parent, son):
    if son not in unic:
	dicUnic[son] = len(unic)
	unic.append(son)
	for i in tree:
	    i.append(0)
	tree.append([ 0 for j in range(len(unic))])
    tree[dicUnic[parent]][dicUnic[son]] = 1


# прямой обход

dad = unic[0]
def straight(tree, unic, x):
    if x == dad:
        print(x)
    for i in range(len(unic)):
        if unic[i] == x:
            break
    for j in range(len(tree)):
        if tree[i][j] == 1:
            print(unic[j])
            if 1 in tree[j]:
                straight(tree, unic, unic[j])
		

# концевой обход

def end(tree, unic, x):
    for i in range(len(unic)):
        if unic[i] == x:
            break
    if 1 in tree[i]:
        for j in range(len(tree)):
            if tree[i][j] == 1:
                break
        end(tree, unic, unic[j]) 
    else:
        print(x)
        for j in range(len(tree)):
            if tree[j][i] == 1:
                tree [j][i] = 0
                end(tree, unic, unic[j])

for i in range(len(tree)): 
    for j in range(len(tree)): 
        print(tree[i][j], end=' ')
    print('')
