# Servidor_Diretorios
Servidor de diretórios para descoberta de servidores, onde aplicação RPC cliente-servidor, é baseada num serviço de diretórios, isto é, para que o cliente possa contatar o servidor desejado, ele precisa antes saber o endereço do servidor para destinar a mensagem para o caminho certo, mas para descobrir o endereço do servidor desejado, o cliente antes contacta um servidor/serviço de diretórios que contém uma lista com todos os servidores ativos no momento e esse servidor de diretórios irá retornar o IP e Porta do servidor desejado pelo cliente.


## Requisitos
[python 3.8.5](https://www.python.org/downloads/release/python-385/)

## Como rodar
1) Instale o pip3 e o virtualenv do python 3
```shell
sudo apt update
sudo apt install python3-pip python3-virtualenv -y
```

2) Clone o projeto
```shell
git clone https://mrleduardo@bitbucket.org/mrleduardo/new-p2-2021.git
```

3) Instale o virtualenv no diretorio do projeto e o inicie
```shell
cd new-p2-2021.git
virtualenv .venv
source ./.venv/bin/activate
```

4) Instale as dependencias do projeto
```shell
pip install -r requeriments.txt
```

### Edite o `constRPYC.py` para apontar para o servidor de  dirertórios

5)   Inicie o servidor com
```shell
cd app
python serverDirectory.py
```

Lembre-se que para cada instancia da AWS todos os passos são necessários. Caso já tenha instalado e desconectou da maquina sem querer, basta executar o virtualenv com o comando `source ./.venv/bin/activate` na pasta do projeto e seguir o passo 5 novamente.# Servidor_Diretorios
Servidor de diretórios para descoberta de servidores, onde aplicação RPC cliente-servidor, é baseada num serviço de diretórios, isto é, para que o cliente possa contatar o servidor desejado, ele precisa antes saber o endereço do servidor para destinar a mensagem para o caminho certo, mas para descobrir o endereço do servidor desejado, o cliente antes contacta um servidor/serviço de diretórios que contém uma lista com todos os servidores ativos no momento e esse servidor de diretórios irá retornar o IP e Porta do servidor desejado pelo cliente.


## Requisitos
[python 3.8.5](https://www.python.org/downloads/release/python-385/)

## Como rodar
1) Instale o pip3 e o virtualenv do python 3
```shell
sudo apt update
sudo apt install python3-pip python3-virtualenv -y
```

2) Clone o projeto
```shell
git clone https://mrleduardo@bitbucket.org/mrleduardo/new-p2-2021.git
```

3) Instale o virtualenv no diretorio do projeto e o inicie
```shell
cd new-p2-2021.git
virtualenv .venv
source ./.venv/bin/activate
```

4) Instale as dependencias do projeto
```shell
pip install -r requeriments.txt
```

### Edite o `constRPYC.py` para apontar para o servidor de  dirertórios

5)   Inicie o servidor com
```shell
cd app
python serverDirectory.py
```

Lembre-se que para cada instancia da AWS todos os passos são necessários. Caso já tenha instalado e desconectou da maquina sem querer, basta executar o virtualenv com o comando `source ./.venv/bin/activate` na pasta do projeto e seguir o passo 5 novamente.
