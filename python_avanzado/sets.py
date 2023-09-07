set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


print(f'''

NUMERIC SETS:
    SET 1: {set1}
    SET 2: {set2}
''')
print(f'''

STRING SETS:
    SET 1: {set_str1}
    SET 2: {set_str2}
''')

example_list = [9, 10]
print(f'''
CASTING SETs:

    LIST to SET: {set(example_list)}
''')


set1.add(6)
print(f'''
ADD ELEMENTS:
    set + 6: {set1}
''')

set1.update([6, 7])
print(f'''
UPDATE SET:
    set + 6, 7: {set1}
        # 6 will be omited because this exist
''')

set1.remove(6)
print(f'''
REMOVE or DISCARD element:

    with REMOVE method:
        set - 6: {set1}
''')

set1.discard(7)
print(f'''
    with DISCARD method:
        set - 7: {set1}
''')

set1.pop()
print(f'''
REMOVE RAMDOM ELEMENT:
    {set1}
''')

set1.clear()
print(f'''
REMOVE ALL ELEMENTS:
    {set1}
''')