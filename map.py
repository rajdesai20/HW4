
try:
    
    from StringIO import StringIO
except ImportError:
    
    from io import StringIO
  
import csv
import sys

for a in sys.stdin:
    a = a.strip()
    b = StringIO(a)
    data = csv.reader(b, skipinitialspace=True, delimiter=',')    
    for w in data:
        
        w = w[-5:]
        for c in w:
            if(c not in (None,"")):
                print '%s\t%s' % (c.upper(), 1)
