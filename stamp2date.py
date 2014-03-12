#!/usr/bin/env python
from __future__ import print_function
from datetime import datetime as d
import sys

if __name__ == "__main__":
  print("./stamp2date timestamp1-timestamp2")
  print(" to ".join([ d.fromtimestamp(int(i)).strftime('%Y-%m-%d %H:%M:%S') for i in sys.argv[1].split("-")]))

