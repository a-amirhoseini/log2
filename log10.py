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
