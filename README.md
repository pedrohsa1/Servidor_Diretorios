![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white) ![Spring Boot](https://img.shields.io/badge/Spring_Boot-F2F4F9?style=for-the-badge&logo=spring-boot) ![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## Ledger

O sistema Ledger foi desenvolvido como projeto da disciplina Residência Técnica em Sistemas de Informação promovida pelo Instituto de Informática da Universidade Federal de Goiás.
O sistema foi construindo para auxiliar a Defesa Civil no registro de ocorrências de desastres, facilitando e padronizando o registro dos danos ocorridos e agilizando o preenchimento do FIDE (Formulário de Informações de Desastres).

## Autores
- [Icaro Aguiar Perez](https://www.github.com/icaro1508)
- [Marcos Vinícius de Souza Oliveira](https://www.github.com/MarcosVSO)
- [Pedro Henrique Souza Arcanjo](https://www.github.com/pedrohsa1)
- [Vitor Abreu Bitencurt]()

## Pré-Requisito

* JDK 11.0.13
* Spring-boot 2.6.4
* Maven 3.8.1

## Passos para execução do projeto

1. Clone do repositório
   ```sh
   git clone https://github.com/MarcosVSO/ledger.git
   ```
2. Instalar dependências
   ```sh
   mvn install
   ```
2. Executar projeto
   ```sh
   mvn spring-boot:run
   ```

## Endpoints

### Áreas Afetada

- Listar todas as áreas afetada

`GET /areas-afetadas`

    curl -i -H 'Accept: application/json' http://localhost:9000/areas-afetadas

### Cobrade

- Listar todos os cobrade

`GET /cobrade`

    curl -i -H 'Accept: application/json' http://localhost:9000/cobrade

### Danos

- Listar todos os danos ambientais

`GET /danos/ambientais`

    curl -i -H 'Accept: application/json' http://localhost:9000/danos/ambientais

- Listar todos os danos materiais

`GET /danos/materiais`

    curl -i -H 'Accept: application/json' http://localhost:9000/danos/materiais

- Buscar pelo ID do dano ambiental

`GET /danos/ambientais/{idDano}`

    curl -i -H 'Accept: application/json' http://localhost:9000/danos/ambientais/{idDano}

- Buscar pelo ID do dano humano

`GET /danos/humanos/{idDano}`

    curl -i -H 'Accept: application/json' http://localhost:9000/danos/humanos/{idDano}

- Buscar pelo ID do dano material

`GET /danos/materiais/{idDano}`

    curl -i -H 'Accept: application/json' http://localhost:9000/danos/materiais/{idDano}

- Inserir dano humano

`POST /danos/humanos/add`

    curl -i -H 'Accept: application/json' -X POST -d 'attr=attr' http://localhost:9000/danos/humanos/add

- Inserir dano material

`POST /danos/materiais/add`

    curl -i -H 'Accept: application/json' -X POST -d 'attr=attr' http://localhost:9000/danos/materiais/add

- Inserir dano ambiental

`POST /danos/ambientais/add`

    curl -i -H 'Accept: application/json' -X POST -d 'attr=attr' http://localhost:9000/danos/ambientais/add


### Tipos de Danos

- Listar todos os tipos de danos humanos

`GET /danos-tipos/humanos`

    curl -i -H 'Accept: application/json' http://localhost:9000/danos-tipos/humanos

- Listar todos os tipos de danos materiais

`GET /danos-tipos/materiais`

    curl -i -H 'Accept: application/json' http://localhost:9000/danos-tipos/materiais

- Listar todos os tipos de danos ambientais

`GET /danos-tipos/ambientais`

    curl -i -H 'Accept: application/json' http://localhost:9000/danos-tipos/ambientais

### Ocorrências

- Listar todas as ocorrências

`GET /ocorrencias`

    curl -i -H 'Accept: application/json' http://localhost:9000/ocorrencias

- Lista paginada de ocorrências filtrando pelo Cobrade e Status

`GET /ocorrencias/list`

    curl -i -H 'Accept: application/json' http://localhost:9000/ocorrencias/list

- Buscar pelo cobrade

`GET /ocorrencias/cobrade/{cobrade}`

    curl -i -H 'Accept: application/json' http://localhost:9000/ocorrencias/cobrade/{cobrade}

- Buscar pela UF

`GET /ocorrencias/uf/{uf}`

    curl -i -H 'Accept: application/json' http://localhost:9000/ocorrencias/uf/{uf}

- Buscar pelo municipio

`GET /ocorrencias/municipio/{municipio}`

	curl -i -H 'Accept: application/json' http://localhost:9000/ocorrencias/municipio/{municipio}
	
- Gerar FIDE da ocorrência

`GET /ocorrencias/gerar-fide/{idOcorrencia}`

    curl -i -H 'Accept: application/json' http://localhost:9000/ocorrencias/gerar-fide/{idOcorrencia}

- Buscar pelo ID da ocorrência

`GET /ocorrencias/{idOcorrencia}`

    curl -i -H 'Accept: application/json' http://localhost:9000/ocorrencias/{idOcorrencia}

- Inserir nova ocorrencias

`POST /ocorrencias/add`

	curl -i -H 'Accept: application/json' -X POST -d 'attr=attr' http://localhost:9000/ocorrencias/add
	
- Buscar todos os danos ambientais da ocorrência

`GET /ocorrencias/{idOcorrencia}/danos-ambientais`

    curl -i -H 'Accept: application/json' http://localhost:9000/ocorrencias/{idOcorrencia}/danos-ambientais

- Buscar todos os danos materiais da ocorrência

`GET /ocorrencias/{idOcorrencia}/danos-materiais`

    curl -i -H 'Accept: application/json' http://localhost:9000/ocorrencias/{idOcorrencia}/danos-materiais

- Gerar documento da Ocorrências

`GET /ocorrencias/gerar-documento/{idOcorrencia}`

    curl -i -H 'Accept: application/json' http://localhost:9000/ocorrencias/gerar-documento/{idOcorrencia}

### Telefone

- Listar todos os telefones

`GET /telefones`

    curl -i -H 'Accept: application/json' http://localhost:9000/ocorrencias/telefones
