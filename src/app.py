##finding most common word's in a lists
from collections import Counter
words = [
'look' , 'into' , 'my' , 'eyes' , 'look' , 'into' , 'my' , 'eyes' ,
'the' , 'eyes' , 'the' , 'eyes' , 'the' , 'eyes' , 'not' , 'around' , 'the' ,
'eyes' , "don't" , 'look' , 'around' , 'the' , 'eyes' , 'look' , 'into' ,
'my' , 'eyes' , "you're" , 'under'
]

list_count = Counter(words)     #Counter will convert this list into map here list_count is map
print("This is map and its key is : ",list_count['eyes'])

most_common_threee = list_count.most_common(3)

print("Most common three ",most_common_threee)


#more words
more_wors = ['why', 'are', 'you', 'not', 'looking', 'into', 'my', 'eyes']
count = 0
for word in more_wors:
    list_count[word] +=1
print(" This is just word count : ", list_count['eyes'])

# there is alternate to this method which is update()

more_wors = ['why', 'are', 'you', 'not', 'looking', 'into', 'my', 'eyes']

list_count.update(more_wors)

print("This is map and its key is : ",list_count['eyes'])
