num =0 
s = 0.0

while True:
    sval = input('Enter a number')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num = num + 1
    s = s + fval

print(s, num, s/num)

