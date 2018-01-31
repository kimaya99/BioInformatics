# Exercise 01
#Kimaya Desai
#820884799

def hello():
    """
    Prints "Hello World"
    :return: None
    """
    print("Hello World")
    return

def percent_decimal(i):
    """
    Converts a percentage to a decimal or a decimal to a percentage depending on the input i
    :param i: a float between 0 and 100
    :return: a float between 0 and 100
    """

    if (i<=100 and i>=1):
        answer = round(i / 100, 6)
    else :
        answer = round(i * 100, 6)
    return answer

def exponent(integer, power):
    """
    Using a loop (no imports!), raise the integer given to the power provided. (integer^power)
    e:param integer: a positive, non zero, integer
    :param power: a positive, non zero, integer
    :return: an integer
    """
    expo = 1
    while (power != 0) :
        expo = expo * integer
        power = power - 1
    return expo

def complement(dna):
    """
    Returns the complement strand of DNA to the input.  C <--> G,  A <--> T
    :param dna: String containing only C, T, A, and G
    :return: String containing only C, T, A, and G

    """
    dict = {'C': 'G', 'A': 'T', 'G': 'C','T':'A'}
    if dict.has_key(dna):
        complement = dict.get(dna)
    return complement


hello()

print(percent_decimal(23.14))
print(percent_decimal(10.56))
print(percent_decimal(0.231))
print(percent_decimal(0.099))

print(exponent(2,3))
print(exponent(9,2))

print(complement('C'))
print(complement('T'))
print(complement('A'))
print(complement('G'))






