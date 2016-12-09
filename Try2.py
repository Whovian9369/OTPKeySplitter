#!/user/bin/env python2
import os, sys, zlib, binascii
import codecs
from Crypto.Cipher import AES


otpbinpath = os.path.abspath("OTP/otp.bin")

#Thank you Audiosurt for:

x = "Output/"
k = " - Wii U Bank"
folders = [x, x+"01 - Wii Bank", x+"02"+k, x+"03"+k, x+"04"+k, x+"05"+k, x+"06 - Wii SEEPROM Bank", x+"07 - Misc Bank"]
for f in folders:
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
        f.seek(0x90)
        starbuck_ancast_key = binascii.hexlify(f.read(16))
        f.seek(0xE0)
        wiiu_common_key = binascii.hexlify(f.read(16))
        print("\n\nOkay, so: Time to start actually doing the key extraction!")
else:
    if not os.path.exists("OTP"):
        os.makedirs("OTP")
    else:
        print("\nPut the otp.bin into the OTP folder please!\n")
        sys.exit(1)

wiiu_common_key = codecs.decode(wiiu_common_key, 'hex')
starbuck_ancast_key = codecs.decode(starbuck_ancast_key, 'hex')

if zlib.crc32(wiiu_common_key) & 0xffffffff != 0x7a2160de:
    print("wiiu_common_key is wrong")
    sys.exit(1)

if zlib.crc32(starbuck_ancast_key) & 0xffffffff != 0xe6e36a34:
    print("starbuck_ancast_key is wrong")
    sys.exit(1)
