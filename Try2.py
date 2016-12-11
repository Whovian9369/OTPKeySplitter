#!/user/bin/env python2
import os, sys, zlib, binascii
import codecs
from Crypto.Cipher import AES


otpbinpath = os.path.abspath("OTP/otp.bin")

if not os.path.exists(otpbinpath):
    response = raw_input("Please enter the relative path to the OTP file: ")
    print(response)
    if os.path.exists(response):
        print("Yep")
        otpbinpath = os.path.exists(response)
        print(otpbinpath)
        sys.exit(1)
    else:
        print("That... That file doesn't exist. Would you please try again?")
        sys.exit(1)

#Thank you Audiosurf for:

x = "Output/"
k = " - Wii U Bank"
outputfol = [x, x+"01 - Wii Bank", x+"02"+k, x+"03"+k, x+"04"+k, x+"05"+k, x+"06 - Wii SEEPROM Bank", x+"07 - Misc Bank"]
for f in outputfol:
	if not os.path.exists(f):
		os.makedirs(f)

#End Audiosurf's amazing and super useful contribution!

#prepare keys
#Thanks FIX94 for this code snippet from the iosuhax
#fw.img grabber in his IOSUHax Branch.
#For the source of this code, see:
# https://github.com/FIX94/iosuhax/blob/master/bin/getfwimg.py

if os.path.exists(otpbinpath):
    with open(otpbinpath,'rb') as f:
        print("Key extraction time!")
        #Wii First.
        f.seek(0x000)
        vwii_boot1_sha1 = binascii.hexlify(f.read(16))
        f.seek(0x014)
        vwii_commonkey = binascii.hexlify(f.read(16))
        #Wii U
        f.seek(0x90)
        starbuck_ancast_key = binascii.hexlify(f.read(16))
        f.seek(0xE0)
        wiiu_common_key = binascii.hexlify(f.read(16))
        f.seek(0xA0)
        wiiu_seeprom = binascii.hexlify(f.read(16))
        f.seek(0x150)
        wiiu_xor = binascii.hexlify(f.read(16))
        f.seek(0x160)
        wiiu_rng = binascii.hexlify(f.read(16))
else:
    if not os.path.exists("OTP"):
        os.makedirs("OTP")
    print("Put the otp.bin into the OTP folder please!")
    sys.exit(1)

##################################################################
#Some actual key extraction. No output to a file yet, though.
print("\nvWii_boot1_sha1:")
print(vwii_boot1_sha1)
print("\nvWii Common Key:")
print(vwii_commonkey)
print("\nStarbuck Ancast Key:")
print(starbuck_ancast_key)
print("\nWii U Common Key:")
print(wiiu_common_key)
print("\nWii U SEEPROM Key:")
print(wiiu_seeprom)
print("\nWii U XOR:")
print(wiiu_xor)
print("\nWii U RNG:")
print(wiiu_rng)
#
##################################################################

wiiu_common_key = codecs.decode(wiiu_common_key, 'hex')
starbuck_ancast_key = codecs.decode(starbuck_ancast_key, 'hex')

if zlib.crc32(wiiu_common_key) & 0xffffffff != 0x7a2160de:
    print("wiiu_common_key is wrong")
    sys.exit(1)

if zlib.crc32(starbuck_ancast_key) & 0xffffffff != 0xe6e36a34:
    print("starbuck_ancast_key is wrong")
    sys.exit(1)
