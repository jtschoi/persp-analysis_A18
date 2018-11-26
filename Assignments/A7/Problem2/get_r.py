import numpy as np

def get_r(K, L, alpha, Z, delta):
    '''
    This function generates the interest rate 
    or a vector of interest rates
    '''

    ## For scalars!
    if np.isscalar(K) and np.isscalar(L):
        r = alpha * Z * ((L / K) ** (1-alpha)) - delta
        return r

    ## For vectors (in numpy arrays)
    elif not np.isscalar(K) and not np.isscalar(L):
        if K.shape == L.shape:
            r = alpha * Z * ((L / K) ** (1-alpha)) - delta
            return r
