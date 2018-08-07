##finding most common word's in a lists
from collections import Counter
words = [
'look' , 'into' , 'my' , 'eyes' , 'look' , 'into' , 'my' , 'eyes' ,
'the' , 'eyes' , 'the' , 'eyes' , 'the' , 'eyes' , 'not' , 'around' , 'the' ,
'eyes' , "don't" , 'look' , 'around' , 'the' , 'eyes' , 'look' , 'into' ,
'my' , 'eyes' , "you're" , 'under'
]

list_count = Counter(words)     #Counter will convert this list into map here list_count is map

most_common_threee = list_count.most_common(3)

print("Most common three ",most_common_threee)
