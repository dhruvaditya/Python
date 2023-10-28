def process(max_tries=1000):
    for a in range(11, 100):
        x = a
        for n in range(max_tries):
            x = x + int(str(x)[::-1])
            if str(x) == str(x)[::-1]:  # stackoverflow.com/questions/17331290
                if (n > 20):  # 89 23, 98 23
                    print(a, n)
                break

process()