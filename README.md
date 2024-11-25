# Sel0337
Tarefa Sel0337
Igor Souza Caproni - 11233032
Rafael Quaglia Te - 13827292

# Projeto: Controle de LEDs com Raspberry Pi 3
Este projeto utiliza duas funções em Python para controlar LEDs conectados a uma Raspberry Pi 3. As funções estão configuradas para serem gerenciadas pelo systemd, de modo que:

A primeira função (led_pisca1.py) é iniciada automaticamente durante o boot.
A segunda função (led2.py) é iniciada automaticamente quando a execução da primeira função é encerrada.
Descrição dos Scripts
## 1. led_pisca1.py
Controla um LED conectado ao pino GPIO 24.
O LED alterna entre ligado (HIGH) e desligado (LOW) com um intervalo de 2 segundos.
Inclui limpeza da configuração GPIO ao finalizar a execução.
## 2. led2.py
Controla um LED conectado ao pino GPIO 18.
Mantém o LED ligado continuamente.
É configurado para iniciar automaticamente quando o script led_pisca1.py é encerrado.
Inclui tratamento de exceções para desligar o LED e limpar a configuração GPIO em caso de erro.

## Funcionamento do arquivo blinky.service
O arquivo blinky.service é uma unidade de serviço do systemd que define como e quando um script Python será executado na Raspberry Pi. 
**ExecStart:** Define o comando que será executado ao iniciar o serviço. No caso, o script Python que controla o LED.
**ExecStop:** Define o comando que será executado ao parar o serviço anterior à partir do comando 
### Localização do Arquivo
O arquivo blinky.service deve ser copiado para o diretório:
/etc/systemd/system/
Esse é o local onde o systemd armazena as unidades de serviço personalizadas.

- Para ativar o serviço e configurá-lo para iniciar automaticamente durante o boot:
sudo systemctl enable blinky.service
- Se quiser iniciar o serviço imediatamente:
sudo systemctl start blinky.service

Para parar o serviço manualmente, o que fará a próxima função começar, basta utilizar:
sudo systemctl stop blinky.service

O video do funcionamento do projeto, que mostra que ao iniciar o sistema, o LED vermelho é aceso automaticamente, e ao finalizar o mesmo, a rotina que faz o LED verde piscar é ativada:


https://github.com/user-attachments/assets/111d6a56-2449-4582-b20d-9f7194a99213

