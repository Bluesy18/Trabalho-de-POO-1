from customtkinter import *
from tkinter import messagebox

# FUNCÕES DE VERIFICAÇÃO
# ----------------------
def verificaNome(nome):
    nome = nome.split()
    for n in nome:
        if not n.isalpha():
            return False
    if len(nome) > 1:
        return True
    return False

def verificaEmail(email):
    email = email.split('@')
    if len(email) == 2:
        if email[1] == "gmail.com":
            return True
    return False

def verificaTelefone(telefone):
    if telefone.isdigit() and len(telefone) == 9:
        return True
    return False

def verificaCPF(cpf):
    if len(cpf) == 11 and cpf.isdigit():
        return True
    return False

#    INTERFACE GRÁFICAwidth
# ----------------------
set_appearance_mode("light")
set_default_color_theme("dark-blue")

# login
#------
class TelaLogin(CTk):
    def __init__(self):
        super().__init__()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        width = 350
        height = 350
        print(screen_width)
        print(screen_height)

        self.title("Login")
        self.geometry(f"{width}x{height}+{screen_width//2-width//2}+{screen_height//2-height//2}")
        self.resizable(False, False)

        # frame
        frame = CTkFrame(master=self, width=200, height=300, fg_color="transparent")
        frame.place(relx=0.5, rely=0.5, anchor="center")


        # login
        login = CTkLabel(master=frame, text="Bem-vindo!", font=("Roboto", 30))
        login.place(relx=0.5, y=70, anchor="center")

        usuario_entry = CTkEntry(master=frame, width=200, border_width=1, placeholder_text="Nome de usuario")
        usuario_entry.place(x=0, y=120)

        senha_entry = CTkEntry(master=frame, width=200, border_width=1, placeholder_text="Senha", show="*")
        senha_entry.place(x=0, y=160)

        sem_conta_entry = CTkButton(master=frame, text="Não possuo uma conta", bg_color="transparent", fg_color="transparent", 
                                    hover="disabled", text_color="gray", 
                                    command=lambda: self.mudar_tela())
        sem_conta_entry.place(relx=0.5, y=190, anchor="n")
    
    def mudar_tela(self):
        self.destroy()
        TelaRegistro()



# registro
#---------
class TelaRegistro(CTk):
    def __init__(self):
        super().__init__()
        self.title("Registro de Cliente")
        self.geometry("350x350+1000+500")
        self.resizable(False, False)

        # frame
        frame = CTkFrame(master=self, width=200, height=300, fg_color="transparent")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # registro
        registro = CTkLabel(master=frame, text="Registrar", font=("Roboto", 30))
        registro.place(relx=0.5, y=20, anchor="center")

        email_entry = CTkEntry(master=frame, width=200, border_width=1, placeholder_text="Email")
        email_entry.place(x=0, y=120)

        usuario_entry = CTkEntry(master=frame, width=200, border_width=1, placeholder_text="Nome de usuario")
        usuario_entry.place(x=0, y=120)

        senha_entry = CTkEntry(master=frame, width=200, border_width=1, placeholder_text="Senha", show="*")
        senha_entry.place(x=0, y=160)

        registrar = CTkButton(master=frame, text="Criar conta", bg_color="transparent", fg_color="transparent", 
                                    hover="disabled", text_color="gray", 
                                    command=lambda: self.mudar_tela())
        registrar.place(relx=0.5, y=190, anchor="n")

    def mudar_tela(self):
        self.destroy()
        TelaLogin()

app = TelaLogin()
app.mainloop()