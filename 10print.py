# 2013-09-20 
# Robin Camille Davis

# emulates 10 PRINT CHR$(205.5+RND(1)); : GOTO 10

from random import randrange
from string import replace

slashes = ["\\", "/"]
#slashes = ["\\", "/", "|", "_"] #for a little more fun

tenprint=[]

for i in range(2000):
    tenprint.append(slashes[randrange(0,2)]) # for x chars, (0,x)

pattern = str(tenprint)
pattern = replace(pattern, "\\\\", "\\") #taking out escape backslash
pattern = replace(pattern, "', '","") #taking out list junk
pattern = pattern[2:-2] #begins [' and ends ']

print pattern
