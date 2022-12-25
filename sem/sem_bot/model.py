def abc_del(message):
    find_txt='абв'
    lst=[i for i in message.split() if find_txt not in i]
    return "".join(lst)
