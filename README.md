# **Sistema Para Baixar Arquivos CTA**

## **Descrição**

Este código baixa os arquivos Fiscal/Dirigida/Combinada e cola os mesmo numa pasta específica.
Ele usa imagens para se localizar em vez de pontos fixos na tela.

Isso evita possíveis erros e atrasos, pois a demora aqui é somente a dos próprios arquivos.
O código é executado na maioria das vezes no final do expediente.

---

## **Funcionalidades**

- *procurar_imagem()*
- *mover_para_a_imagem()*
- *mover_para_a_imagem_e_clicar()*
- *baixar_arquivo_fiscal*
- *baixar_arquivo_dirigida()*
- *baixar_arquio_combinada_multipla_negra()*
- *copiar_e_colar_arquivo_dirigida_e_combinada()*
- *copiar_e_colar_arquivo_fiscal()*

---

## **Tecnologias Utilizadas**

- **Python 3.11.4+**
- **PyAutoGUI 0.9.54**
- **PyScreeze 0.1.30**
- **Opencv-Python 4.9.0.80**

---

## **Estrutura do Projeto**

```
.
├── app
│   ├── arquivos.txt
│   ├── baixar_arquivo_cta.py
│   └── main.py
│
├── arquivo_dirigida.png
├── arquivo_fiscal.png
├── arquivo_pasta_analytics_cta.png
├── arquivo_pasta_dados.png
├── arquivo_pasta_IND.png
├── aviso_do_sistema.png
├── barra_endereco_explorador_arquivos.png
├── barra_pesquisa_cta.png
├── book_combinada_wps_office.png
├── book1_wps_office.png
├── botao_confirmar.png
├── botao_ok.png
├── botao_replace_wps_office.png
├── botao_save_wps_office.png
├── icon_reporttxl.png
├── icone_apps.png
├── icone_arquivos_cta_1.png
├── icone_arquivos_cta_2.png
├── icone_auto_sky.png
├── icone_cta.png
├── icone_gerencial.png
├── icone_wps_office.png
├── icones_auto_sky.png
├── texto_cobertura_multipla_negra.png
├── texto_cobertura_sku.png
├── texto_colecoes.png
├── texto_exportacao_dados_competencia.png
├── texto_iniciativa_dirigida.png
├── texto_open_file_location.png
├── texto_relatorio_performance.png
├── texto_save_as_wps_office.png
├── texto_server_o.png
├── texto_substituir_o_arquivo_destino.png
├── texto_substituir_os_arquivos_destino.png
|
├── README.md
```

---
## **Como Executar**

1. Acesse o arquivo `main.py`.
2. Execute o programa:
   ```bash
   python main.py
   ```

___


## **Autoria**
- Lucas Pereira Silva Mello

<br>

Fique à vontade para contribuir!