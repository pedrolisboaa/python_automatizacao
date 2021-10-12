from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--profile-directory=1') # no casso do meu navegador tive que entrar como visitante
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_sign_in(self):
        try:
            # clicando no sing in
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as e:
            print(f'Erro ao clicar em Sign in:')

    def faz_login(self):
        try:
            # selecionando os campos
            input_login = self.chrome.find_element_by_id("login_field")
            input_password = self.chrome.find_element_by_id("password")
            btn_login = self.chrome.find_element_by_name('commit')

            # inserindo login e senha
            input_login.send_keys('testedopedrao@gmail.com')
            input_password.send_keys('churrasco123@')

            sleep(2)
            btn_login.click()
        except Exception as e:
            print(f'Error ao fazer o login {e}')

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary')
            perfil.click()
        except Exception as e:
            print(f'Error ao clicar no perfil {e}')

    def clica_explore(self):
        try:
            explore = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.Header-item--full.flex-column.flex-md-row.width-full.flex-order-2.flex-md-order-none.mr-0.mr-md-3.mt-3.mt-md-0.Details-content--hidden-not-important.d-md-flex > nav > a:nth-child(5)')
            explore.click()
        except Exception as e:
            print(f'Erro ao clicar no Explore {e}')




if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')

    chrome.clica_sign_in()
    chrome.faz_login()

    chrome.clica_perfil()
    sleep(2)
    chrome.clica_perfil()
    sleep(2)
    chrome.clica_explore()

    sleep(10)
    chrome.sair()





