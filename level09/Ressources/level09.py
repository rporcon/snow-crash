#!/usr/bin/python           
                            
import sys                  
                            
char = list(sys.argv[1])    
for i, c in enumerate(char):
    sys.stdout.write(chr(ord(c) - i))
sys.stdout.write('\n')
sys.stdout.flush()
