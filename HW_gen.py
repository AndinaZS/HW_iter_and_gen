#генератор со *, задание без * тоже выполняет
def flat_generator(obj_list):
    flag = True
    while flag:
        flag = False
        for num, el in enumerate(obj_list):
            if not isinstance(el, list):
                yield el
            else:
                obj_list = el + obj_list[num + 1:]
                flag = True
                break
        continue


nested_list = [['a', 'b', 'c', [1, 2]],
	['d', 'e', 'f', 'h', False, ['e', 'f', [1, 2], 'h'], ],
	[1, 2, 3, [4]]
]

print(list(flat_generator(nested_list)))
