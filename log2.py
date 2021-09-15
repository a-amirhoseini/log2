def log2(nu):
    num = int(nu)
    num_log2 = ''
    while num >= 1 :
        num_log2 = str(num % 2) + num_log2
        num = num // 2
    return " عدد شما در مبنای 2 : " + num_log2 + " است. "
