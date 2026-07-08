# Curso de Automação com Python (RPA)

Repositório com os projetos práticos de cada aula do curso, usando `pyautogui`
para automatizar tarefas repetitivas em sistemas web.

## Aulas

- [Aula 1 — Cadastro de Produtos com automação](#aula-1--cadastro-de-produtos)

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

### ⚠️ Antes de rodar você precisa ajustar

Esse script usa **coordenadas de tela fixas** (x, y) e **credenciais** que
são específicas do computador/conta de quem gravou a aula. Antes de rodar
na sua máquina:

1. **Troque o login e senha** pelo seu usuário cadastrado no sistema do curso.
2. **Recalcule todas as coordenadas de clique**, porque elas dependem da
   resolução da sua tela e de onde a janela do navegador abre. Use o
   `pegar_posicao.py` pra isso:
   ```bash
   python pegar_posicao.py
   ```
   Rode, posicione o mouse sobre o campo desejado durante os 5 segundos de
   espera, e anote o `(x, y)` impresso no terminal. Repita para: campo de
   busca do Chrome, campo de email, campo de código do formulário.
3. Rode com o Chrome **fechado** antes de começar, para o fluxo de abrir o
   navegador funcionar corretamente.

### Rodando

```bash
python gabarito.py
```

Evite mexer no mouse/teclado enquanto o script roda — como ele usa
coordenadas fixas de tela, qualquer interferência pode fazer ele clicar no
lugar errado.
