import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Func_Consultar_Banco import *

class MyDestiny:
    def __init__(self, master):
        try:
            '''
            --------------------------------------------------------------------------------------------------------------------------
                                        Estabelecendo as PROPRIEDADES DA INTERFACE de agendamento
            --------------------------------------------------------------------------------------------------------------------------
            '''
            self.master = master
            self.master.geometry('500x520')
            self.master.title('N_Trip_Project_V1.0')
            self.master.columnconfigure(0, weight=1)
            self.master.columnconfigure(1, weight=6)
            self.frame = tk.Frame(self.master)
            self.master.resizable(0, 0)
            self.master.attributes('-toolwindow', False)
            self.master['bg'] = '#222222'

            '''
            Opções para a escolha das viagens:

            >>> Tipo de viagem, estilo de comida, clima, melhor preço, etc...
            '''

            '''
            --------------------------------------------------------------------------------------------------------------------------
                                                        Estabelecendo o HEADING do programa
            --------------------------------------------------------------------------------------------------------------------------
            '''
            # Heading, Labels and Entry
            self.heading_lb = tk.Label(self.master, text='Procure sua viagem', font=('Heveltica', 20), bg='#114470', fg='white')
            self.heading_lb.grid(ipadx=200, columnspan=2, row=0, column=0)

            '''
            --------------------------------------------------------------------------------------------------------------------------
                                                    Estabelecendo o TIPO DE TURISMO procurado pelo usuário
                                                    *Variáveis
                                                    *Listas
                                                    *Widget
            --------------------------------------------------------------------------------------------------------------------------
            '''
            # self.meu_tipo = tk.Label(self.master, text='Tipo de Viagem:', bg='#222222', fg='white', font=('Heveltica Bold', 14))
            # self.meu_tipo.grid(column=0, row=1, padx=20, sticky=tk.W, pady=10)

            # # Variable for the type of the trip
            # self.all_types = ['Turismo Cultural', 'Ecoturismo', 'Intercâmbio', 'Turismo de Saúde',
            #                 'Turismo de Esportes', 'Turismo de Sol e Praia', 'Turismo Rural']

            # self.type_of_trip = tk.StringVar()
            # self.option_for_trip = ttk.Combobox(self.master, textvariable=self.type_of_trip, values=self.all_types)
            # self.option_for_trip['state'] = 'readonly'
            # self.option_for_trip.current(0)
            # self.option_for_trip.grid(column=1, row=1, sticky=tk.NS, padx=25, pady=10, ipadx=50)

            '''
            --------------------------------------------------------------------------------------------------------------------------
                                                    Estabelecendo o ESTADO do usuário
            --------------------------------------------------------------------------------------------------------------------------
            '''
            self.cod_label = tk.Label(self.master, text='Código', font=('Heveltica', 14), bg='#222222', fg='white')
            self.cod_label.grid(column=0, row=1, padx=20, sticky=tk.W, pady=10)
            self.cod_var = tk.StringVar()
            self.cod_entry = tk.Entry(self.master, textvariable=self.cod_var)
            self.cod_entry.grid(column=1, row=1, sticky=tk.NS, padx=10, pady=10, ipadx=60)


            self.cidade_label = tk.Label(self.master, text='Cidade', font=('Heveltica', 14), bg='#222222', fg='white')
            self.cidade_label.grid(column=0, row=2, padx=20, sticky=tk.W, pady=10)
            self.cidade_var = tk.StringVar()
            self.cidade_entry = tk.Entry(self.master, textvariable=self.cidade_var)
            self.cidade_entry.grid(column=1, row=2, sticky=tk.NS, padx=10, pady=10, ipadx=60)

            # Estado
            self.estado = tk.Label(self.master, text='Estado:', bg='#222222', fg='white', font=('Heveltica Bold', 14))
            self.estado.grid(column=0, row=3, padx=20, sticky=tk.W, pady=10)

            # All the states
            self.lista_estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PR',
                                  'PB', 'PA', 'PE', 'PI', 'RN', 'RS', 'RJ', 'RO', 'RR', 'SC', 'SE', 'SP', 'TO']
            # Variable
            self.estado_var = tk.StringVar()
            self.estado_option = ttk.Combobox(self.master, textvariable=self.estado_var, values=self.lista_estados)
            self.estado_option['state'] = 'readonly'
            self.estado_option.current(0)
            self.estado_option.grid(column=1, row=3, sticky=tk.NS, padx=10, pady=10, ipadx=50)
        
            '''
            --------------------------------------------------------------------------------------------------------------------------
                                                     Estabelecendo a CIDADE de ida para viajar
            --------------------------------------------------------------------------------------------------------------------------
            '''
            self.classe_label = tk.Label(self.master, text='Classe:', bg='#222222', fg='white', font=('Heveltica Bold', 14))
            self.classe_label.grid(column=0, row=4, padx=20, sticky=tk.W, pady=10)

            self.classe_var = tk.StringVar()
            self.lista_classes = ['Econômica', 'Premium Economy', 'Executiva/Business', 'Primeira Classe']
            self.cidade_option = ttk.Combobox(self.master, textvariable=self.classe_var, values=self.lista_classes)
            self.cidade_option['state'] = 'readonly'
            self.cidade_option.current(0)
            self.cidade_option.grid(column=1, row=4, sticky=tk.NS, padx=10, pady=10, ipadx=50)

            '''
            --------------------------------------------------------------------------------------------------------------------------
                                                    Estabelecendo o DESTINO escolhido pelo usuário
            --------------------------------------------------------------------------------------------------------------------------
            '''

            # DESTiNO
            self.destino = tk.Label(self.master, text='Destino:', bg='#222222', fg='white', font=('Heveltica Bold', 14))
            self.destino.grid(column=0, row=5, padx=20, sticky=tk.W, pady=10)
            self.destino_var = tk.StringVar()
            # Lista dos destinos
            self.lista_destinos = ['1| Paris, França', '2| Dubai', '3| Berlim, Alemanha',
             '4| Londres, Inglaterra', '5| Roatán', '6| Belize']
            self.destino_option = ttk.Combobox(self.master, textvariable=self.destino_var, values=self.lista_destinos)
            self.destino_option['state'] = 'readonly'
            self.destino_option.current(0)
            self.destino_option.grid(column=1, row=5, sticky=tk.NS, padx=10, pady=10, ipadx=50)
            '''
            --------------------------------------------------------------------------------------------------------------------------
                                                    Estabelecendo a QUANTIDADE DE HÓSPEDES
            --------------------------------------------------------------------------------------------------------------------------
            '''

        # Total de Pessoas para a viagem
            self.pessoas = tk.Label(self.master, text='Total de Pessoas:', bg='#222222', fg='white', font=('Heveltica Bold', 14))
            self.pessoas.grid(column=0, row=6, padx=20, sticky=tk.W, pady=10)
            self.total_pessoas = tk.StringVar(value=0)
            self.pessoas_spinbox = ttk.Spinbox(self.master,from_=1, to=8, wrap=True, textvariable=self.total_pessoas, width=4)
            self.pessoas_spinbox.grid(column=1, row=6, sticky=tk.NS, padx=45, pady=10, ipadx=15)

            '''
            --------------------------------------------------------------------------------------------------------------------------
                Estabelecendo a QUANTIDADE DE DIAS que o indivíduo ficará hospedado
            --------------------------------------------------------------------------------------------------------------------------
            '''
            self.ida_label = tk.Label(self.master, text='Ida:', bg='#222222', fg='white', font=('Heveltica Bold', 14))
            self.ida_label.grid(column=0, row=7, padx=20, sticky=tk.W, pady=10)
            self.ida_var = tk.StringVar()
            self.ida_entry = tk.Entry(self.master, textvar=self.ida_var)
            self.ida_entry.grid(column=1, row=7, sticky=tk.NS, padx=45, pady=10, ipadx=60)

            self.volta_label = tk.Label(self.master, text='Volta:', bg='#222222', fg='white', font=('Heveltica Bold', 14))
            self.volta_label.grid(column=0, row=8, padx=20, sticky=tk.W, pady=10)
            self.volta_var = tk.StringVar()
            self.volta_entry = tk.Entry(self.master, textvar=self.volta_var)
            self.volta_entry.grid(column=1, row=8, sticky=tk.NS, padx=45, pady=10, ipadx=60)
            
            
            '''
            --------------------------------------------------------------------------------------------------------------------------
                Estabelecendo as variáveis e o widgets para o VALOR MIN e VALOR MAX
                1° - Valor mínimo p/viagem;
                2° - Valor máximo p/viagem;
            --------------------------------------------------------------------------------------------------------------------------
            '''

            self.valor_label = tk.Label(self.master, text='Valor(R$):', bg='#222222', fg='white', font=('Heveltica Bold', 14))
            self.valor_label.grid(column=0, row=9, sticky=tk.W, padx=20)
            self.valor_var = tk.Variable()
            self.valor_scale = tk.Scale(self.master, from_=0, to='10000', orient='horizontal', bg='#114470', fg='white', variable=self.valor_var)
            #self.maximo = ttk.Scale(self.master, from_=0, to='10000', orient='horizontal', variable=self.max_value)
            self.valor_scale.grid(column=1, row=9, sticky=tk.NS, pady=10, padx=12, ipadx=10)

            '''
            --------------------------------------------------------------------------------------------------------------------------
                Botão para CONCLUIR o agendamento e SALVAR no banco de dados
            --------------------------------------------------------------------------------------------------------------------------
            '''
            self.concluir_button = tk.Button(self.master,
                                            text='Concluir',
                                            font=('Heveltica Bold', 15),
                                            bg='green',
                                            fg='white',
                                            command=self.inserir_banco)
            
            self.concluir_button.grid(column=1, row=10, sticky=tk.E, padx=10, pady=20)

            '''
            --------------------------------------------------------------------------------------------------------------------------
                Botão para CANCELAR o agendamento
            --------------------------------------------------------------------------------------------------------------------------
            '''
            self.cancel_button= tk.Button(self.master,
                                        text='Fechar',
                                        bg='red',
                                        fg='white',
                                        font=('Heveltica Bold', 15),
                                        command=self.master.destroy)

            self.cancel_button.grid(column=0, row=10, padx=20, sticky=tk.W)

            '''
            --------------------------------------------------------------------------------------------------------------------------
                Botão para RESETAR OS VALORES NOS CAMPOS caso o usuário queira apagar tudo
            --------------------------------------------------------------------------------------------------------------------------
            '''
            self.Resetar_button = tk.Button(self.master,
                                            text='Resetar',
                                            font=('Heveltica Bold', 15),
                                            bg='#114488',
                                            fg='white',
                                            command=self.reset_fields)

            self.Resetar_button.grid(columnspan=2, row=10, sticky=tk.N, padx=18, pady=20)

        except Exception as error:
            print(error)

    def reset_fields(self):
        '''
            --------------------------------------------------------------------------------------------------------------------------
                Função para RESETAR os valores nos campos
            --------------------------------------------------------------------------------------------------------------------------
         '''
        self.cidade_var.set('')
        self.estado_var.set('')
        self.classe_var.set('')
        self.destino_var.set('')
        self.total_pessoas.set('')
        self.ida_var.set('')
        self.volta_var.set(0)
        self.valor_var.set(0)
    
        '''
            Função para CRIAR e INSERIR os dados
        '''

    def inserir_banco(self):
        import mysql.connector
        con = mysql.connector.connect(host='localhost', database='usuarios', user='root', password='matheus.rodrigues.araujo.083')
        cursor = con.cursor()
        try:
            cursor.execute('''update informacoes.viagem set viagem=? where id=?''', (self.cod_var.get(), 1))
            con.commit()
            con.close()
        except Exception as deu_erro:
            print(deu_erro)
        finally:
            showinfo(title='Status da Viagem', message='Sua viagem foi marcada com sucesso!')

            
if __name__ == '__main__':
    '''
        * Controle de escopo de execução;
        * Executará somente arquivo, já que é o principal;
        * Se for importado não executará;
    '''

    root = tk.Tk()
    frame = MyDestiny(root)
    root.mainloop()
