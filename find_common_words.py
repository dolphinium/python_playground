s1 = input("Please enter sentence 1: ")
s2 = input("Please enter sentence 2: ")

s1_words = set(s1.split(" "))
s2_words = set(s2.split(" "))
common_words = s1_words & s2_words
print("common words in s1 and s2 is : " + str(common_words))
