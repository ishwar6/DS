# A1, A2, A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15]
# Output – [A1,A15,A2,A3,A14,A4,A5,A6,A13,A7,A8,A9,A10,A12,A11].
# Sample Input – [2,5,9,10,45,2,34,13,49,20,].
# Output – [2,20,5,9,49,10,45,2,13,34].

def list_print(mylist):
    l, r = 1, len(mylist)
    res = []
    prev = 0
    res.append(mylist[0])

    for i in range(1, len(mylist)):
        r -= 1
        if len(res) <= len(mylist):
            res.append(mylist[r])

        # increment l by i units
        prev = l
        l = l + i+1
        # print(prev, l)
        if l < len(mylist) and len(res) < len(mylist):
            for k in range(prev, l):
                res.append(mylist[k])

        # decrease j by one unit
    return res


a = list_print(list(range(1, 31)))
print(a)


Msg(Msg_id, user_id, text, file, timestamp)

OneToOneChat(user_id_1, user_id_2, timestamp, Msg_id)

GroupChat(GroupChat_id, list_of_user_ids, host_user_id, Msg_id, timestamp)

State(User_id, GroupChat_id, is_active, is_muted)

GroupMsg(GroupChat_id, Msg_id)
