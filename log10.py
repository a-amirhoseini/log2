def log10(nu):
    num = nu[::-1]
    num_log10 = 0
    dor = 0
    for n in num:
        if not int(n) == 0 :
            num_log10 += 2 ** dor
        dor += 1
    return ' عدد شما در مبنای 10 ' + str(num_log10) + ' می باشد. '
