import pytest

from src.SalaEspera import cSalaEspera

def testSalaEspera1():
	cargo1 = Cargo(100,0.5,2000,1000)
	# 2000 - 1000*1.5 - 100*2 es igual a 300
	assert(cargo1.is_worth_it() == 300) == True

