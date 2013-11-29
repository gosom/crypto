#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: giorgos
# @Date:   2013-11-29 08:25:38
# @Last Modified by:   giorgos
# @Last Modified time: 2013-11-29 09:51:20
import random


def xgcd(a, b):
    """Extended Euclidean Algorithm
    returns: tuple (gcd, x, y) where gcd is the greatest common divisor of
    a and b. X, y are such that gcd = ax + by"""
    px, x = 1, 0
    py, y = 0, 1
    while b:
        q, r = divmod(a, b)
        x, px = px - q*x, x
        y, py = py - q*y, y
        a, b = b, r
    return a, px, py


def is_prime_fermat(n, x=None):
    """determines if n is prime using Fermat's theorem
    (Let N be prime and x in Zn with x !=0 then x*(n-1)==1 in Zn)
    Parameters:
    :param n: n >= 2
    :param x: if x is None then we perform the test with a random value
    :returns : True for for "probably prime" False for composite"""
    assert n >= 2
    if not x:
        x = random.randint(1, n-1)
    g = xgcd(x, n)
    if g[0] != 1:
        return False
    y = pow(x, n-1, n)
    if y != 1:
        return False
    return True


def is_prime_strong(n, x=None):
    """Strong psesudoprimality test
    Parameters:
    :param n: the number to check for primality n>=2
    :param x: the random integer between 1 and n-1. Default None
    :returns: True if n is probably prime and False if n is composite"""
    if not x:
        x = random.randint(1, n-1)
    g = xgcd(x, n)
    if g[0] != 1:
        return False
    # writing n-1 = 2^e * m
    m = n - 1
    e = 0
    while m % 2 == 0:
        m >>= 1
        e += 1
    # so n - 1 = 2^e + m
    y = pow(x, m, n)
    if y == 1:
        return True
    for i in xrange(0, e):
        if y == -1:
            return True
        y = pow(y, 2, n)
    return False


def get_liars(n, test_with=is_prime_fermat):
    """returns the x in Zn for which the test_with returns True although
    n is composite"""
    liars = []
    for x in xrange(1, n):
        if test_with(n, x):
            liars.append(x)
    return liars


if __name__ == '__main__':

    #Exercise 5.3
    print 41, 'prime: ', is_prime_strong(n=41, x=2) #iii Returns False
    print 41, 'prime: ', is_prime_strong(n=41, x=37) #iv Returns True
    print 1105, 'prime: ', is_prime_strong(n=1105, x=45) #iv Returns False
    print 1105, 'prime: ', is_prime_strong(n=1105, x=2) #iv Returns False

    #vii
    liars = get_liars(n=35, test_with=is_prime_fermat)
    print 'number of Fermat liars for n=35 : %d ' % len(liars) # 4 fermat liars
    print 'The liars are: %s' % ','.join(map(str, liars))

    #viii
    liars = get_liars(n=35, test_with=is_prime_strong)
    print 'number of Strong liars for n=35 : %d ' % len(liars) # 1 strong liar
    print 'The liars are: %s' % ','.join(map(str, liars))

    #ix
    liars = get_liars(n=561, test_with=is_prime_fermat)
    print 'number of Fermat liars for n=561 : %d ' % len(liars) # 320 fermat liars
    #print 'The liars are: %s' % ','.join(map(str, liars)) # too many to print

    liars = get_liars(n=561, test_with=is_prime_strong)
    print 'number of Strong liars for n=561 : %d ' % len(liars) # 5 strong liars
    print 'The liars are: %s' % ','.join(map(str, liars))

    #x
    liars = get_liars(n=15274, test_with=is_prime_fermat)
    print 'number of Fermat liars for n=15274 : %d ' % len(liars) # 3 fermat liars
    liars = get_liars(n=15274, test_with=is_prime_strong)
    print 'number of Strong liars for n=15274 : %d ' % len(liars) # 3 strong liars

    liars = get_liars(n=1729, test_with=is_prime_fermat)
    print 'number of Fermat liars for n=1729 : %d ' % len(liars) # 1296 fermat liars
    liars = get_liars(n=1729, test_with=is_prime_strong)
    print 'number of Strong liars for n=1729 : %d ' % len(liars) # 81 strong liars

    liars = get_liars(n=8911, test_with=is_prime_fermat)
    print 'number of Fermat liars for n=8911 : %d ' % len(liars) # 7128 fermat liars
    liars = get_liars(n=8911, test_with=is_prime_strong)
    print 'number of Strong liars for n=8911 : %d ' % len(liars) # 891 strong liars

    liars = get_liars(n=100, test_with=is_prime_fermat)
    print 'number of Fermat liars for n=100 : %d ' % len(liars) # 1 fermat liars
    liars = get_liars(n=100, test_with=is_prime_strong)
    print 'number of Strong liars for n=100 : %d ' % len(liars) # 1 strong liars


    liars = get_liars(n=102, test_with=is_prime_fermat)
    print 'number of Fermat liars for n=102 : %d ' % len(liars) # 1 fermat liars
    liars = get_liars(n=102, test_with=is_prime_strong)
    print 'number of Strong liars for n=102 : %d ' % len(liars) # 1 strong liars


    liars = get_liars(n=253, test_with=is_prime_fermat)
    print 'number of Fermat liars for n=253 : %d ' % len(liars) # 4 fermat liars
    liars = get_liars(n=253, test_with=is_prime_strong)
    print 'number of Strong liars for n=253 : %d ' % len(liars) # 1 strong liars





