def sorted_freq(s):
    if len(s) == 0:
        return ""

    char_freq = {"aa": -1}
    result = []
    maxs = s[0]

    for i in s:
        char_freq[i] = char_freq.get(i, 0) + 1
    print(char_freq)

    while(len(char_freq)):
        # print(result)
        maxs = "aa"
        for k, v in char_freq.items():
            if v > char_freq[maxs]:
                maxs = k

        result.append(maxs*char_freq[maxs])

        del char_freq[maxs]
    # print(result)
    return "".join(result)


string = "pututturkr"
# sortStr = "uuutttrrkp"
a = sorted_freq(string)
print(a)
