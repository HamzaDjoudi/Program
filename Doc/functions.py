# -*- coding: utf-8 -*-
"""
Created on Wed Oct 08 09:35:03 2014

@author: hdjoudi
"""


def myfunction(x):
  """
  A powerful function that computes :math: `y = x^2`
  :param x: the x value
  :type x: float
  :rtype: float
  
  >>> x = 5
  >>> y = myfunction(x)
  >>> y
  25
  >>> print "AMAZING !!
    File "<stdin>", line 1
    
  .. note::
  
   This function will get me the Fields medal ! (at least)
   .. image:: images/rabbit.jpg
  """  
  return x**2
    
x = 5
y = myfunction(x)