from operator import itemgetter
import sys

now = None
count = 0
word = None


for a in sys.stdin:
    
    a = a.strip()

    
    word, count1 = a.split('\t', 1)

    
    try:
        count1 = int(count1)
    except ValueError:
        
        
        continue

    
    
    if now == word:
        count += count1
    else:
        if now:
           
            print '%s\t%s' % (now, count)
        count = count1
        now = word


if now == word:
    print '%s\t%s' % (now, count)
