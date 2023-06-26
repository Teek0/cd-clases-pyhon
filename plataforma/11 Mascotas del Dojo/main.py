from clases.ninja import Ninja
from clases.gato import Gato

Yumi=Gato("Yuumi","Gato",0,100,100)
ninja1=Ninja("Vicente","Sepulveda",Yumi,0,0)

ninja1.alimentar(Yumi).caminar(Yumi).bañar(Yumi)
Yumi.cuantas_vidas_tiene_el_gato()