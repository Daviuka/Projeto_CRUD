from conexao import *

def enviar_dados(nome, email, senha):
    criar_usuario(nome, email, senha)


def criar_usuario(nome, email, senha):
    if conn.is_connected():
        print('Banco conectado com sucesso!') 
        
        cursor = conn.cursor()

        sql = ' INSERT INTO usuario (nome, email, senha) values (%s, %s, %s)'
        values = (nome, email, senha)

        cursor.execute(sql, values)
        conn.commit()
        conn.close()
        conn.close()

    else:
        print("Falha m ao conectar com o banco!")

def listar_usuario():
    if conn.is_connected():
        print('Banco conectado com sucesso!') 
        
        cursor = conn.cursor()
    
        cursor.execute('select id, nome, email from usuario;')

        usuarios = cursor.fetchall()
        cursor.close
        return usuarios
    else:
        print("Falha ao conectar com o banco!")

def remover_usuario(email):
    if conn.is_connected():
        print('Banco conectado com sucesso!') 
        
        cursor = conn.cursor()
        
        sql_select = 'select id, nome, email from usuario where email=%s;'
        cursor.execute(sql_select, (email,))

        usuario = cursor.fetchone()
        if usuario:
            print(f'Usuário {usuario[1]} foi removido com sucesso!')
            sql_delete = 'delete from usuario where email=%s;'
            cursor.execute(sql_delete, (email,))
            conn.commit()
            cursor.close()
            conn.close()

        else:
            print(f'Usuário com email {email} não encontrado!')
