from numbers import Number

class Polynomial:


    def  __init__(self, coefs):

        self.coefficients = coefs

    def degree(self):

        return len(self.coefficients) - 1
    
    def __str__(self): # __str__ to represent the variable
                       # called by 'print' or 'str'
        
        coefs = self.coefficients
        terms = [] 

        if coefs[0]: # terms 在前 condition 放后
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]: 
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x") # " f with "" " 
                                                                  # string counts EVERYUNIT in the quote

        # common rule for higher degrees:
        terms += [f"{'' if c == 1 else c}x^{d}" # nothing between ''
                 for d, c in enumerate(coefs[2:], start = 2) if c] # 'if c': leaving out the term if c==0
                                                                   # '[]' co include an 'if' condition
                                                                   # 'enumerate' gives 2 loop variables
        return " + ".join(reversed(terms)) or "0" # 'join' but descending # 'reversed' so ascending order
                                                  # " or "0" " so that python gives 0 if coefs[] == 0

    def __repr__(self): # __repr__ : default string representation: ' "" ' with '+'

        return type(self).__name__+ "(" + repr(self.coefficients) + ")" # 'type(self).__name__': class name
    
    ## whether 2 objects are actually the same
    def __eq__(self, other): # other : which we compare to

        return self.coefficients == other.coefficients

    def __add__(self, other): # called by '+' or '.__add__()'

        if isinstance(other, Polynomial):

            common = min(self.degree(), other.degree()) + 1  # num of common terms of 2 polys

            coefs = tuple(a + b for a, b in zip(self.coefficients, other.coefficients))
                                                            # zip: more iterators 
                                                            # zip stops when any one of the tuple runs out
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        # if the 'other' is a more general 'number'
        elif isinstance(other, Number):

            return  Polynomial((self.coefficients[0] + other,) # (x,) so that it's a one-length tuple 
                               + self.coefficients[1:])

        else:

            return NotImplemented # A special value returned in the case where the addition makes no sense

    def __radd__(self, other): # reverse the order of addition cause it's commutative

        return self.__add__(other)

        
