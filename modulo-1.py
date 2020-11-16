#import modulo

#print(xs.mascotas)
#xs.saludo('jeison')

import modulo as xs 
from camelcase import CamelCase

c = CamelCase()
s = 'esta oracion nesecita camelcase!'
camelcase = c.hump(s)
print(camelcase)