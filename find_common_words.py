s1 = input("Please enter sentence 1: ")
s2 = input("Please enter sentence 2: ")

s1_words = set(s1.split(" "))  # split s1's words and set them in a list
s2_words = set(s2.split(" "))  # split s2's words and set them in a list
common_words = s1_words & s2_words  # compare s1_words and s2_words and store them in another list common_words
print("common words in s1 and s2 is : " + str(common_words))    # print common words
