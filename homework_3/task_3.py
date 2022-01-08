from hashlib import sha256

def finding_substrings(s):
    hash_set = set()
    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            if s == s[i:j]:
                break
            result = sha256(s[i:j].encode()).hexdigest()
            hash_set.add(result)
    return len(hash_set), hash_set

str = input("Введите слово: ")
print(finding_substrings(str))

