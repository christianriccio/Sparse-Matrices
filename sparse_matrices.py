import numpy as np

def matrix(n):
  '''sparse matrices needs to be menaged by dictionaries. This function buil a dictionary that represent the sparse matrices of a given dimension'''
    d=dict()
    for el in range(n):
        if len(d) == n:
            break
        else:
            i = np.random.randint(0,10**4)
            j = np.random.randint(0,10**4)
            z = np.random.randint(1,31)
            if (i,j) not in d:
                d[(i,j)]=z
    return d

def prodotto(diz1, diz2):
  '''this function performs the matrix product of two sparse matrices'''
    dizionario = dict()
    for k1,k2 in zip(diz1.keys(), diz2.keys()):
        if k1==k2:
            dizionario[k1] = diz1[k1]*diz2[k2]
    return dizionario    


def main():
    m1 = matrix(100)
    m2=matrix(100)
    prod=prodotto(m1,m2)
    print(prod)

if __name__=='__main__':
    main()
