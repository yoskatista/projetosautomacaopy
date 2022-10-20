import pyautogui


#inputs
pedido = str(input("Qual o número do pedido? "))
lote = str(input("Qual o número do lote? "))
quantia = int(input("Qual a quantia do lote? "))

pyautogui.PAUSE = 5
pyautogui.hotkey('alt','tab', interval=0.3)

#pedido

pyautogui.click(616, 351)
pyautogui.write((pedido), interval=0.3)
pyautogui.press('enter')

#lote

pyautogui.click(810, 1051)
pyautogui.write((lote), interval=0.1)
pyautogui.press('enter')

