
import tkinter as tk
from PIL import Image, ImageTk

def splash_screen():
    root = tk.Tk()
    root.title("Sistema Bancário")
    root.geometry("1080x630")

    # Criar um canvas
    canvas = tk.Canvas(root, width=1280, height=720)
    canvas.pack()

    # Carregar a imagem
    image = Image.open(".\\splashScreem\\imagem\\bank2.jpg")
    photo = ImageTk.PhotoImage(image)

    # Exibir a imagem no canvas
    canvas.create_image(476, 226, anchor=tk.CENTER, image=photo)

    # Informações dos desenvolvedores
    desenvolvido_por = [
        "Bem-vindo ao Sistema Bancário",
        "Desenvolvido por:",
        "Carlos de Aquino Itaboray",
        "Fabrício Dias de Oliveira",
        "Maciel Costa do Nascimento",
    ]

    # Adicionar as informações como texto no canvas
    y_pos = 100
    for info in desenvolvido_por:
        canvas.create_text(30, y_pos, text=info, font=("Helvetica", 16, "bold"), fill="white", anchor=tk.W)
        y_pos += 10
        y_pos += 10  # Adicionando um espaçamento de 10 pixels entre cada linha

    # Informações do menu principal
    menu_principal = [
        "1 - Abrir Nova Conta",
        "2 - Consultar Saldo",
        "3 - Realizar Depósito",
        "4 - Realizar Saque",
        "5 - Transferência PIX",
        "6 - Transferência TED",
        "7 - Transferência DOC",
        "8 - Mostrar Clientes",
        "9 - Limpar Todas as Contas",
        "0 - Sair do Programa",
    ]

    # Adicionar as informações como texto no canvas
    y_pos = 250
    for info in menu_principal:
        canvas.create_text(30, y_pos, text=info, font=("Helvetica", 14, "bold"), fill="white", anchor=tk.W)
        y_pos += 20
        y_pos += 20  # Adicionando um espaçamento de 10 pixels entre cada linha

    root.mainloop()

splash_screen()

