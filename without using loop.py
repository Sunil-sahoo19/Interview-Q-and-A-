
def p(n=1):
    if n > 100:
        return
    print(n)
    p(n + 1)
p()