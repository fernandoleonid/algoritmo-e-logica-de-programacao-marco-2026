# 🎓 Algoritmos e Lógica de Programação

**Instituição:** UniFECAF  
**Professor:** Fernando Leonid  
**Período:** Março de 2026  
**Linguagem:** Python 🐍

---

## 📚 Sobre a Disciplina

Disciplina de **Algoritmos e Lógica de Programação** com foco no desenvolvimento do raciocínio lógico e na construção de soluções computacionais utilizando Python. O conteúdo é trabalhado de forma progressiva, partindo de conceitos básicos até integração com banco de dados e APIs externas.

---

## 📅 Cronograma das Lives

| # | Data | Pasta | Conteúdo |
|---|------|-------|----------|
| 01 | 03/03/2026 | `live01/` | Apresentação da disciplina e introdução à lógica de programação |
| 02 | 05/03/2026 | `live02/` | Entrada de dados, operações aritméticas e estruturas condicionais |
| 03 | 10/03/2026 | `live03/` | Aprofundamento em estruturas condicionais (`if`, `elif`, `else`) |
| 04 | 12/03/2026 | `live04/` | Estruturas de repetição (`while`, `for`), listas e manipulação de dados |
| 05 | 17/03/2026 | `live05/` | Funções, dicionários e módulos personalizados |
| 06 | 19/03/2026 | `live06/` | Modularização, bibliotecas externas e sistema de tarefas |
| 07 | 24/03/2026 | `live07/` | Estruturas de dados avançadas com dicionários e gerenciamento de tarefas |
| 08 | 26/03/2026 | `live08/` | Banco de dados com SQLite — persistência e operações CRUD |
| 09 | 31/03/2026 | `live09/` | Consumo de APIs externas com `requests` (ViaCEP, TMDB, Open-Meteo) + uso de IAs generativas na programação |

---

## 🗂️ Estrutura do Repositório

```
📦 algoritmo-e-logica-de-programacao-marco-2026
├── 📁 live01/        → Introdução à lógica de programação
├── 📁 live02/        → Entrada de dados e condicionais
│   ├── 01-soma.py
│   └── 02-media.py
├── 📁 live03/        → Estruturas condicionais
├── 📁 live04/        → Repetição e listas
│   ├── 01-estrutura-repeticao.py
│   ├── 02-tabuada.py
│   ├── 03-login.py
│   ├── 04-menu.py
│   ├── 05-estrutura-dados-lista.py
│   ├── 06-repeticao-for.py
│   ├── 07-desconto.py
│   └── 08-controle-notas.py
├── 📁 live05/        → Funções e dicionários
│   ├── 01-dicionario.py
│   ├── 02-lista_dicionario.py
│   ├── 03-funções.py
│   ├── 04-soma.py
│   ├── 05-alunos.py
│   ├── 06-calculadora.py
│   └── escola.py
├── 📁 live06/        → Módulos e bibliotecas
│   ├── 01-modulo.py
│   ├── 02-calculadora.py
│   ├── 03-lista-tarefas.py
│   ├── matematica.py
│   └── uteis.py
├── 📁 live07/        → Estruturas de dados avançadas
│   └── 01 - lista_de_tarefas.py
├── 📁 live08/        → Banco de dados SQLite
│   ├── 01 - lista_de_tarefas_sqlite.py
│   └── 02 - cadastro cliente.py
├── 📁 live09/        → Consumo de APIs externas
│   ├── clima_cidade.py
│   ├── escola.py
│   ├── filmes.py
│   ├── genres.py
│   └── viacep.py
├── 📁 revisão/       → Exercícios de revisão
│   ├── 01.py
│   └── 02.py
├── 03.py             → Exercício de condicionais
└── README.md
```

---

## 🧠 Conteúdos Abordados

- **Variáveis e tipos de dados** — `int`, `float`, `str`, `bool`
- **Entrada e saída de dados** — `input()`, `print()`
- **Operadores** — aritméticos, relacionais e lógicos
- **Estruturas condicionais** — `if`, `elif`, `else`
- **Estruturas de repetição** — `while`, `for`
- **Listas** — criação, manipulação, `append()`, `pop()`, `enumerate()`
- **Dicionários** — chave-valor, listas de dicionários
- **Funções** — definição, parâmetros, retorno, importação
- **Módulos** — criação e uso de módulos personalizados
- **Bibliotecas externas** — `colorama`, `requests`
- **Banco de dados** — SQLite com `sqlite3` (CREATE, INSERT, SELECT, UPDATE, DELETE)
- **Consumo de APIs** — requisições HTTP com `requests`, tratamento de respostas JSON
- **Uso de IAs generativas** — demonstração do GitHub Copilot como ferramenta de apoio ao desenvolvimento

---

## 🤖 Sobre o Uso de IA Generativa

No arquivo `live09/filmes.py`, a função `consultar_filme` foi desenvolvida **passo a passo em live coding**, enquanto as demais funções foram geradas com o auxílio do **GitHub Copilot**. O objetivo foi demonstrar aos alunos como utilizar IAs generativas na criação de código, ao mesmo tempo conscientizando sobre o uso responsável dessas ferramentas durante o processo de aprendizado.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3** instalado
2. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/algoritmo-e-logica-de-programacao-marco-2026.git
   ```
3. Instale as dependências necessárias (para as lives 06 e 09):
   ```bash
   pip install colorama requests
   ```
4. Execute qualquer arquivo:
   ```bash
   python live02/01-soma.py
   ```

---

## � Material de Apoio

- **Git e GitHub** — [Playlist no YouTube](https://www.youtube.com/playlist?list=PLDgemkIT111A4GXwC2loYiLAvfIlMQRlZ)
- **VS Code e Python** — [Vídeo no YouTube](https://youtu.be/ALxlQWuPZN4)

---

## �📝 Licença

Este repositório é de uso educacional para os alunos da disciplina de Algoritmos e Lógica de Programação — UniFECAF.