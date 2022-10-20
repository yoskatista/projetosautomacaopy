

import pyautogui
print('_'*106)
print("\n IMPORTANTE\n Para não dar erro, pedimos para que entre no ERP novo 192.168.0.182/relatorios e deixe a tela maximizada.\n\n Logo ABRA a tela de Expedição> Atendimento de pedido.")
print('_'*106)
confirmacao = str(input("Já se encontram abertos Expedição> Atendimento de pedido?? \n(digite 's' para sim ou 'n' para não)"))

if confirmacao == 's':
    confirmacao = True
else:
    print("Encerrado")
    confirmacao = False


while confirmacao == True:
    pedido = str (input("Qual o número do pedido?"))
    lote = str (input("Qual o seu lote a ser bipado?"))
    quantia = int (input("Qual a quantidade do Lote? (Somente números)"))

    pyautogui.click(616, 351)