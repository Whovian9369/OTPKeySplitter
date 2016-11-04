#!/user/bin/env python2
import os
import sys
##
##

print("Opening otp.bin ...")
otp = "".join(open("otp.bin", "rb").readlines())

print("Getting first part")
out = open("First Part.bin", "wb")
out.write(otp[0:5])

print("Getting second part")
out = open("Second Part.bin", "wb")
out.write(otp[5:15])

