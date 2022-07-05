# Bot Excel
## Libs usadas:
- JSON;
- Pathlib;
- Pyautogui;
- Time;
- Pyperclip
- Keyboard

Com base no que realizo de atividades para minha mãe no Excel, vi que eu poderia automatizar algumas tarefas repetitivas do processo de trabalho, então eu tive a ideia de realizar este programa, que apenas com alguns comandos realiza a maior parte das tarefas de inclusão de conteúdo em células e ajuste de linhas.

Primeiramente tive que realizar um Web Scraping para resgatar dados de um site para conseguir as informações necessárias para uma parte do programa, em seguida salvadas em um arquivo JSON, após isso o processo de desenvolvimento do programa foi simples utilizando bastante o pyautogui e o pyperclip.

O pyautogui, juntamente com o keyboard, foram utilizados para executarem comandos do computador para ir até a janela do Excel, mover para outra célula, ajustar e centralizar as linhas, etc.

Com o pyperclip pude copiar as informações que já foram salvas no arquivo JSON para a área de transferência do computador e então, colando nas células.

Acredito que o programa já está finalizado, pude refatorar o máximo possível para deixá-lo mais otimizado, todo o código fonte está funcionando perfeitamente.
