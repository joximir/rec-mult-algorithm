def RecMultInt(x, y):

    x = str(x)
    y = str(y)

    # base case
    if len(x)==1 or len(y)==1 :
        return int(x) * int(y)
    
    # lengths of x and y
    n = len(x)
    m = len(y)

    # halving x and y into a,b and c,d
    a = x[: n//2]
    b = x[n//2 :]
    c = y[: m//2]
    d = y[m//2 :]

    # recursively multiply ac, ad, bc and bd
    ac = RecMultInt(int(a), int(c))
    ad = RecMultInt(int(a), int(d))
    bc = RecMultInt(int(b), int(c))
    bd = RecMultInt(int(b), int(d))

    # combine adding zeros and return
    product  = ac * 10**(n//2 + m//2)
    product += ad * 10**(n//2)
    product += bc * 10**(m//2)
    product += bd
    return product
    
    
    #test
    print(a + ' ' +b)
    print(c + ' ' +d)




print(RecMultInt(123, 456))