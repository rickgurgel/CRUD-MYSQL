import random
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='130128',
    database='bd_produtos'
)

cursor = conexao.cursor()
menu = True

while menu:
    print('MENU DO SISTEMA')
    print('1- ADICIONAR ELEMENTOS AO BANCO DE DADOS')
    print('2- LER BANCO DE DADOS')
    print('3- ALTERAR ELEMENTOS AO BANCO DE DADOS')
    print('4- DELETAR ELEMENTOS AO BANCO DE DADOS')
    print('PARA SAIR DIGITE QUALQUER VALOR...')
    option = int(input('Digite a opção desejada:'))
    if option == 1:
        # CREATE
        CODIGO = input('Digite o codigo do produto:')
        FORNECEDOR = input('Digite o fornecedor do produto:')
        NOME_PRODUTO = input('Digite o nome do produto:')
        QTDE = int(input('Digite a quantidade do produto em estoque:'))
        VALOR = float(input('Digite o valor do produto:'))
        SALDO = QTDE * VALOR
        print('PRODUTO: ')
        print(CODIGO)
        print(FORNECEDOR)
        print(NOME_PRODUTO)
        print(QTDE)
        print(VALOR)
        print(SALDO)
        insere_na_tabela = f'INSERT INTO deposito (CODIGO, FORNECEDOR, NOME_PRODUTO, QTDE, VALOR, SALDO) VALUES (' \
                           f'{CODIGO}, "{FORNECEDOR}", "{NOME_PRODUTO}", {QTDE}, {VALOR}, {SALDO})'
        cursor.execute(insere_na_tabela)
        conexao.commit()
        check = input('Deseja adicionar outro produto? Y/N?')
        # if check == 'Y' or check == 'y' or check == 'SIM' or check == 'yes' or check == 'sim':
        #     option = 1
        # else:
        #     print('Voltando ao menu principal...')
        # menu = True

    elif option == 2:
        # READ
        print('Você pode pesquisar por:')
        print('1- CODIGO')
        print('2- FORNECEDOR')
        print('3- NOME_PRODUTO')
        print('4- QUANTIDADE')
        print('PARA SAIR DIGITE QUALQUER VALOR...')
        option_read = int(input('Informe a opção desejada:'))
        if option_read == 1:
            ler_tabela = f'SELECT CODIGO FROM deposito'
            cursor.execute(ler_tabela)
            resultado = cursor.fetchall()
            print('Fornecedores:')
            print(resultado)
            menu = True
        if option_read == 2:
            ler_tabela = f'SELECT FORNECEDOR FROM deposito'
            cursor.execute(ler_tabela)
            resultado = cursor.fetchall()
            print('Fornecedores:')
            print(resultado)
            menu = True
        elif option_read == 3:
            ler_tabela = f'SELECT NOME_PRODUTO FROM deposito'
            cursor.execute(ler_tabela)
            resultado = cursor.fetchall()
            print('Produtos:')
            print(resultado)
            menu = True
        elif option_read == 4:
            ler_tabela = f'SELECT QTDE FROM deposito'
            cursor.execute(ler_tabela)
            resultado = cursor.fetchall()
            print('Quantidades:')
            print(resultado)
            menu = True

    elif option == 3:
        # UPDATE
        print('ALTERAR DADOS DE PRODUTOS')
        aux = int(input('Digite o CÓDIGO do produto que você gostaria de alterar: '))
        ler_tabela = f'SELECT * FROM deposito WHERE CODIGO LIKE {aux}'
        cursor.execute(ler_tabela)
        resultado = cursor.fetchall()
        print(resultado)
        print('1- ALTERAR FORNECEDOR')
        print('2- ALTERAR NOME DO PRODUTO')
        print('3- ALTERAR QUANTIDADE DO PRODUTO')
        print('4- ALTERAR VALOR DO PRODUTO')
        print('PARA SAIR DIGITE QUALQUER VALOR...')
        read_option = int(input('Selecione o dado que você deseja alterar: '))
        if read_option == 1:
            NOVO_FORNECEDOR = input('Digite o novo fornecedor para este produto')
            atualiza_tabela = f'UPDATE deposito SET FORNECEDOR = "{NOVO_FORNECEDOR}" WHERE CODIGO = {aux}'
            cursor.execute(atualiza_tabela)
            conexao.commit()
            option == 3
        elif read_option == 2:
            NOVO_NOME_PRODUTO = input('Digite o novo nome para este produto: ')
            atualiza_tabela = f'UPDATE deposito SET NOME_PRODUTO = "{NOVO_NOME_PRODUTO}" WHERE CODIGO = {aux}'
            cursor.execute(atualiza_tabela)
            conexao.commit()
            option == 3
        elif read_option == 3:
            NOVA_QTDE = int(input('Digite a nova quantidade deste produto: '))
            atualiza_tabela = f'UPDATE deposito SET QTDE = {NOVA_QTDE} WHERE CODIGO = {aux}'
            cursor.execute(atualiza_tabela)
            conexao.commit()
            option == 3
        elif read_option == 4:
            NOVO_VALOR = float(input('Digite o novo valor deste produto: '))
            atualiza_tabela = f'UPDATE deposito SET VALOR = {NOVO_VALOR} WHERE CODIGO = {aux}'
            cursor.execute(atualiza_tabela)
            conexao.commit()
            option == 3
        else:
            menu = True

    elif option == 4:
        # DELETE
        CODIGO = int(input('Digite o código do produto a ser deletado: '))
        deleta_tabela = f'DELETE FROM deposito WHERE CODIGO = {CODIGO}'
        cursor.execute(deleta_tabela)
        conexao.commit()
        menu = True

    else:
        print('Encerrando...')
        cursor.close()
        conexao.close()
        exit()

