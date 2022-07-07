import re


cats = [
    {'id': 1, 'name': 'Zelda', 'age': 3},
    {'id': 2, 'name': 'Tigerlily', 'age': 9},
    {'id': 3, 'name': 'Salem', 'age': 500}
]


# for c in cats:
#     print(c)

for c in cats:
    print(c['id'])


def christest():
    for c in cats:
        c

print (christest)



# new_cat = {'name': 'xargon', 'age':999 }

# just_mem_adr = (c for c in cats)
# print('1',just_mem_adr)






# print(c for c in cats)

# just_list = ([c['id'] for c in cats])
# print(just_list)

# sorted_array = sorted(c['id'] for c in cats)
# print(sorted_array)

# new_id = sorted(c['id'] for c in cats)[-1] + 1
# print(new_id)

# new_cat['id'] = new_id
# cats.append(new_cat)

# print(cats)