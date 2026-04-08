#!/usr/bin/env bash

# variáveis de cores para saída no terminal
GREEN="\033[32m"
YELLOW="\033[33m"
RED="\033[31m"
RESET="\033[0m"


verifica() {
    printf "%b\n" "\n${GREEN}🔮 Verificando dependências...\n${RESET}"
    sleep 1

    # verifica se python está instalado
    if command -v python3 &> /dev/null; then
        printf "%b\n" "${GREEN}✅ Python encontrado!${RESET}\n"
	sleep 1 # pequena pausa antes de continuar
    else
        printf "%b\n" "${RED}❌ Python não encontrado!${RESET}\nInstale-o com o comando 'sudo apt install python3'"
        exit 1 # encerra o script indicando erro
    fi

    # verifica se o arquivo existe
    if [ ! -f "calculadora.py" ]; then
        printf "%b\n" "${RED}❌ Erro! O arquivo 'calculadora.py' não foi localizado nesta pasta.${RESET}\n"
        exit 1
    fi

	# valida permissão 
	if [ ! -x calculadora.py ]; then
		printf "%b\n" "${YELLOW}⚠️ Concedendo permissão de execução...${RESET}\n"
		chmod +x calculadora.py
		sleep 1
	fi

    # executa o programa
    printf "%b\n" "${GREEN}🚀 Iniciando aplicação...${RESET}\n"
    sleep 1

    ./calculadora.py
}

verifica
