import hashlib;
import itertools;
import string;
import time;
from argparse import ArgumentParser;

def check_guess_md5(guess):
  hash = hashlib.md5(str(guess).encode('utf-8')).hexdigest();
  if (hash[0]=='0') and (hash[1]=='e'):
    try:
      print(int(hash[2:]));
    except:
      return False;
    return True;

def enumerate(minl,maxl):
  while(minl<maxl):
    for guess in itertools.product(string.ascii_letters + string.digits, repeat=i):
      if check_guess_md5(''.join(guess)):
        print("md5({0}) = {1}".format(''.join(guess),hashlib.md5(str(guess).encode('utf-8')).hexdigest()));
    minl=minl+1;

try:
  parser = ArgumentParser();
  parser.add_argument("-min", dest="minl", type=int, help="Minimum number of symbols in source phrase", default=0, metavar="1");
  parser.add_argument("-max", dest="maxl", type=int, help="Maximum number of symbols in source phrase (required)", metavar="5");
  args = parser.parse_args();
  enumerate(args.minl,args.maxl);
except:
  print("Something went wrong. Use -h for help.");