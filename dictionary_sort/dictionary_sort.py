data = {'hello': ['doc1'], 'my': ['doc1'], 'name': ['doc1'], 'is': ['doc1', 'doc2'], 'james': ['doc1', 'doc2'],
'a': ['doc2'], 'developer': ['doc2']}

def sort_list_with_tuples(data):
 
    # creating a list with list comprehension using dictionary sorting 
    # dictionary sorting is done with 2 conditions: 1.Primary sort by length of value, 2.secondary sort by 
    
    list_sorted = [(k, v) for k, v in sorted(data.items(), key=lambda item: (len(item[1]),item[0]),reverse = False)]
    
    print(list_sorted)
    
    
#calling the sorting function with the input data
sort_list_with_tuples(data)