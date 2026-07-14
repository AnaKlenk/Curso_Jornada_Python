# Curso de Automação com Python (RPA)

Repositório com os projetos práticos de cada aula do curso, usando `pyautogui`
para automatizar tarefas repetitivas em sistemas web.

## Aulas

- [Aula 1 — Cadastro de Produtos](#aula-1--cadastro-de-produtos)
- [Aula 2 — Análise de Cancelamentos](#aula-2--análise-de-cancelamentos)

---

## Aula 1 — Cadastro de Produtos

Automação que faz login em um sistema web e cadastra uma lista de produtos
a partir de um arquivo CSV, usando `pyautogui`.

### Arquivos

| Arquivo | Descrição |
|---|---|
| `gabarito.py` | Script principal. Abre o Chrome, acessa o sistema, faz login e cadastra todos os produtos do `produtos.csv`, um por um. |
| `pegar_posicao.py` | Script auxiliar. Espera 5 segundos e imprime a posição atual do mouse `(x, y)` — usado para descobrir as coordenadas de clique de cada campo na tela. |
| `produtos.csv` | Base de dados com ~290 produtos a cadastrar. Colunas: `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo`, `obs`. |

### Pré-requisitos

```bash
pip install pyautogui pandas
```

- Google Chrome instalado
- Acesso ao sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

### Como o `gabarito.py` funciona

1. **Abre o navegador**: aperta `Win`, digita "chrome", dá enter, e clica numa
   posição fixa da tela (`x=399, y=364`) — usada para selecionar o Chrome
   na busca do Windows.
2. **Acessa o link de login** e espera a página carregar.
3. **Faz login**: clica no campo de email (`x=545, y=369`), digita o email
   e a senha, e aperta Enter.
4. **Lê o `produtos.csv`** com pandas.
5. **Para cada linha da planilha**: clica no campo de código (`x=600, y=257`),
   preenche código → marca → tipo → categoria → preço → custo → obs
   (pulando de campo em campo com `Tab`), aperta Enter pra cadastrar, e dá
   scroll pra cima antes do próximo produto.

### Rodando

```bash
python gabarito.py
```

Evite mexer no mouse/teclado enquanto o script roda — como ele usa
coordenadas fixas de tela, qualquer interferência pode fazer ele clicar no
lugar errado.

---

## Aula 2 — Análise de Cancelamentos

Notebook Jupyter que analisa uma base de clientes e gera histogramas
interativos para investigar quais fatores mais se relacionam com o
cancelamento do serviço, usando `pandas` e `plotly`.

### Arquivos

| Arquivo | Descrição |
|---|---|
| `inicial.ipynb` | Notebook principal. Lê a base de clientes, remove a coluna de identificação, e gera um histograma para cada coluna, colorido por status de cancelamento. |
| `cancelamentos.csv` | Base de dados dos clientes (colunas incluem `CustomerID`, `cancelou`, entre outras informações do cliente). |

### Pré-requisitos

```bash
pip install pandas plotly nbformat ipykernel
```

### Como o `inicial.ipynb` funciona

1. **Importa o pandas** e lê a base com `pd.read_csv("cancelamentos.csv")`.
2. **Remove a coluna `CustomerID`** (só um identificador, não ajuda na análise).
3. **Importa o plotly.express** e, para cada coluna restante da tabela, gera
   um histograma (`px.histogram`) separando as barras por cor de acordo com
   a coluna `cancelou` — assim dá pra comparar visualmente clientes que
   cancelaram vs. que não cancelaram, em cada característica da base.
4. Cada gráfico é exibido com `.show()`.

### Rodando

1. Abra o `inicial.ipynb` no VS Code.
2. Confirme o **kernel** selecionado no canto superior direito (deve ser o
   mesmo Python onde `pandas`, `plotly`, `nbformat` e `ipykernel` estão
   instalados).
3. Use **"Run All"** (▶▶) para rodar todas as células em ordem — rodar só a
   célula do gráfico isoladamente gera erro (`NameError: tabela is not
   defined`), porque a variável `tabela` é criada nas células anteriores.
