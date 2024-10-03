from tkinter import *
from tkinter import ttk
import services


def main():
    def on_enviar():
        nome = nomeEntry.get()
        email = emailEntry.get()
        senha = senhaEntry.get()
        services.envair_dados(nome, email, senha)

        # Limpar o campo da digiatação
        nomeEntry.delete(0,END)
        emailEntry.delete(0,END)
        senhaEntry.delete(0,END)
        services.enviar_dados(nome, email, senha)

    def remover_usuario():
        email = emailEntry.get()
        services.remover_usuario(email)


    def listar_usuario():
        usuarios = services.listar_usuario()

        # Criar um ajanela para mostra a listar de ususario    
        listar_janela = Toplevel()
        listar_janela.geometry('400x300')
        listar_janela.title('Listar Usuários')

        # Criar uma Treeview (view, visualização) da lista de usuarios
        tree = ttk.Treeview(listar_janela, columns=('ID', 'Nome', 'Email'), show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Nome', text='Nome')
        tree.heading('Email', text='Email')

        # Criar um botão de voltar que ir fechar a tela inicial da listagem de usuário
        voltar_botao = Button(listar_janela, text='Voltar', width=10,command=listar_janela.destroy)
        voltar_botao.pack(fill=BOTH, expand=True, side=BOTTOM)

        tree.pack(fill=BOTH, expand=True)

        #Inserir os dados dos usuarios na Treeview
        for usuario in usuarios:
            # END vai inserir o item no final da tabela
            tree.insert('', END, values=usuario)
    
    janela = Tk()
    janela.geometry('400x300')
    janela.title('Sistema de Gerenciamento de Usuário')

    titulo = Label(janela, text='CRUD', font=('Atial Black', 20))
    titulo.pack(pady=30)

    # Nome
    nome = Label(janela, text='Nome:')
    nome.place(x=50, y=100)

    global nomeEntry
    nomeEntry = Entry(janela, width=30)
    nomeEntry.place(x=100, y=100)

    # Email
    email = Label(janela, text='Email')
    email.place(x=50, y=130)

    global emailEntry
    emailEntry = Entry(janela, width=30)
    emailEntry.place(x=100, y=130)

    #Senha
    senha = Label(janela, text='Senha:')
    senha.place(x=50, y=160)

    #Comando show para esconder a senha
    global senhaEntry
    senhaEntry = Entry(janela, width=30, show="*")
    senhaEntry.place(x=100, y=160)

    cadastrar = Button(janela, text='Cadastrar', width=10, command=on_enviar)
    cadastrar.place(x=100, y=200)    

    listar = Button(janela, text='Listar Usuários', width=15, command=listar_usuario)
    listar.place(x=200, y=200)

    remove = Button(janela, text='Remover', width=10, command=lambda: remover_usuario(email))
    remove.place(x=100, y=230)

    janela.mainloop()    
if __name__ == '__main__':
    main()