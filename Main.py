import tkinter as tk
from Destinos import MyDestiny
from Cadastro import Register
from Verificacao_Dados import verificar_Final_Version

class MainFrame:
    def __init__(self, master):
        try:
            # Definindo os métodos da Root Window
            self.master = master
            self.master.geometry('280x280')
            self.master.title('Main_Trip_Project_V1.0')
            self.master.columnconfigure(0, weight=1)
            self.master.columnconfigure(1, weight=3)
            self.master.resizable(0, 0)
            self.master.attributes('-toolwindow', True)
            self.frame = tk.Frame(self.master)
            self.master['bg'] = '#222222'

            # Definindo variáveis, funções, listas e ect...
            # Cadastro
            # VARIÁVEIS
            self.email = tk.StringVar()
            self.senha = tk.StringVar()
            
            # Heading
            self.heading_lb = tk.Label(self.master, text='Trip Project V1.0', font=('Heveltica', 20), bg='#114488', fg='white')
            self.heading_lb.grid(ipadx=200, columnspan=2, row=0, ipady=8)

            # Email 
            self.email_lb = tk.Label(self.master, text='EMAIL', bg='#222222', fg='white', font=('Heveltica Bold', 14))
            self.email_lb.grid(column=0, row=1, sticky=tk.W, padx=15)
            self.email_entry = tk.Entry(self.master, width=40, textvariable=self.email)
            self.email_entry.focus()
            self.email_entry.grid(column=0, row=2, padx=18, sticky=tk.W)

            # SENHA E VERIFICAÇÃO
            self.senha_lb = tk.Label(self.master, text='Senha', bg='#222222', fg='white', font=('Heveltica Bold', 14))
            self.senha_lb.grid(column=0, row=3, sticky=tk.W, padx=15)
            self.senha_entry = tk.Entry(self.master, width=40, show='*', textvariable=self.senha)
            self.senha_entry.grid(column=0, row=4, padx=18, sticky=tk.W)

            # Buttons
            self.login_button = tk.Button(self.master,
                                        text='Login',
                                        bg='#114488',
                                        activebackground='#339911',
                                        activeforeground='white',
                                        fg='white',
                                        font=('Heveltica Bold', 12),
                                        command=lambda:verificar_Final_Version(self.email.get(), self.senha.get()))
            self.login_button.grid(column=0, row=5, padx=17, pady=10, sticky=tk.E)


            self.nova_senha_button = tk.Button(self.master,
                                               text='Esqueceu a senha?',
                                               bg='#114488',
                                               fg='white',
                                               font=('Heveltica Bold', 12))
            
            self.nova_senha_button.grid(column=0, row=5, padx=18, pady=10, sticky=tk.W)

            self.reg_button = tk.Button(self.master,
                                        text='Cadastrar',
                                        bg='#114488',
                                        fg='white',
                                        font=('Heveltica Bold', 12),
                                        command=lambda:self.new_window(Register))
            
            self.reg_button.grid(column=0, row=6, padx=18, pady=10, sticky=tk.E)

            self.cancel_button= tk.Button(self.master,
                                        text='Fechar',
                                        bg='red',
                                        fg='white',
                                        font=('Heveltica Bold', 13),
                                        command=self.master.destroy)

            self.cancel_button.grid(column=0, row=6, padx=18, sticky=tk.W)

        except Exception as error:
            print(error)

    def new_window(self, _class):
        try:
            self.create_window = tk.Toplevel()
            self.create_window.grab_set()
            _class(self.create_window)
        except Exception as error:
            print(error)


if __name__ == '__main__':
    root = tk.Tk()
    frame = MainFrame(root)
    root.mainloop()
