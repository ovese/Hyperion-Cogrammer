# this file demnstrates python string replace function
test_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog"

# use replace to remove all instances of the !
new_sentence = test_sentence.replace("!", " ")
print(new_sentence)

# converting the new sentence to upper case
upper_sentence = new_sentence.upper()
print(upper_sentence)

# reversing the new sentence using the strig indexing
reversed_sentence = new_sentence[::-1]
print(reversed_sentence)