class Polynomial:


    def  __init__(self, coefs):

        self.coefficients = coefs

    def degree(self):

        return len(self.coefficients) - 1
    
    def __str__(self): # __str__ to represent the variable
        
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
