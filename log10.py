def log2(nu):
    num = int(nu)
    num_log2 = ''
    while num >= 1 :
        num_log2 = str(num % 2) + num_log2
        num = num // 2
    return " عدد شما در مبنای 2 : " + num_log2 + " است. "
# مثال:
number = input('لطفا عدد خود را در مبنای 10 وارد کنید تا ما آن را در مبنای 2  تحویل دهیم:  ')
print(log2(number))

def log10(nu):
    num = nu[::-1]
    num_log10 = 0
    dor = 0
    for n in num:
        if not int(n) == 0 :
            num_log10 += 2 ** dor
        dor += 1
    return ' عدد شما در مبنای 10 ' + str(num_log10) + ' می باشد. '

# مثال:
number = input('لطفا عدد خود را در مبنای 2 وارد نمایید تا آن را در مبنای 10 تحویل دهیم:  ')
print(log10(number))
