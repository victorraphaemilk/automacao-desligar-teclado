### README

# Desativar Teclado Interno do Linux com `xinput`

Este script utiliza o comando `xinput` para desativar o teclado interno de um sistema Linux. Ele identifica o teclado pelo nome e o desativa usando seu ID. É útil para situações em que o teclado interno apresenta defeitos ou precisa ser temporariamente desativado.

---

## Requisitos

1. **Python**: Certifique-se de que o Python 3 está instalado no sistema.
2. **xinput**: O comando `xinput` deve estar disponível. Em distribuições baseadas em Debian/Ubuntu, instale com:
   ```bash
   sudo apt install xinput
   ```

---

## Como Funciona

1. O script utiliza a biblioteca `subprocess` para executar comandos do terminal.
2. Ele executa o comando `xinput list` para listar todos os dispositivos de entrada conectados.
3. Busca pelo dispositivo chamado `AT Translated Set 2 keyboard`.
4. Se encontrado:
   - Obtém o ID do teclado.
   - Executa o comando `xinput float` com o ID, desativando o teclado.
   - Exibe a mensagem **"teclado desativado"**.
5. Se não for encontrado ou o processo falhar, exibe a mensagem **"não conseguiu desativar teclado"**.

---

## Uso

1. Execute o script com permissões suficientes (recomenda-se como superusuário):
   ```bash
   sudo python3 script.py
   ```
2. Certifique-se de que o nome do teclado interno está correto. Por padrão, o script procura por `AT Translated Set 2 keyboard`. Caso o nome do dispositivo seja diferente, ajuste esta linha no código:
   ```python
   if "AT Translated Set 2 keyboard" in line:
   ```

---

## Pontos de Atenção

- **Risco de perder acesso ao teclado**: Após desativar o teclado interno, pode ser necessário usar um teclado externo para reativá-lo.
- **Edição do script**: Caso o nome do dispositivo no seu sistema seja diferente, ajuste o valor na condição para corresponder ao nome correto exibido pelo comando `xinput list`.

---

## Exemplo de Saída

### Caso o teclado seja desativado com sucesso:
```
teclado achado
teclado desativado
```

### Caso o teclado não seja encontrado ou não possa ser desativado:
```
não conseguiu desativar teclado
```

---

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou soluções alternativas!
