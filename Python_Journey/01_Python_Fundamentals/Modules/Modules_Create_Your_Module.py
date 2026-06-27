# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

import sys
sys.path.append(r"D:\Games")
print(sys.path)

import Sohayb
print(dir(Sohayb))

Sohayb.sayHello("Ahmed")
Sohayb.sayHello("Osama")
Sohayb.sayHello("Mohamed")

Sohayb.sayHowAreYou("Ahmed")
Sohayb.sayHowAreYou("Osama")
Sohayb.sayHowAreYou("Mohamed")

# Alias

import Sohayb as ee

ee.sayHello("Ahmed")
ee.sayHello("Osama")
ee.sayHello("Mohamed")

ee.sayHowAreYou("Ahmed")
ee.sayHowAreYou("Osama")
ee.sayHowAreYou("Mohamed")

from Sohayb import sayHello

sayHello("Osama")

from Sohayb import sayHello as ss

ss("Osama")
