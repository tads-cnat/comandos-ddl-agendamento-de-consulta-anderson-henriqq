[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Vw2CNNG5)
# dbdevcontainer-ifrn
- DevContainer Template para as disciplinas de Banco de Dados

## Executando o Docker Container localmente
$ docker-compose -f docker-compose.yml up

ou 

$ docker run --name db_server -e POSTGRES_PASSWORD=postgres -p 5433:5432 -d postgres