tree = [[ 0 for j in range(10)] for i in range(10)] 

def file1(): 
    with open('input.txt', 'r') as f: 
        for line in f: 
            main = '' 
            for x in line: 
                if main == '': 
                    main = x 
                elif x != ' ' and x != '\n': 
                    tree[int(main)][int(x)] = 1 

file1() 

for i in range(len(tree)): 
    for j in range(len(tree)): 
        print(tree[i][j], end=' ')
    print('')
