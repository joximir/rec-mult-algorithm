def RecMultInt(x, y):
    """Muliplies two positive integers via D&C recursion"""

    # base case
    if len(str(x))==1 or len(str(y))==1 :
        return int(x) * int(y)
    
    # lengths of x and y...
    x = str(x)
    y = str(y)
    n = len(x)
    m = len(y)

    # ...and their 'ceil' halves used for combining parts
    nby2 = n//2 + 1 if n%2 == 1 else n//2
    mby2 = m//2 + 1 if m%2 == 1 else m//2

    # halving x and y into a,b and c,d 
    #   using 'floor' halves of lengths
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
    product  = ac * 10**(nby2 + mby2)
    product += ad * 10**(nby2)
    product += bc * 10**(mby2)
    product += bd
    return product
    
print(str(RecMultInt(123156, 12987)) + ' tacno je ' + str(123156*12987))