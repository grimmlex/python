def pig_it(text):
    res = []
    split_text = text.split()
    for item in split_text:
        if item.isalpha():
            res.append(item[1:] + item[0] + "ay")
            print(item[1:] + item[0] + "ay")
        else:
            res.append(item)
    return " ".join(res)

print(pig_it('Pig latin is cool !'))