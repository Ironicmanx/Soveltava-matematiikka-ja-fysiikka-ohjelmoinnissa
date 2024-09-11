# Tehtävä 9

#OIKEIN TEHTY ja tarkistettu wolfamalpha.com:illa


#ilmaise funktio 6*sin(4*t+pi/3)sinin ja kosinin summana, siis muodossa Csin(wt) + Dcos(wt)

#muistetaan että sin(a+b) = sin(a) * cos(b) + cos(a) * sin(b)

#itse laskut tehty alla
#f(t) = 6*sin(4*t+pi/3)
# = 6*sin(4*t)*cos(pi/3) + 6*cos(4*t)*sin(pi/3)
# = 6*sin(4*t)*(1/2) + 6*cos(4*t)*(sqrt(3)/2)
# = 3*sin(4*t) + 3*sqrt(3)*cos(4*t)
# = 3*sin(4*t) + 5.196152422706632*cos(4*t)
# = 6/2 * sin(4*t) + 6*sqrt(3)/2*cos(4*t)
# = 3*sin(4*t) + 3*sqrt(3)*cos(4*t)

import numpy as np # tuodaan numpy ja matplotlib.pyplot
import matplotlib.pyplot as plt

t= np.linspace(0, 10, 100) # rajaukset 0-10, 100 väliä, gridiin

tulos = 3*np.sin(4*t) + 3*np.sqrt(3)*np.cos(4*t) #yksinkertaistettu funktio

print(tulos) # tulostetaan tulos

plt.plot(t, tulos) # x ja y akselit
plt.xlabel('aika (s)') # x akselin nimi
plt.ylabel('f(t)') # y akselin nimi
plt.title('siniaalto') # otsikko
plt.grid(True) # ruudukko
plt.show() # näytä kuvaaja

