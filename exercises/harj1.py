

#Kuinka pitk¨a matka on maanpinnan suuntaisesti 
# rampin alap¨a¨an kohdalta yl¨ap¨a¨an kohdalle? 
# Toisin sanoen,
#kuinka pitk¨a on muodostuvan suorakulmaisen
# kolmien
#kolmas (vaakasuora) sivu.

#A)

import math

# Annetut arvot
h = 5        # Rampin korkeus
ramppi = 12  # Rampin pituus

# Pythagoraan lause: h^2 + x^2 = ramppi^2
# Ratkaistaan vaakasuora etäisyys x
x = math.sqrt(ramppi**2 - h**2)

print("Vaakasuora etäisyys rampin alapään ja yläpään välillä on:", x)

#B)  Kuinka suuri on rampin ja maanpinann v¨alinen kulma (kutsutaan sit¨a nimell¨a α) ?

alpha_radians = math.asin(h/ramppi)

alpha_degrees = math.degrees(alpha_radians)

print("Rampin ja maan valinen kulma a on", alpha_degrees, "astetta")


#C) Kuinka suuri on rampin ja pystysuoran suunnan v¨alinen kulma (kutsutaan sit¨a nimell¨a β)? Esit¨a kaksi tapaa
#laskea β, kun tunnet kolmion sivujen pituudet ja kulman α

# cosb = h/ ramppi

beta_degrees_from_alpha = 90 -alpha_degrees

beta_radians = math.asin(h/ramppi)
beta_degrees_from_sin = math.degrees(beta_radians)

print(beta_degrees_from_alpha)
print(beta_degrees_from_sin)

