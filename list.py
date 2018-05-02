from itertools import groupby
from nltk.corpus import stopwords
'listing all the words from the text file'
def listing(filename):
    open_file = open(filename, 'r')
    words_list =[]
    contents = open_file.readlines()
    for i in range(len(contents)):
        words_list.extend(contents[i].split())

    return words_list

'removing duplicate words from the above list'
def no_duplicates(words_list):
    no_duplicates = []
    seen = set()
    for word in words_list:
        if word not in seen:
            no_duplicates.append(word)
            seen.add(word)
    return no_duplicates


def w_plus_1(input,words_list,no_duplicates):
    w_plus_1_list = []
    w_count = []
    count = 0
    bigram_list = []
    for i in range(len(words_list) - 1):
        bigram_list.append((words_list[i], words_list[i + 1]))
    for i in range(len(no_duplicates) - 1):
        w_plus_1_list.append((input,no_duplicates[i]))
    for i in range(len(w_plus_1_list) - 1):
        for j in range(len(bigram_list) - 1):
            if(w_plus_1_list[i]==bigram_list[j]):
                count = count+1
                w_count.append(w_plus_1_list[i])
    #print("w+1:")
    return w_count


def w_minus_1(input, words_list, no_duplicates):
    w_minus_1_list = []
    count = 0
    w_count = []
    bigram_list = []
    for i in range(len(words_list) - 1):
        bigram_list.append((words_list[i], words_list[i + 1]))
    for i in range(len(no_duplicates) - 1):
        w_minus_1_list.append((no_duplicates[i],input))
    for i in range(len(w_minus_1_list) - 1):
        for j in range(len(bigram_list) - 1):
            if (w_minus_1_list[i] == bigram_list[j]):
                count = count + 1
                w_count.append(w_minus_1_list[i])
    #print("w-1:")
    return w_count


def w_plus_2(input, words_list, no_duplicates):
    w_plus_2_list = []
    count = 0
    bigram_list = []
    w_count = []
    for i in range(len(words_list)):
        bigram_list.append((words_list[i - 2], words_list[i]))
    for i in range(len(no_duplicates)):
        w_plus_2_list.append((input,no_duplicates[i]))
    for i in range(len(w_plus_2_list)):
        for j in range(len(bigram_list)):
            if (w_plus_2_list[i] == bigram_list[j]):
                count = count + 1
                w_count.append(w_plus_2_list[i])
    #print("w+2:")
    return w_count

def w_minus_2(input, words_list, no_duplicates):
    w_plus_2_list = []
    count = 0
    bigram_list = []
    w_count = []
    for i in range(len(words_list) -1):
        bigram_list.append((words_list[i -2], words_list[i]))
    for i in range(len(no_duplicates)):
        w_plus_2_list.append((no_duplicates[i],input))
    for i in range(len(w_plus_2_list)):
        for j in range(len(bigram_list)):
            if (w_plus_2_list[i] == bigram_list[j]):
                count = count + 1
                w_count.append(bigram_list[j])
    #print("w-2:")
    return w_count

def bigram_1(input, words_list, no_duplicates):
    bigram_1_list = []
    bigram_1 = []
    bigram_1_final = []
    count = 0
    for i in range(len(words_list) - 1):
        bigram_1_list.append((words_list[i],(words_list[i],words_list[i+1])))
    for i in range(len(no_duplicates) - 1):
        bigram_1.append((input,(input,no_duplicates[i])))
    for i in range(len(bigram_1)):
        for j in range(len(bigram_1_list)):
            if(bigram_1[i] == bigram_1_list[j]):
                bigram_1_final.append(bigram_1_list[i])
                count = count+1
    #print("bigram1:")
    return bigram_1_final

def bigram_2(input, words_list, no_duplicates):
    bigram_1_list = []
    bigram_1 = []
    bigram_1_final = []
    count = 0
    for i in range(len(words_list) - 1):
        bigram_1_list.append(((words_list[i],words_list[i+1]),input))
    for i in range(len(no_duplicates) - 1):
        bigram_1.append(((no_duplicates[i],input),input))
    for i in range(len(bigram_1)):
        for j in range(len(bigram_1_list)):
            if(bigram_1[i] == bigram_1_list[j]):
                bigram_1_final.append(bigram_1_list[i])
                count = count+1
    #print("bigram2:")
    return bigram_1_final

input1 = raw_input("enter the target word:\n")
input2 = raw_input("enter the target word:\n")

words_list = listing("filteredtext.txt")
no_duplicates = no_duplicates(words_list)
sw = set(stopwords.words('english'))
fs = [w for w in words_list if not w in sw]

for w in words_list:
    if w not in sw:
        fs.append(w)
#input1 = "Kim"
#input2 = "West"

#print("for input 1:")
w_plus_1_count1 = w_plus_1(input1,fs,no_duplicates)
#print(w_plus_1_count1)

w_minus_1_count1 = w_minus_1(input1,fs,no_duplicates)
#print(w_minus_1_count1)

w_plus_2_count1 = w_plus_2(input1, fs, no_duplicates)
#print(w_plus_2_count1)

w_minus_2_count1 = w_minus_2(input1, fs, no_duplicates)
#print(w_minus_2_count1)

bigram_1_count1 = bigram_1(input1,fs,no_duplicates)
#print(bigram_1_count1)

bigram_2_count1 = bigram_2(input1, fs, no_duplicates)
#print(bigram_2_count1)

#print("for input 2:")
w_plus_1_count2 = w_plus_1(input2,fs,no_duplicates)
#print(w_plus_1_count2)

w_minus_1_count2 = w_minus_1(input2,fs,no_duplicates)
#print(w_minus_1_count2)

w_plus_2_count2 = w_plus_2(input2, fs, no_duplicates)
#print(w_plus_2_count2)

w_minus_2_count2 = w_minus_2(input2, fs, no_duplicates)
#print(w_minus_2_count2)

bigram_1_count2 = bigram_1(input2, fs, no_duplicates)
#print(bigram_1_count2)

bigram_2_count2 = bigram_2(input2, fs, no_duplicates)
#print(bigram_2_count2)

six_list1 = [w_plus_1_count1,w_minus_1_count1,w_plus_2_count1,w_minus_2_count1,bigram_1_count1,bigram_2_count1]
six_list2 = [w_plus_1_count2,w_minus_1_count2,w_plus_2_count2,w_minus_2_count2,bigram_1_count2,bigram_2_count2]

#print(six_list1)
#print(six_list2)
six_list1_c = [len(w_plus_1_count1),len(w_minus_1_count1),len(w_plus_2_count1),len(w_minus_2_count1),len(bigram_1_count1),len(bigram_2_count1)]
print("count of six lists for input 1")
print(six_list1_c)

six_list2_c = [len(w_plus_1_count2),len(w_minus_1_count2),len(w_plus_2_count2),len(w_minus_2_count2),len(bigram_1_count2),len(bigram_2_count2)]
print("count of six lists for input 2")
print(six_list2_c)

combined_list = []
for i in range(0,6):
    combined_list.append((six_list1[i],six_list2[i]))
#print(combined_list)
l = len(combined_list)
f12 = 0
f21 = 0
#print(l)
cl=(input1,input2)
new_list1 = []

for i in range(6):
    if(i==0):
        for j in range(len(w_plus_1_count1)):
            for k in range(len(w_plus_1_count1)):
                for m in range(len(w_plus_1_count1)):
                    if((combined_list[i][j][k][m])==input2):
                        f12 = f12 + 1
                        new_list1.append(combined_list[i][j][k][m])
    elif(i==1):
        for j in range(len(w_minus_1_count1)):
            for k in range(len(w_minus_1_count1)):
                for m in range(len(w_minus_1_count1)):
                    if((combined_list[i][j][k][m])==input2):
                        f12 = f12 + 1
                        new_list1.append(combined_list[i][j][k][m])
    elif(i==2):
        for j in range(len(w_plus_2_count1)):
            for k in range(len(w_plus_2_count1)):
                for m in range(len(w_plus_2_count1)):
                    if((combined_list[i][j][k][m])==input2):
                        f12 = f12 + 1
                        new_list1.append(combined_list[i][j][k][m])
    elif(i==3):
        for j in range(len(w_minus_2_count1)):
            for k in range(len(w_minus_2_count1)):
                for m in range(len(w_minus_2_count1)):
                    if((combined_list[i][j][k][m])==input2):
                        f12 = f12 + 1
                        new_list1.append(combined_list[i][j][k][m])
    elif(i==4):
        for j in range(len(bigram_1_count1)):
            for k in range(len(bigram_1_count1[j])):
                if (combined_list[i][j][k][0] == input2):
                    f12 = f12 + 1
                    new_list1.append(combined_list[i][j][k][0])
    elif(i==5):
        for j in range(len(bigram_2_count1)):
            for k in range(len(bigram_2_count1[j])):
                if (combined_list[i][j][k][1] == input2):
                    f12 = f12 + 1
                    new_list1.append(combined_list[i][j][k][1])
print("list 1 contains input2 :")
print(f12)

new_list2 = []

for i in range(6):
    if(i==0):
        for j in range(len(w_plus_1_count2)):
            for k in range(len(w_plus_1_count2)):
                for m in range(len(w_plus_1_count2)):
                    if((combined_list[i][j][k][m])==input1):
                        f21 = f21 + 1
                        new_list2.append(combined_list[i][j][k][m])
    elif(i==1):
        for j in range(len(w_minus_1_count2)):
            for k in range(len(w_minus_1_count2)):
                for m in range(len(w_minus_1_count2)):
                    if((combined_list[i][j][k][m])==input1):
                        f21 = f21 + 1
                        new_list2.append(combined_list[i][j][k][m])
    elif(i==2):
        for j in range(len(w_plus_2_count2)):
            for k in range(len(w_plus_2_count2)):
                for m in range(len(w_plus_2_count2)):
                    if((combined_list[i][j][k][m])==input1):
                        f21 = f21 + 1
                        new_list2.append(combined_list[i][j][k][m])
    elif(i==3):
        for j in range(len(w_minus_2_count2)):
            for k in range(len(w_minus_2_count2)):
                for m in range(len(w_minus_2_count2)):
                    if((combined_list[i][j][k][m])==input1):
                        f21 = f21 + 1
                        new_list2.append(combined_list[i][j][k][m])
    elif(i==4):
        for j in range(len(bigram_1_count2)):
            for k in range(len(bigram_1_count2[j])):
                if(combined_list[i][j][k][0]==input1):
                    f21 = f21 + 1
                    new_list2.append(combined_list[i][j][k][0])
    elif(i==5):
        for j in range(len(bigram_2_count2)):
            for k in range(len(bigram_2_count2[j])):
                if (combined_list[i][j][k][1] == input1):
                    f21 = f21 + 1
                    new_list2.append(combined_list[i][j][k][1])
print("list 2 contains input1:")
print(f21)

p1 = f12//len(w_minus_1_count1)
p2 = f21//len(w_minus_1_count2)
print("frequency divided by size of w-1 list for input 1:")
print(p1)
print("frequency divided by size of w-1 list for input 2:")
print(p2)

func = max(p1,p2)
print("max of parameter 1 and 2:")
print(func)
print("the context similarity obtained using distributional context is:")
y = 0.1*func
print(y)