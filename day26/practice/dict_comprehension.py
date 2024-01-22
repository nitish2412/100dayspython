sentence = input()
word_list=sentence.split(" ")
result = {word:len(word) for word in word_list}
print(result)
