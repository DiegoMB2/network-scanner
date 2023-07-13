# Network Scanner - Detecção de Dispositivos de Rede

# Descrição:
O Network Scanner é uma ferramenta em Python que permite detectar e listar dispositivos de rede em uma rede local. Utilizando a biblioteca python-nmap em conjunto com o utilitário nmap, o script realiza uma varredura na rede e fornece informações como endereço IP, endereço MAC e fabricante dos dispositivos encontrados.

# Recursos:

Detecta e lista dispositivos de rede em uma rede local.
Exibe informações como endereço IP, endereço MAC e fabricante dos dispositivos.
Utiliza a biblioteca python-nmap para realizar a varredura na rede.

# Requisitos de Instalação:

Python 3.x
Biblioteca python-nmap

# Como Usar:

## Instale o nmap em seu sistema Linux:

sudo apt-get install nmap

## Instale a biblioteca python-nmap:

pip install python-nmap

## Execute o script network_scanner.py:

python network_scanner.py

# Exemplo de Saída:

IP: 192.168.0.1      MAC: 12:34:56:78:90:AB     Vendor: Cisco Systems, Inc.

IP: 192.168.0.10     MAC: AB:CD:EF:12:34:56     Vendor: Unknown

# Melhorias Futuras:

Adicionar recursos avançados de análise de rede, como identificação de serviços em execução nos dispositivos.
Aprimorar a detecção de dispositivos, incluindo dispositivos conectados por Wi-Fi.

# Problemas Conhecidos:

O script pode levar mais tempo para executar em redes maiores com muitos dispositivos.

# Contribuição:

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull (pull requests).

# Licença:

Este projeto está licenciado sob a Apache 2.0. Consulte o arquivo LICENSE para obter mais detalhes.

# Agradecimentos:

Este projeto utiliza a biblioteca python-nmap para interagir com o utilitário nmap e é inspirado pelo interesse em segurança de rede e descoberta de dispositivos.

