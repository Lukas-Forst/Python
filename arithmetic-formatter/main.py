# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main
import difflib

#print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'],True))
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
#print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
#print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
#print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49']))
#print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
#print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']))
"""
a = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
cases = [(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']),a)]
for a,b in cases:     
    print('{} => {}'.format(a,b))  
    for i,s in enumerate(difflib.ndiff(a, b)):
        if s[0]==' ': continue
        elif s[0]=='-':
            print(u'Delete "{}" from position {}'.format(s[-1],i))
        elif s[0]=='+':
            print(u'Add "{}" to position {}'.format(s[-1],i))    
    print()
"""
# Run unit tests automatically
main(module='test_module', exit=False)