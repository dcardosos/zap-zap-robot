with open('codes.txt', 'r', encoding='utf8') as f:
    codes = [code.strip() for code in f.readlines()]

print(codes)
