"""
Pattern program will print the arrow head
shape of specififed size which is passed as an argument
"""     
def print_arrow_headv2(n, multiplicity):
    i = 0
    j = 0
    count = 0
    while i != n:
        print('*'*i)
        if i == n-1:
            while i!= -1:
                j = i
                print('*'*j)
                i -= 1
        i += 1
        count += 1
        if count == multiplicity:
            break             


def main():
    n = int(input("Enter maximum size for arrow: "))    
    print("Method 3 for full arrow")
    print_arrow_headv2(n,2*n)


if __name__ == '__main__':
    main()
