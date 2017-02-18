#!/usr/bin/env python2
import os, sys, zlib
import os.path
import codecs
from Crypto.Cipher import AES
import csv


optbin = os.path.abspath("OTP/otp.bin")

#Thank you Audiosurf for the initial folder creation help.
#Mine was way too messy originally!

categories = {
  0: '00wii_bank',
  1: '01wiiu_bank',
  2: '02wiiu_bank',
  3: '03wiiu_bank',
  4: '04wiiu_ng_bank',
  5: '05wiiu_cert_bank',
  6: '06wii_cert_bank',
  7: '07misc_bank'
}

descriptors = []
class OTPDescriptor(object):
  def __init__(self, name, offset, length, category):
    self.name = name
    self.offset = offset
    self.length = length
    self.category = category


with open('names.csv', 'r') as fin:
  reader = csv.reader(fin)
  for row in reader:
    name, offset, length, category = row
    offset = int(offset, 16)
    length = int(length)
    category = int(category)
    descriptors.append(OTPDescriptor(name, offset, length, category))

data = {}
with open(sys.argv[1], 'rb') as fin:
  for descriptor in descriptors:
    if descriptor.category < 0:
      continue
    print "Reading %s @ %d, length %d" % (descriptor.name, descriptor.offset, descriptor.length)
    fin.seek(descriptor.offset)
    x = fin.read(descriptor.length)
    data[descriptor.name] = x


for key,value in categories.iteritems():
  p = os.path.join('output', value)
  os.makedirs(p)

for descriptor in descriptors:
  if descriptor.category < 0:
    continue
  output_file = os.path.join('output',categories[descriptor.category], descriptor.name + '.bin')
  print "Writing %s" % (descriptor.name)
  with open(output_file, 'wb') as fout:
    fout.write(data[descriptor.name])

