def kt(n):
    if ('888' in n) or (n[0] == '8'):
        return "NO"
    for c in n:
        if c != '6' and c != '8':
            return "NO"
    return "YES"

print(kt(input()))
