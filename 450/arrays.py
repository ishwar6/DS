my_str = 'A unicode \u018e \u1F6e string \xf1'
print(my_str)


def IsUnique(string) -> bool:
    if len(string) > 128:
        return False
    array = [False for i in range(128)]
    for i in string:
        if array[ord[i]]:
            return False
        array[ord[i]] = True
    return True


def IsUnique(string):
    # if UTF-8 vs ASSCI
