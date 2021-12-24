from tkinter.messagebox import showerror, showinfo
import tkinter as tk
from Destinos import MyDestiny

def nova_janela(_class):
        try:
            create_window = tk.Toplevel()
            create_window.grab_set()
            _class(create_window)
        except Exception as error:
            print(error)

def verificar_Final_Version(email, senha):
    import mysql.connector
    from mysql.connector import Error
    try:
        con = mysql.connector.connect(host='localhost', database='usuarios', user='root', password='matheus.rodrigues.araujo.083')

        cursor = con.cursor()
        cursor.execute('select * from informacoes')
        for n in cursor.fetchall():
            if email == n[4]:
                if senha == n[5]:
                    showinfo(title='Status', message='Bem-vindo(a)!')
                    nova_janela(MyDestiny)
                else:
                    showerror(title='Status', message='Email ou senha podem estar errados ou não existem')
                break
    except Error as e:
        print(e)
    finally:
        con.close()
        cursor.close()
