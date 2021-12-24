'''
    Criar Funções para serem utilizadas em outros arquivos
'''
from tkinter.messagebox import NO


def Insert_Data(nome, nascimento, cpf, email, senha):
    try:
        import mysql.connector
        connection = mysql.connector.connect(host='localhost', database='usuarios', user='root', password='matheus.rodrigues.araujo.083')
        cursor = connection.cursor()
        cursor.execute(
            f'''
            INSERT INTO `informacoes`(`nome`, `nascimento`, `cpf`, `email`, `senha`) VALUES('{nome}','{nascimento}','{cpf}', '{email}','{senha}')
            ''',
            )

        connection.commit()
        connection.close()

    except Exception as error:
        print(error)
