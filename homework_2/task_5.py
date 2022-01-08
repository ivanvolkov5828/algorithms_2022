def table(start, finish, count=0, answer=''):
    if start == finish:
        return answer

    if count == 10:
        count = 0
        print(answer)
        answer = ''
    return table(start + 1, finish, count + 1, answer + f'{start} - {chr(start)} ')

print(table(32, 128))