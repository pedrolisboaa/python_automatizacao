from selenium import webdriver
from time import sleep


class Amazon:
    def __init__(self):
        self.driver_path = '../Instagram/chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessar(self):
        self.chrome.get('https://www.amazon.com.br/')

    def sair(self):
        self.chrome.quit()

    def realizar_login(self):
        try:
            btn_login = self.chrome.find_element_by_id('nav-link-accountList-nav-line-1').click()
            input_email = self.chrome.find_element_by_name('email').send_keys('testedopedrao@gmail.com')
            btn_continuar = self.chrome.find_element_by_id('continue').click()
            input_senha = self.chrome.find_element_by_id('ap_password').send_keys('churrasco123@')
            btn_fazer_login = self.chrome.find_element_by_id('signInSubmit').click()
        except Exception as e:
            print(f'Erro ao realizar login: ', e)

    def buscar_produto(self):
        try:
            input_busca = self.chrome.find_element_by_id('twotabsearchtextbox')
            btn_busca = self.chrome.find_element_by_id('nav-search-submit-button')

            input_busca.send_keys('Smartphone Poco X3 PRO 256gb 8gb RAM – Phantom Black - Preto')
            btn_busca.click()

            # frete grátis pela amazon
            btn_frete_gratis = self.chrome.find_element_by_xpath('//*[@id="p_n_free_shipping_eligible/19171733011"]'
                                                                 '/span/a/div[1]/label/i')
            btn_frete_gratis.click()
        except Exception as e:
            print(f'Erro ao realizar busca de produto: ', e)

    def clicando_no_produto(self):
        try:
            sleep(2)
            btn_produto = self.chrome.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/'
                                                            'div[2]/div[1]/div/span/div/div/span/a/div/img')
            btn_produto.click()
        except Exception as e:
            print(f'Erro ao clicar no produto: ', e)

    def comprar(self):
        try:
            btn_comprar = self.chrome.find_element_by_name('submit.buy-now')
            btn_comprar.click()
        except Exception as e:
            print(f'Erro ao comprar o produto')



