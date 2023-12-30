"""
Pattern program will print the arrow head
shape of specififed size which is passed as an argument
"""
# max_len = input("Enter the shape size: ")
# shape_size = int(max_len)

# for i in range(1,shape_size):
#     print(i*'*')


# this function prints the top part of the arrow
def print_arrow_asc(start, stop):
    for i in range(start, stop):  # default counts up in increments of 1
        print(i*'*')
        # if i == stop-1:
        #     temp = start
        #     start = stop-1
        #     stop = temp
        #     print("Swapped start and stop position here")
        # for j in range(start-i, stop):
        #     print(j*'*')


# tis functions prints bottoom part of the arrow
def print_arrow_desc(start, stop):

    for i in range(start, stop-1, -1):  # decrementing by 1
        print(i*'*')


def main():
    start_val = 1  # the start val will always be 1 in this case
    end_val = input("Enter maximum size for arrow: ")
    stop_val = int(end_val)

    print_arrow_asc(start_val, stop_val)
    print_arrow_desc(stop_val, start_val)


if __name__ == '__main__':
    main()
