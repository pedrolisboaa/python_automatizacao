from amazon import Amazon
from time import sleep

a = Amazon()
a.acessar()
a.realizar_login()
a.buscar_produto()
a.clicando_no_produto()
a.comprar()


sleep(50)
a.sair()