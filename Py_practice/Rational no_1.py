
def gcd(bigger, smaller):
    '''compute the greatest common divisor of two positive integers'''
    #print(' in gcd ')
    if not bigger > smaller :
        bigger, smaller = smaller, bigger
    while smaller != 0:
        remainder = bigger % smaller
        #print('gcd calc, big:{}, small:{}, rem:{}'.format(bigger, smaller, remainder))
        bigger, smaller = smaller, remainder
    return bigger

def lcm(a, b):
    '''calculate the least common multiple of two positive integers'''
    #print(' in lcm ')
    return (a*b)//gcd(a,b)
    
def division(a, b):
    '''calculate the least common multiple of two positive integers'''
    #print(' in lcm ')
    return (a*b)//gcd(a,b)
    
def multiplication(a, b):
    '''calculate the least common multiple of two positive integers'''
    #print(' in multiplication ')
    return (a//b);    


class Rational(object):
    '''Rational with numerator and denominator. Denominator defaults to 1'''

    def __init__(self, numer, denom = 1):
        #print('in constructor')
        self.numer = numer
        self.denom = denom

    def __str__(self):
        '''String representation for printing'''
        #print(' in str ')
        return str(self.numer)  + '/'  +  str(self.denom)

    def __repr__(self):
        ''' Used in the interpreter. Call __str__ for now'''
        print(' in repr ')
        return self.__str__()

    def __add__(self, param_Rational):
        '''Add two Rationals'''
        if type(param_Rational) == int:
            param_Rational = Rational(param_Rational)
        if type(param_Rational) == Rational:
            # find the lcm
            the_lcm = lcm(self.denom, param_Rational.denom)
            # multiply each numerator by the lcm, then add
            numerator_sum = the_lcm*self.numer/self.denom + \
                        the_lcm*param_Rational.numer/param_Rational.denom
            return Rational( int(numerator_sum), the_lcm )
        else:
            print("Wrong type in addition method.")
            raise(TypeError)
        
    def __sub__(self, param_Rational):
        '''Subtract two Rationals'''
        #print(' in add ')
        # find the lcm
        the_lcm = lcm(self.denom, param_Rational.denom)
        # multiply each numerator by the lcm, then add
        numerator_sum = the_lcm*self.numer/self.denom - \
                    the_lcm*param_Rational.numer/param_Rational.denom
        return Rational( int(numerator_sum), the_lcm )
                    
    def __mul__(self, param_Rational):
        '''multiply two Rationals'''
        if type(param_Rational) == int:
            param_Rational = Rational(param_Rational)
        if type(param_Rational) == Rational:
            # multiply  numerator
            numerator_mul = self.numer * param_Rational.numer
            # multiply denominator
            denominator_mul = self.denom * param_Rational.denom
            return Rational( int( numerator_mul), int(denominator_mul))
        else:
            print("Wrong type in multiplication method.")
            raise(TypeError)
            
    def __div__(self, param_Rational):
        '''divide two Rationals'''
        if type(param_Rational) == int:
            param_Rational = Rational(param_Rational)
        if type(param_Rational) == Rational:
            # multiply  numerator
            numerator_mul = self.numer * param_Rational.denom
            # multiply denominator
            denominator_mul = self.denom * param_Rational.numer
            return Rational( int( numerator_mul), int(denominator_mul))
        else:
            print("Wrong type in multiplication method.")
            raise(TypeError)
            
    def reduce_rational(self):
        '''Return the reduced fraction value as a Rational'''
        # find the gcd and divide numerator and denominator by it
        the_gcd = gcd(self.numer, self.denom)
        return Rational( self.numer//the_gcd, self.denom//the_gcd)

    def __eq__(self, param_Rational):
        '''Compare two Rationals for equalit and return a Boolean'''
        reduced_self  = self.reduce_rational()
        reduced_param = param_Rational.reduce_rational()
        return reduced_self.numer == reduced_param.numer and\
               reduced_self.denom == reduced_param.denom
        

# ------------------------------ MAIN ------------------------------
def main():
    r1=Rational(10,5)
    r2=Rational(5,10)
    print("First Rational Number: ",r1.__str__())
    print("Second Rational Number: ",r2.__str__())
    print("Addition",r1.__add__(r2))
    print("Subtraction",r1.__sub__(r2))
    print("Multiplication",r1.__mul__(r2))
    print("Division",r1.__div__(r2))
if __name__ == "__main__":
    main()
