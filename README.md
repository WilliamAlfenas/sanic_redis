# Sanic + DockerCompose

O objetivo deste respositório é demonstrar o correto funcionamento do sanic e redis sendo subidos via docker-compose.

## Como executar este exemplo?

Após ter clonado este repositório, vá até a pasta do projeto e execute:

    docker-compose up

Aguarde o build do serviços e então acesse:

    http://localhost:8000/

Ele te dará uma contagem de tasks, repare que você também terá os seguintes cmds disponíveis:

    http://localhost:8000/add_task

O cmd acima tem um sleep de 10 segs, enquanto ele roda experimente rodar em outro navegador:

    http://localhost:8000/count

Ele deverá responder de imediado dado a arquitetura async do Sanic. Experimente também acessar a task que você criou:
    http://localhost:8000/query/0

Note que os ids das tasks iniciam por 0 - fique a vontade para rodar mais testes com o serviço.