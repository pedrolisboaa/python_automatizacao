from mercado_livre import Auto
from time import sleep
from pegando_informacoes import pegar_todos_valores_da_pagina


# Inicializando aplicação
busca = input('Informe o item que deseja buscar no mercado livre ')
ml = Auto(busca)
ml.acessar_site()

# Buscando no site
ml.realizar_busca()
pegar_todos_valores_da_pagina(ml.retorna_url())

# Fechando site
sleep(10)
ml.sair_site()



