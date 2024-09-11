

#Tehtävä 8
#Ilmaise funktio 5sin(2t) + 2cos(2t) yhden siniaallon avulla, siis muodossa Asin(wt + vaihe).

#incomplete

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

#yleisesti sin(a+b) = sin(a) * cos(b) + cos(a) * sin(b)
#5sin(2t) + 2cos(2t) = sqrt(5^2 + 2^2) * sin(2t + vaihe)

#g(t) = A*sin(w*t + vaihe)
#g(t) = A*[sin(w*t)*cos(vaihe) + cos(w*t)*sin(vaihe)]
#     = A*[5sin(2t)*cos(vaihe) + 2cos(2t)*sin(vaihe)]
#     =  sqrt(5^2 + 2^2) * sin(2t + vaihe)
#     =  sqrt(29) * sin(2t + vaihe)
#     = 5.385164807134504 * sin(2t + vaihe)
#     = 5.385164807134504 * sin(2t + 1.1071487177940904)
#     = sin(2t + 1.1071487177940904) * 5.385164807134504
#     = 

t = np.linspace(0, 2, 1000)



#alkuperäinen funktio 
t_original = 5*np.sin(2*t) + 2*np.cos(2*t)
#laskettu funktio
t_modified = np.sin(2*t + 1.1071487177940904) * 5.385164807134504
#verrataan laskettua funktiota alkuperäiseen funktioon
plt.plot(t_original, t_modified)

#piirretään kuvaaja
plt.plot(t_original, t_modified)
plt.xlabel('aika (s)')
plt.ylabel('g(t)')
plt.title('siniaalto')
plt.grid(True)
plt.show()

#Tulos on sama kuin 5sin(2t) + 2cos(2t) eli funktio on oikein ilmaistu yhden siniaallon avulla.
