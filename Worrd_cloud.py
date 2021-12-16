# LEARNER CODE START HERE

file_kc = ""
for index, char in enumerate(file_contents):
    if (char.isalpha() == True or char.isspace()):
        file_c += char
file_kc = file_kc.split()
file_ky = []

for word in file_kc:
    if word.lower() not in uninteresting_words and word.isalpha() == True:
        file_ky.append(word)
frequency = {}

for word in file_ky:
    if word.lower() not in frequency:
        frequency[word.lower()] = 1
    else:
        frequency[word.lower()] += 1
# print(result)