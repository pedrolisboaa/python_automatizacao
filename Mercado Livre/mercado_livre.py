from selenium import webdriver
from time import sleep


class Auto:
    def __init__(self, item_busca):
        self.item_busca = item_busca
        self.driver_path = '../stackoverflow/chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--profile-directory=1')  # no casso do meu navegador tive que entrar como visitante
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    # Funções principais de minha classe que automatiza o mercado livre

    def acessar_site(self):
        self.chrome.get('https://www.mercadolivre.com.br/')

    def sair_site(self):
        self.chrome.quit()

    def retorna_url(self):
        return self.chrome.current_url

    def realizar_busca(self):
        try:
            # Selecionando o input de busca e escrevendo qual será minha busca
            input_pesquisa = self.chrome.find_element_by_class_name('nav-search-input')
            input_pesquisa.send_keys(self.item_busca)
            sleep(2)

            # Clicando para realizar pesquisa
            btn_buscar = self.chrome.find_element_by_class_name('nav-search-btn')
            btn_buscar.click()
        except Exception as e:
            print(f'Erro ao tentar realizar a busca: ', e)
