from selenium import webdriver
from random import randint
from time import sleep


def randomico():
    return randint(1, 3)


class ChromeAuto:
    def __init__(self, login, senha, usuario_curtida, quantidade_fotos):
        self.login = login
        self.senha = senha
        self.usuario_curtida = usuario_curtida
        self.quantidade_fotos = quantidade_fotos
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessar(self):
        self.chrome.get('https://www.instagram.com/accounts/login/')

    def sair(self):
        self.chrome.quit()

    def fazer_login(self):
        try:
            sleep(2)
            input_login = self.chrome.find_element_by_name('username')
            input_login.send_keys(self.login)

            sleep(2)
            input_senha = self.chrome.find_element_by_name('password')
            input_senha.send_keys(self.senha)

            sleep(2)
            btn_entrar = self.chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

        except Exception as e:
            print(f'Erro ao fazer login ', e)

    def agora_nao(self):
        try:
            sleep(2)
            btn_agora_nao = self.chrome.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/div/div/button').click()

            sleep(2)
            btn_nao = self.chrome.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        except Exception as e:
            print(f'Erro ao fazer clicar em agora não ', e)

    def realizar_pesquisa(self):
        try:
            sleep(2)
            input_pesquisa = self.chrome.find_element_by_xpath(
                '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
            input_pesquisa.send_keys(self.usuario_curtida)

            sleep(3.5)
            btn_perfil = self.chrome.find_element_by_class_name('-qQT3').click()
        except Exception as e:
            print(f'Erro ao pesquisar ou aperta: ', e)

    def curtir_fotos(self):
        try:
            sleep(4)
            btn_foto = self.chrome.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a').click()

            for vezes in range(int(self.quantidade_fotos)):
                sleep(randomico())
                btn_curtir = self.chrome.find_element_by_xpath(
                    '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()

                sleep(randomico())
                btn_mudar_foto = self.chrome.find_element_by_class_name('coreSpriteRightPaginationArrow').click()

        except Exception as e:
            print(f'Erro ao clicar na foto ', e)


if __name__ == '__main__':
    login = input('Informe seu login: ')
    senha = input('Informe sua senha: ')
    usuario = input('Informe o usuário que vai receber as curtidas: ')
    qtd_fotos = int(input('Quantas fotos deseja curtir: '))

    i = ChromeAuto(login, senha, usuario, qtd_fotos)
    i.acessar()
    i.fazer_login()

    sleep(2)
    i.agora_nao()
    i.realizar_pesquisa()

    i.curtir_fotos()

    sleep(50)
    i.sair()
