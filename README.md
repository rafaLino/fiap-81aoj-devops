# Trabalho Final

![](img/arquitetura.png)



Nessa arquitetura um barramento do eventBridge vai receber todos os eventos de uma pizzaria. Desde o pedido até a entrega. Onde cada um dos eventos deve ser guardados no banco de dados dynamo e apenas os eventos de pizza pronta que devem ser adicionados a fila SQS que posteriormente deve ser consumida por outro lambda.


### Passos

1. Criar manualmente um novo barramento de eventos no eventBridge, o banco de dados DynamoDB e a fila SQS.
   1. EventBridge:
      1. Nome = pizzaria
   2. DynamoDB:
      1. Chave de partição: pedido(String)
      2. Chave de pesquisa: status(String)
      3. Nome: eventos-pizzaria
   3. Fila SQS:
      1. Tipo: Standard
      2. Nome: espera-entrega
2. instalar 
   ```console
    npm install -g serverless
    ```
   ```console
    npm install -g c9
   ```
   ```console
    git clone https://github.com/rafaLino/fiap-81aoj-devops.git
   ```
3. executar
    ```console
       pip3 install virtualenv && python3 -m venv ~/venv
    ```
    ```console
       pip3 install boto3
    ```
     ```console
       source ~/venv/bin/activate
    ```
     ```console
       sls deploy --verbose
    ```
     ```console
       python3 putEventsPizzaria.py
    ```

  

