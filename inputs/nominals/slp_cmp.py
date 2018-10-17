# -*- coding: utf-8 -*-
"""slp_cmp
   comparison function for sorting Sanskrit words coded as slp into
   Sanskrit alphabetical order.
"""


import string
# Note 'L' and '|' and 'Z' and 'V' are not present
# Not sure where they go 
tranfrom="aAiIuUfFxXeEoOMHkKgGNcCjJYwWqLQ|RtTdDnpPbBmyrlvSzsh"
tranto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy"
trantable = string.maketrans(tranfrom,tranto)
def slp_cmp(a,b):
 a = str(a)  # required since a,b are unicode, not acceptable to translate
 b = str(b)
 try:
  a1 = string.translate(a,trantable)
  b1 = string.translate(b,trantable)
 except Exception as e:
  print "slp_cmp error: a='%s',b='%s'" %(a,b)
  print "Error=",e
  exit(1)
 return cmp(a1,b1)
