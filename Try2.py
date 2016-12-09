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
        print("The otp.bin has been found!")
        print(" ")
        print("Okay. I have the wiiu_common_key!")
        print(" ")
        print("Okay. I have the starbuck_ancast_key!")
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
    print("Folders are probably already made. Not doing anything.")

print("")
print("")
print("Uh what do you want me to do now?")