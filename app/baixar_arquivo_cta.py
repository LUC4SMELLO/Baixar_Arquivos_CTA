import time

import pyautogui
import pyscreeze
import cv2

caminho_para_colar_arquivos = "O:/VENDAS/2025/02 - 2025/Arquivos"

class BaixarArquivo:

    @staticmethod
    def procurar_imagem(
        imagem,
        tempo_de_procura=10,
        nivel_de_confianca=0.8,
    ):
        """Retorna uma tupla com 4 coordenadas da imagem (esquerda, topo, largura, altura)"""
        posicao = pyscreeze.locateOnScreen(
            image=imagem, minSearchTime=tempo_de_procura, confidence=nivel_de_confianca
        )
        if posicao:
            return posicao
        else:
            raise pyscreeze.ImageNotFoundException("Imagem não encontrada")


    @staticmethod
    def mover_para_a_imagem(nome_imagem):
        """Move para a imagem passada como parâmetro"""
        pyautogui.moveTo(pyautogui.center(BaixarArquivo.procurar_imagem(nome_imagem)))
        time.sleep(0.500)

    @staticmethod
    def mover_para_a_imagem_e_clicar(
        nome_imagem, numero_de_clicks=1, tempo_de_procura=10,
        nivel_confianca=0.8, botao="left", intervalo_click=0
    ):
        """Move para a imagem passada como parâmetro e clica nela"""
        pyautogui.moveTo(
            pyautogui.center(
                BaixarArquivo.procurar_imagem(
                    imagem=nome_imagem,
                    tempo_de_procura=tempo_de_procura,
                    nivel_de_confianca= nivel_confianca
                )
            )
        )
        time.sleep(0.450)
        pyautogui.click(clicks=numero_de_clicks, button=botao, interval=intervalo_click)
        time.sleep(0.700)

    def baixar_arquivo_fiscal(self):
        BaixarArquivo.mover_para_a_imagem_e_clicar("icone_cta.png")
        BaixarArquivo.mover_para_a_imagem_e_clicar("barra_pesquisa_cta.png")
        pyautogui.write("Compet") # Competência
        BaixarArquivo.mover_para_a_imagem_e_clicar("texto_exportacao_dados_competencia.png")
        BaixarArquivo.mover_para_a_imagem_e_clicar("botao_confirmar.png")
        BaixarArquivo.mover_para_a_imagem_e_clicar("botao_ok.png", tempo_de_procura=600)
        time.sleep(0.333)


    def baixar_arquivo_dirigida(self):
        BaixarArquivo.mover_para_a_imagem_e_clicar("icone_apps.png")
        BaixarArquivo.mover_para_a_imagem_e_clicar("icone_gerencial.png")

        posicao = BaixarArquivo.procurar_imagem("texto_colecoes.png")
        pyautogui.moveTo(posicao[0] + 5, posicao[1] + 5)
        pyautogui.click()

        posicao = BaixarArquivo.procurar_imagem("texto_cobertura_sku.png")
        pyautogui.moveTo(posicao[0] + 10, posicao[1] + 8)
        pyautogui.click()

        BaixarArquivo.mover_para_a_imagem_e_clicar("texto_iniciativa_dirigida.png")
        BaixarArquivo.mover_para_a_imagem_e_clicar("botao_confirmar.png")
        time.sleep(10)
        BaixarArquivo.mover_para_a_imagem_e_clicar("icon_reporttxl.png")
        BaixarArquivo.mover_para_a_imagem_e_clicar("book1_wps_office.png", tempo_de_procura=600, botao="right")
        BaixarArquivo.mover_para_a_imagem_e_clicar("texto_save_as_wps_office.png")
        time.sleep(0.400)
        pyautogui.write("dirigida")
        time.sleep(0.400)
        BaixarArquivo.mover_para_a_imagem_e_clicar("botao_save_wps_office.png")
        time.sleep(0.400)
        BaixarArquivo.mover_para_a_imagem_e_clicar("botao_replace_wps_office.png")
        pyautogui.hotkey("alt", "f4")
        time.sleep(0.400)
        pyautogui.hotkey("alt", "f4")
        time.sleep(0.333)


    def baixar_arquivo_combinada_multipla_negra(self):
        BaixarArquivo.mover_para_a_imagem_e_clicar("icone_apps.png")
        BaixarArquivo.mover_para_a_imagem_e_clicar("icone_gerencial.png")

        posicao = BaixarArquivo.procurar_imagem("texto_relatorio_performance.png")
        pyautogui.moveTo(posicao[0] + 5, posicao[1] + 5)
        pyautogui.click()

        BaixarArquivo.mover_para_a_imagem_e_clicar("texto_cobertura_multipla_negra.png")
        BaixarArquivo.mover_para_a_imagem_e_clicar("botao_confirmar.png")
        
        time.sleep(45)
        BaixarArquivo.mover_para_a_imagem_e_clicar("icon_reporttxl.png")
        BaixarArquivo.mover_para_a_imagem_e_clicar("book1_wps_office.png", tempo_de_procura=600, botao="right")
        BaixarArquivo.mover_para_a_imagem_e_clicar("texto_save_as_wps_office.png")
        time.sleep(0.400)
        pyautogui.write("combinada")
        time.sleep(0.400)
        pyautogui.hotkey("enter")
        BaixarArquivo.mover_para_a_imagem_e_clicar("botao_save_wps_office.png")
        time.sleep(0.400)
        BaixarArquivo.mover_para_a_imagem_e_clicar("botao_replace_wps_office.png")
        time.sleep(0.400)
        

    def copiar_e_colar_arquivo_dirigida_e_combinada(self):
        time.sleep(0.400)
        BaixarArquivo.mover_para_a_imagem_e_clicar("book_combinada_wps_office.png", botao="right")
        BaixarArquivo.mover_para_a_imagem_e_clicar("texto_open_file_location.png")
        time.sleep(5)
        pyautogui.hotkey("win", "up")
        time.sleep(1)

        pyautogui.keyDown("ctrl")
        BaixarArquivo.mover_para_a_imagem_e_clicar("arquivo_dirigida.png")
        pyautogui.keyUp("ctrl")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.400)
        BaixarArquivo.mover_para_a_imagem_e_clicar("texto_server_o.png")
        time.sleep(0.400)

        BaixarArquivo.mover_para_a_imagem_e_clicar("barra_endereco_explorador_arquivos.png")
        pyautogui.write(caminho_para_colar_arquivos)
        pyautogui.hotkey("enter")
        time.sleep(3.500)

        pyautogui.moveTo(x=718, y=508)
        pyautogui.click()   
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1.500)
        BaixarArquivo.mover_para_a_imagem_e_clicar("texto_substituir_os_arquivos_destino.png")


    def copiar_e_colar_arquivo_fiscal(self):
        time.sleep(0.400)
        BaixarArquivo.mover_para_a_imagem_e_clicar("icone_auto_sky.png")
        BaixarArquivo.mover_para_a_imagem_e_clicar("icones_auto_sky.png")
        BaixarArquivo.mover_para_a_imagem_e_clicar("icone_arquivos_cta_1.png", numero_de_clicks=2)

        time.sleep(5)
        pyautogui.hotkey("win", "up")
        time.sleep(1)
        BaixarArquivo.mover_para_a_imagem_e_clicar("arquivo_pasta_IND.png", numero_de_clicks=2)
        BaixarArquivo.mover_para_a_imagem_e_clicar("arquivo_pasta_analytics_cta.png", numero_de_clicks=2)
        BaixarArquivo.mover_para_a_imagem_e_clicar("arquivo_pasta_dados.png", numero_de_clicks=2)

        BaixarArquivo.mover_para_a_imagem_e_clicar("arquivo_fiscal.png")
        pyautogui.hotkey("ctrl", "c")

        time.sleep(0.400)
        BaixarArquivo.mover_para_a_imagem_e_clicar("texto_server_o.png")
        time.sleep(0.400)

        BaixarArquivo.mover_para_a_imagem_e_clicar("barra_endereco_explorador_arquivos.png")
        pyautogui.write(caminho_para_colar_arquivos)
        pyautogui.hotkey("enter")
        time.sleep(3.500)

        pyautogui.moveTo(x=718, y=508)
        pyautogui.click()   
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1.500)
        BaixarArquivo.mover_para_a_imagem_e_clicar("texto_substituir_o_arquivo_destino.png")
