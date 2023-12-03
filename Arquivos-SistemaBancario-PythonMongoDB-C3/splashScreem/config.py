MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Cadastro de Cliente Banco
2 - Relatório de Contas de Clientes
3 - Relatório de Transações PIX
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - BANCO
2 - CLIENTE
3 - CONTA
"""


def clear_console(wait_time:int=3):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")