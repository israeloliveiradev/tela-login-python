import customtkinter as ctk
import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import PhotoImage


# Criando e conectando DB
class BackEnd():
    def conecta_db(self):
        self.conn = sqlite3.connect("Sistema_cadastros.db")
        self.cursor = self.conn.cursor()
        print("Banco de Dados conectado com sucesso")

    def desconecta_db(self):
        self.conn.close()
        print ("Banco de Dados desconectado com sucesso")

    def cria_tabela(self):
        self.conecta_db()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL,
            Email TEXT NOT NULL,
            Senha TEXT NOT NULL,
            Confirma_Senha TEXT NOT NULL
            );
        """)
        self.conn.commit()
        print("Tabela Criada com Sucesso!")
        self.desconecta_db()

    def cadastrar_usuario(self):
        self.username_cadastro = self.username_cadastro_entry.get()
        self.email_cadastro = self.email_cadastro_entry.get()
        self.password_cadastro = self.senha_cadastro_entry.get()
        self.confirma_senha_cadastro = self.confirma_senha_entry.get()

        self.conecta_db()

        self.cursor.execute("""
            INSERT INTO Usuarios (Username, Email, Senha, Confirma_Senha)
            VALUES (?, ?, ?, ?)""", (self.username_cadastro, self.email_cadastro, self.password_cadastro, self.confirma_senha_cadastro))

        try:
            if(self.username_cadastro == "" or self.email_cadastro == "" or self.password_cadastro == "" or
            self.confirma_senha_cadastro == ""):
                messagebox.showerror(title="Sistema de Login", message=" ERRO!!! \nPor Favor preencha todos os campos")

            elif (len(self.username_cadastro)< 4):
                messagebox.showwarning(title="Sistema de Login", message="O Nome de usuario deve ter no mínino 4 caracteres.")

            elif (len(self.password_cadastro) < 4):
                 messagebox.showwarning(title="Sistema de Login", message=" A Senha deve ter no mínino 7 caracteres.")

            elif (self.password_cadastro != self.confirma_senha_cadastro):
                messagebox.showerror(title="Sistema de Login", message=" ERRO!!!\nAs senhas não correspondem.")

            else:
                self.conn.commit()
                messagebox.showinfo(title="Sistema de Login", message=f"Parabéns! {self.username_cadastro}\n Os seus dados foram cadastrados com sucesso!")
                self.desconecta_db()
                self.limpa_entry_cadastro()


        except:
            messagebox.showerror(title="Sistema de Login", message="Erro no procecessamento do seu cadastro!\n Tente Novamamente!")
            self.desconecta_db()


    def verifica_login(self):
        self.username_login = self.username_login_entry.get()
        self.senha_login = self.password_login_entry.get()

        self.conecta_db()

        self.cursor.execute(""" SELECT * FROM Usuarios WHERE (Username = ? AND Senha = ?)""", (self.username_login, self.senha_login))

        self.verifica_dados = self.cursor.fetchone() # PERCORRENDO PELA TABELA USUARIOS

        try:

            if (self.username_login == "" or self.senha_login == ""):
                messagebox.showwarning(title="Sistema de Login", message="Preencha todos os campos")

            elif (self.username_login in self.verifica_dados and self.senha_login in self.verifica_dados ):
                messagebox.showinfo(title="Sistema de Login", message=f"Parabéns, {self.username_login}\n Login feito com sucesso!")
                self.desconecta_db()
                self.limpa_entry_login()

                #Fechar Tela Login

                self.destroy()

                #Abrir Menu

                self.config_menu_prin = MenuPrincipal()





        except:
            messagebox.showerror(title="Sistema de Login", message="ERRO! \n Dados não encontrados em nosso sistema. \n  Por Favor, Tente Novamente.")
            self.desconecta_db()




#Menu Principal
class MenuPrincipal(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()
        self.config_menu_prin()
        self.Tela_Principal_Programa()


    #Config Menu Principal
    def config_menu_prin(self):
        self.largura_janela = 1080
        self.altura_janela = 720
        self.title("Menu Principal")

        # Obter as dimensões da tela
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        # Calcular as coordenadas para centralizar a janela
        pos_x = (largura_tela - self.largura_janela) // 2
        pos_y = (altura_tela - self.altura_janela) // 2

        # Definir as dimensões e coordenadas para centralizar a janela
        self.geometry(f"{self.largura_janela}x{self.altura_janela}+{pos_x}+{pos_y}")

        # Impedir que a janela seja redimensionada
        self.resizable(False, False)








    #Config Tela Principal
        # MUDANÇA DARK E LIGHT
    def ChangeMode(self):
        self.val = self.switch.get()
        if self.val:
            ctk.set_appearance_mode("light")
            print("Modo do sistema aplicado")

        else:
            ctk.set_appearance_mode("dark")
            print("Modo escuro aplicado")

    def Tela_Principal_Programa(self):

        #Imagens

        # Frame Titulo Principal

        self.frame_titulo = ctk.CTkFrame(self, width=220, height=720, fg_color="white")
        self.frame_titulo.place(x=0, y=0)

        #Titulo da Tela Principal

        # self.logomenu = PhotoImage(file="LOGO MENU (2).png")
        # self.lb2_menu = ctk.CTkLabel(self, text=None, image=self.logomenu)
        # self.lb2_menu.place(relx=0.20, rely=0.30, anchor="c")

        # self.img = PhotoImage(file="FINAL.png")
        # self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        # self.lb_img.place(relx=0.25, rely=0.53, anchor="c")
        #Botoes Tela Principal

        self.img_btn_home = PhotoImage(file="223.png")

        self.btn_home = ctk.CTkButton(self.frame_titulo, width=220, height=40,corner_radius=0, text="HOME".upper(), font=("calibri", 20, "bold"), bg_color="transparent", image=(self.img_btn_home), compound=ctk.LEFT)
        self.btn_home.place(relx=0.5, rely=0.17, anchor="c")

        self.btn_clientes = ctk.CTkButton(self.frame_titulo, width=220, height=40,corner_radius=0, text="CLIENTES",font=("calibri", 20, "bold"))
        self.btn_clientes.place(relx=0.5, rely=0.22, anchor="c")

        self.btn_add_prod = ctk.CTkButton(self.frame_titulo, width=220, height=40, corner_radius=0, text="ADICIONAR PRODUTOS".upper(), font=("calibri", 20, "bold"))
        self.btn_add_prod.place(relx=0.5, rely=0.27, anchor="c")

        self.btn_excluir_prod = ctk.CTkButton(self.frame_titulo, width=220, height=40, corner_radius=0,
        text="EXCLUIR PRODUTOS".upper(), font=("calibri", 20, "bold"))
        self.btn_excluir_prod.place(relx=0.5, rely=0.32, anchor="c")

        self.btn_visualizar_estoque = ctk.CTkButton(self.frame_titulo, width=220, height=40, corner_radius=0,
        text="ESTOQUE".upper(), font=("calibri", 20, "bold"))
        self.btn_visualizar_estoque.place(relx=0.5, rely=0.37, anchor="c")







        #Option Menu

        # self.opcoes_tema = ctk.CTkLabel(self.frame_titulo, text="ESCOLHA O SEU TEMA".upper(), corner_radius=20, font=("calibri", 15, "bold"))
        # self.opcoes_tema.grid(row=5, column=0, pady=10, padx=10)
        # self.opcoes_mudar_tema = ctk.CTkOptionMenu(self.frame_titulo, values=("DARK", "LIGHT"))
        # self.opcoes_mudar_tema.grid(row=6, column=0, pady=10, padx=10)
        #
        self.switch = ctk.CTkSwitch(self.frame_titulo, text="Dark Mode", onvalue=0, offvalue=1, command=self.ChangeMode)
        self.switch.place(relx=0.5, rely=0.97, anchor="c")

        #Frame Principal

        self.frame_principal = ctk.CTkFrame(self, width=787, height=720, corner_radius=0, fg_color="transparent")
        self.frame_principal.place(x=293, y=0)




#Tela de Login/Cadastro
class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.configuracoes_da_janela_inicial()
        self.tela_login()
        self.cria_tabela()






     #CONFIG A JANELA PRINCIPAL
    def configuracoes_da_janela_inicial(self):
        self.largura_janela_app = 700
        self.altura_janela_app = 400

        # Obter as dimensões da tela
        largura_tela_app = self.winfo_screenwidth()
        altura_tela_app = self.winfo_screenheight()

        # Calcular as coordenadas para centralizar a janela
        pos_x_app = (largura_tela_app - self.largura_janela_app) // 2
        pos_y_app = (altura_tela_app - self.altura_janela_app) // 2

        # Definir as dimensões e coordenadas para centralizar a janela
        self.geometry(f"{self.largura_janela_app}x{self.altura_janela_app}+{pos_x_app}+{pos_y_app}")

        self.resizable(False, False)
        self.title("StockMaster 1.0")



    #TELA DE LOGIN
    def tela_login(self):

        # Titulo da Plataforma
        # Titulo da Plataforma
        # self.nome_foto = PhotoImage(file="NOME.png")
        # self.lb1_nome = ctk.CTkLabel(self, text=None, image=self.nome_foto)
        # self.lb1_nome.place(x=100, y=100)

        #Trabalhando com as Imagens
        self.img = PhotoImage(file="FINAL.png")
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.place(relx=0.25, rely=0.53, anchor="c")




        #Criar Frame Formulario de Login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380, fg_color="white", corner_radius=15)
        self.frame_login.place(x=350, y=10)

        #Colocando Widgets dentro do frame - formulario de login
        self.lb_title = ctk.CTkLabel(self.frame_login, text="Faça o seu Login".upper(), font=("calibri", 20, "bold"), text_color="#333333")
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="USUARIO", font=("calibri", 16), corner_radius=15, border_color="#A6A6A6")
        self.username_login_entry.grid(row=1, column=0, padx=10, pady=10)

        self.password_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="SENHA",font=("calibri", 16), show="*", corner_radius=15, border_color="#A6A6A6")
        self.password_login_entry.grid(row=2, column=0, padx=10, pady=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_login,text= "Clique para ver a senha".upper(),font=("calibri", 14), corner_radius=5, border_color="#A6A6A6", onvalue=0, offvalue=1, command=self.ShowPass, fg_color="#4E9343", hover_color="#4E9343")
        self.ver_senha.grid(row=3, column=0, padx=10, pady=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, text="Fazer Login".upper(), font=("calibri", 20, "bold"), corner_radius=15, command=self.verifica_login, fg_color="#4E9343", hover_color="#2E7D32", text_color="#FFFFFF")
        self.btn_login.grid(row=4, column=0, padx=10, pady=10)
        
        #Cadastro

        # frame para ocupar espaço
        self.frame_login = ctk.CTkFrame(self.frame_login, height=10, fg_color="transparent")
        self.frame_login.grid(row=5, column=0, padx=10, pady=44)

        self.sap = ctk.CTkLabel(self.frame_login, text="Não tem uma conta? Crie aqui".upper(), font=("calibri", 14))
        self.sap.grid(row=7, column=0, padx=10, pady=0)

        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=300, text="Criar uma Conta".upper(), font=("calibri", 18, "bold"), corner_radius=15, fg_color="#F4B74F", command=self.tela_de_cadastro, hover_color="#FFD54F", text_color="#FFFFFF")
        self.btn_cadastro.grid(row=8, column=0, padx=10, pady=0)

    #CONFIG CHECKBOX SENHA
    def ShowPass(self):
        self.teste_box = self.ver_senha.get()

        if self.teste_box:
            self.password_login_entry.configure(show="*")

        else:
            self.password_login_entry.configure(show="")

    def tela_de_cadastro(self):
        #REMOVER O FORMULARIO DE LOGIN
        self.frame_login.place_forget()


        #Frame de formulario de cadastro
        self.frame_for_cadastro = ctk.CTkFrame(self, width=350, height=380, fg_color="white", corner_radius=15)
        self.frame_for_cadastro.place(x=350, y=10)


        #CRIANDO TITULO
        self.lb_title = ctk.CTkLabel(self.frame_for_cadastro, text="Faça o Seu Cadastro".upper(), font=("calibri", 20, "bold"), text_color="#333333")
        self.lb_title.grid(row=0, column=0, padx=20, pady=5)

        #Criar os nossos widgets da tela de cadastro
        self.username_cadastro_entry = ctk.CTkEntry(self.frame_for_cadastro, width=300, placeholder_text="Usuario".upper(), font=("calibri", 16), corner_radius=15, border_color="#A6A6A6")
        self.username_cadastro_entry.grid(row=1, column=0, padx=20, pady=5)

        self.email_cadastro_entry = ctk.CTkEntry(self.frame_for_cadastro, width=300, placeholder_text= "Seu Email".upper(), font=("calibri", 16), corner_radius=15, border_color="#A6A6A6")
        self.email_cadastro_entry.grid(row=2, column=0, padx=20, pady=5)

        self.senha_cadastro_entry = ctk.CTkEntry(self.frame_for_cadastro, width=300, placeholder_text="Digite sua senha".upper(), font=("calibri", 16), corner_radius=15, border_color="#A6A6A6", show="*")
        self.senha_cadastro_entry.grid(row=3, column=0, padx=20, pady=5)

        self.confirma_senha_entry = ctk.CTkEntry(self.frame_for_cadastro, width=300, placeholder_text="Confirme a senha".upper(), font=("calibri", 16), corner_radius=15, border_color="#A6A6A6", show="*")
        self.confirma_senha_entry.grid(row=4, column=0, padx=20, pady=5)

        self.ver_senha_cadastro = ctk.CTkCheckBox(self.frame_for_cadastro, width=300, text="CLIQUE PARA VER A SENHA",font=("calibri".upper(), 14), corner_radius=5, fg_color="#4E9343", hover_color="#4E9343", border_color="#A6A6A6", command=self.ShowPassCadastro, onvalue=0, offvalue=1)
        self.ver_senha_cadastro.grid(row=5, column=0, pady=20, padx=20)

        self.button_finalizar_cadastro = ctk.CTkButton(self.frame_for_cadastro, width=300, text="FAZER CADASTRO".upper(), font=("calibri", 18, "bold"), corner_radius=15, command=self.cadastrar_usuario, fg_color="#4E9343", hover_color="#2E7D32", text_color="#FFFFFF")
        self.button_finalizar_cadastro.grid(row=6, column=0, pady=5, padx=20)

        self.button_fazer_login_cadastro = ctk.CTkButton(self.frame_for_cadastro, width=200, text="Voltar a Login".upper(),font=("calibri", 18, "bold"), corner_radius=15, command=self.tela_login, hover_color="#FFD54F", text_color="#FFFFFF", fg_color="#F4B74F")
        self.button_fazer_login_cadastro.grid(row=7, column=0, pady=10)

    #MOSTRAR SENHA CADASTRO
    def ShowPassCadastro(self):
        ShowPass = self.ver_senha_cadastro.get()

        if ShowPass:
            self.senha_cadastro_entry.configure(show="*")
            self.confirma_senha_entry.configure(show="*")
        else:
            self.senha_cadastro_entry.configure(show="")
            self.confirma_senha_entry.configure(show="")



    def limpa_entry_cadastro(self):
        self.username_cadastro_entry.delete(0, END)
        self.senha_cadastro_entry.delete(0, END)
        self.email_cadastro_entry.delete(0, END)
        self.confirma_senha_entry.delete(0, END)

    def limpa_entry_login(self):
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

if __name__ == "__main__":
    app = App()
    app.mainloop()
