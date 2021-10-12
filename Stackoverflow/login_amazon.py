from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self, login, senha, pesquisa):
        self.login = login
        self.senha = senha
        self.pesquisa = pesquisa
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--profile-directory=1')  # no casso do meu navegador tive que entrar como visitante
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessar(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def faca_seu_login(self):
        try:
            btn_faca_seu_login = self.chrome.find_element_by_id('nav-link-accountList')
            btn_faca_seu_login.click()
        except Exception as e:
            print(f'Erro ao clicar no login: ', e)

    def preencher_login(self):
        try:
            input_login = self.chrome.find_element_by_id('ap_email')
            input_login.send_keys(self.login)  # Aqui vai o e-mail cadastrado
            sleep(2)

            btn_continue = self.chrome.find_element_by_id('continue')
            btn_continue.click()
        except Exception as e:
            print(f'Erro ao preencher o login: ', e)

    def preencher_senha(self):
        try:
            input_senha = self.chrome.find_element_by_id('ap_password')
            input_senha.send_keys(self.senha)  # Aqui vem a senha do usuário

            sleep(2)
            btn_fazer_login = self.chrome.find_element_by_id('signInSubmit')
            btn_fazer_login.click()
        except Exception as e:
            print(f'Erro ao preencher sua senha: ', e)

    def pesquisar_produto(self):
        try:
            input_pesquisa = self.chrome.find_element_by_id('twotabsearchtextbox')
            input_pesquisa.send_keys(self.pesquisa)

            sleep(1)
            btn_pesquisar = self.chrome.find_element_by_id('nav-search-submit-button')
            btn_pesquisar.click()
        except Exception as e:
            print(f'Erro ao pesquisar o produto: ', e)

    def prime(self):
        try:
            btn_prime = self.chrome.find_element_by_id('p_85/19171728011')
            btn_prime.click()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    login = input('Informe seu login: ')
    senha = input('Informe sua senha: ')
    pesquisa = input('O que deseja pesquisar: ')

    chrome = ChromeAuto(login, senha, pesquisa)
    chrome.acessar('https://www.amazon.com.br/')

    chrome.faca_seu_login()
    chrome.preencher_login()
    chrome.preencher_senha()

    chrome.pesquisar_produto()
    chrome.prime()

    sleep(10)
    chrome.sair()
