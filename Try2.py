#!/user/bin/env python2
import os, sys, zlib, binascii
import codecs
from Crypto.Cipher import AES
##
##

otpbinpath = os.path.abspath("OTP/otp.bin")
if os.path.exists(otpbinpath):
    with open(otpbinpath,'rb') as f:
        f.seek(0x90)
        starbuck_ancast_key = binascii.hexlify(f.read(16))
        f.seek(0xE0)
        wiiu_common_key = binascii.hexlify(f.read(16))
else:
        os.makedirs("OTP")
        print("Put the otp.bin into the OTP folder please!")
        print(" ")
if not os.path.exists("Output/"):
    os.makedirs("Output/")
    os.makedirs("Output/01 - Wii Bank")
    os.makedirs("Output/02 - Wii U Bank")
    os.makedirs("Output/03 - Wii U Bank")
    os.makedirs("Output/04 - Wii U Bank")
    os.makedirs("Output/05 - Wii U Bank")
    os.makedirs("Output/06 - Wii SEEPROM Bank")
    os.makedirs("Output/07 - Misc Bank")
if not os.path.exists("Output/01 - Wii Bank"):
    print("I assume that I did not make ANY of the output folders.")
    print("So I'm doing that now. Because screw you is why.")
    os.makedirs("Output/01 - Wii Bank")
    os.makedirs("Output/02 - Wii U Bank")
    os.makedirs("Output/03 - Wii U Bank")
    os.makedirs("Output/04 - Wii U Bank")
    os.makedirs("Output/05 - Wii U Bank")
    os.makedirs("Output/06 - Wii SEEPROM Bank")
    os.makedirs("Output/07 - Misc Bank")
else:
    print("The output folders are probably already made. Not doing a thing.")
print("")
print("")
print("Okay, so: Time to start actually doing the key extraction!")

#prepare keys
#Thanks FIX94 for this code snippet from the iosuhax
#fw.img grabber in his IOSUHax Branch.
#For the source of this code, see:
# https://github.com/FIX94/iosuhax/blob/master/bin/getfwimg.py
wiiu_common_key = codecs.decode(wiiu_common_key, 'hex')
starbuck_ancast_key = codecs.decode(starbuck_ancast_key, 'hex')

if zlib.crc32(wiiu_common_key) & 0xffffffff != 0x7a2160de:
    print("wiiu_common_key is wrong")
    sys.exit(1)

if zlib.crc32(starbuck_ancast_key) & 0xffffffff != 0xe6e36a34:
    print("starbuck_ancast_key is wrong")
    sys.exit(1)
