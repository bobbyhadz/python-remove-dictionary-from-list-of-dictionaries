# Remove a dictionary from a list of dictionaries in Python

my_list = [
    {'id': 1, 'fruit': 'apple'},
    {'id': 2, 'fruit': 'banana'},
    {'id': 3, 'fruit': 'kiwi'},
]

for item in my_list.copy():
    if item.get('id') == 2:
        my_list.remove(item)
        break

# 👇️ [{'id': 1, 'fruit': 'apple'}, {'id': 3, 'fruit': 'kiwi'}]
print(my_list)