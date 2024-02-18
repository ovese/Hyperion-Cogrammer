def duplicate_encode(word):
    """ This code is meant to test the encoding
        of charcters in a word such that if the charcater
        occurs once we use a '(' and if more than once ')'
    """
    word_list = list(word)
    len_word = len(word_list)
    print(len_word)
    print(word_list)
    alph_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
    letter_count = 0
    word_dict = {}
    word_found = []
    i = len_word
    while i != 0:
        if word_list[i] == {item : item for item in alph_list} :
            print(f"{word[i]}: {i}")
            word_found.append(f"{word[i]}:{i}")
    print(word_found)

def open_or_senior(data):
    len_data = len(data)
    print(len_data)
    len_data_i = len(data[0])
    print(len_data_i)
    print()
    for i in range(len_data):
        for j in range(len_data_i):
            print(data[i][j])
            if data[i][j]
        
    #return

def main():
    # duplicate_encode('salamandeer')
    input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
    open_or_senior(input)

if __name__ =='__main__':
    main()



##for i, (key,value) in enumerate({}):
##    print(i,key,value)
##    
##for i, (key,value) in enumerate(my_dict.items()):
##    print(i,key,value)
