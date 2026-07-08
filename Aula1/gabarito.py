
import pyautogui as pa
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pa.PAUSE = 1.5

# Abrir o navegador (chrome)
pa.press("win")
pa.write("chrome")
pa.press("enter")
pa.click(x=399, y=364)
time.sleep(3)

# Entrar no link 
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")
time.sleep(3)

# Passo 2: Fazer login
pa.click(x=545, y=369)
pa.write("ana@gmail.com")
time.sleep(1)
pa.press("tab")
time.sleep(1)
pa.write("A@na1.2.3")
time.sleep(1)
pa.press("tab")
time.sleep(1)
pa.press("enter")

# Passo 3: Importar a base de produtos pra cadastrar
# Importar a biblioteca pandas as pd
import pandas as pd
tabela = pd.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pa.click(x=600, y=257)

    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]

    # preencher o campo
    pa.write(str(codigo))

    # passar para o proximo campo
    pa.press("tab")

    # preencher o campo
    pa.write(str(tabela.loc[linha, "marca"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "tipo"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "categoria"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "preco_unitario"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "custo"]))
    pa.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pa.write(str(tabela.loc[linha, "obs"]))
    pa.press("tab")

    pa.press("enter") # cadastra o produto (botao enviar)
    pa.scroll(5000)

    # dar scroll de tudo pra cima
    # Passo 5: Repetir o processo de cadastro até o fim
