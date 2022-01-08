def reverse_num(number, ans):
    if number == 0:
        return ans
    ans += str(number % 10)
    return reverse_num(number // 10, ans)

print(reverse_num(34860, ''))
