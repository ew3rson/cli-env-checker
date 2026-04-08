.PHONY: default run setup lint help # .PHONY impede o make de confundir os comandos com possíveis arquivos da pasta

# cores
GREEN=\033[32m
YELLOW=\033[33m
RESET=\033[0m

default: run # define o comando a ser executado ao usar apenas 'make'

run: setup
	@./cli-env-checker.sh # o @ oculta o comando e exibe apenas a saída

setup:
	@chmod +x cli-env-checker.sh calculadora.py

lint: # necessário ter shellcheck instalado
	@shellcheck cli-env-checker.sh

help:
	@printf "\n$(GREEN)--- COMANDOS DISPONÍVEIS ---$(RESET)\n\n"
	@printf " $(YELLOW)make$(RESET)             executa o projeto\n"
	@printf " $(YELLOW)make run$(RESET)         executa o projeto\n"
	@printf " $(YELLOW)make setup$(RESET)       concede permissão de execução\n"
	@printf " $(YELLOW)make lint$(RESET)        analisa o script com ShellCheck\n\n"
