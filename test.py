
from os import environ
exclude = 'XPC_FLAGS'
d2 = dict((k.upper(), v.lower()) for k, v in environ.items())
del d2[exclude]
for k ,v in d2.items():
    print(k, v)

    
    


     

