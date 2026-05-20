# ⌨️ CLI Environment Checker
<p>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black"/>
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white"/>
  <img src="https://img.shields.io/badge/ShellCheck-FFD500?style=flat-square"/>
  <img src="https://img.shields.io/badge/Makefile-000000?style=flat-square&logo=gnu&logoColor=white"/>
  <img src="https://img.shields.io/badge/shfmt-316688?style=flat-square"/>
</p>

este projeto consiste em uma aplicação em Python, executada via terminal, com um script em Bash responsável por validar o ambiente antes da execução, testes unitários automatizados com pytest, e um Makefile para orquestração de tarefas.

o foco está em consolidar e demonstrar fundamentos práticos de Linux, scripts e automação, com orquestração de tarefas em ambiente de linha de comando, simulando um fluxo real de execução, aplicando boas práticas.

🚧 projeto em evolução contínua, com melhorias incrementais focadas em boas práticas, automação e robustez.

---

## 🎬 demo

execução completa (validação + calculadora):

[![demo da execução do script no terminal](https://asciinema.org/a/907010.svg)](https://asciinema.org/a/907010)

## 🎯 objetivo

este projeto tem como objetivo explorar, na prática, como ocorre a execução e automação de aplicações em ambiente Linux, utilizando scripts e ferramentas de linha de comando.

além da implementação, o propósito está em compreender:
- fluxo de execução de programas
- validação de ambientes
- automação e orquestração de tarefas
- uso de códigos de saída *(exit codes)*
- escrita e execução de testes unitários
- construção e funcionamento de uma pipeline

## 🚀 como executar 

```bash
make
```

ou:

```bash
make run
```

## ⚙️ comandos disponíveis

```bash
make help
```

- `make` ou `make run` — executa o projeto  
- `make setup` — concede permissão de execução aos scripts  
- `make lint` — analisa o script Bash com ShellCheck  
- `make test` — executa os testes unitários com pytest

## 🧠 funcionalidades

- interface da calculadora via terminal (Python)
- validação automática de dependências (python3)
- verificação de existência do arquivo principal
- validação e ajuste automático de permissões de execução
- execução no padrão Unix (`./script`)
- orquestração com Makefile
- lint do script Bash com ShellCheck
- testes unitários automatizados da aplicação com pytest
- saída colorida para melhor legibilidade

## 🏗️ estrutura do projeto

```
.
├── Makefile               # orquestração de tarefas
├── cli-env-checker.sh     # valida o ambiente e executa o programa
├── calculadora.py         # código principal da calculadora
├── operacoes.py           # código das operações usadas pela calculadora 
└── test_operacoes.py      # testes das funções das operações
```


## 🧱 o que este projeto demonstra

- uso de *shebang* para execução de scripts
- diferença entre execução via interpretador e executável (`bash script.sh` vs `./script.sh`)
- manipulação de permissões com `chmod`
- validação de dependências no ambiente
- boas práticas com `printf` em Bash
- Quality Assurance com testes unitários
- organização e automação com Makefile
- uso de ferramenta de lint (ShellCheck)

## 💡 aprendizados e insights

- **execução como executável vs interpretado**  
    >entendi na prática a diferença entre rodar um script com `./script.sh` e com `bash script.sh`.  
    >quando executo com `./`, ele depende da permissão e do *shebang*; já com `bash`, ele simplesmente interpreta o arquivo, ignorando essas regras.
    
- **como o Bash pensa (`exit code` vs `true/false`)**  
    >diferente do Python, o Bash não trabalha exatamente com booleanos da mesma forma.  
    >o que importa é o código de saída: `0` significa *sucesso*, qualquer outro valor indica *erro* — isso muda bastante a forma de pensar em condicionais.
    
- **importância dos exit codes**   
    >é o que permite automação funcionar na prática, porque outros processos conseguem saber se algo deu certo ou não sem precisar interpretar texto, sendo muito útil em logs e integração com outros sistemas.
    
- **Makefile orquestra o workflow**  
    >sempre achei meio chato ter que lembrar de dar `chmod` antes de rodar script. 
    >o Makefile organiza isso, padroniza a execução do projeto, e permite a execução completa com um único comando — é uma camada de automação simples, mas muito útil.

- **separação de responsabilidades** 
    >modularizar a aplicação seguindo o conceito de separação de responsabilidades é uma decisão de design que, além de deixar o código mais limpo, também facilita o reuso de funções e o teste de software.  

- **Quality Assurance com pytest**
    >apliquei QA através de testes unitários automatizados para validar as operações da aplicação, utilizando pytest.

- **por que tudo isso importa no mundo real**  
    >esse projeto me ajudou a ter um vislumbre melhor de como pipelines funcionam em ambientes reais, porque são tão úteis, e como essas práticas aparecem no dia a dia de quem trabalha com automação e infraestrutura.
    
## 🧭 próximos passos

- 🐳 containerizar a aplicação com Docker
- ⚙️ implementar automação com CI (GitHub Actions)
- 🔮 aprimorar o tratamento de erros no script

## 🛠️ tecnologias

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white) ![ShellCheck](https://img.shields.io/badge/ShellCheck-FFD500?style=for-the-badge) ![Makefile](https://img.shields.io/badge/Makefile-000000?style=for-the-badge&logo=gnu&logoColor=white) ![shfmt](https://img.shields.io/badge/shfmt-316688?style=for-the-badge)