import pyautogui
import time
import keyboard

def fill_form(data):
    time.sleep(3) 
    for campo, valor in data.items():
        print(f"Preenchendo {campo}...")
        pyautogui.write(valor, interval=0.1)
        pyautogui.press('tab')
    pyautogui.press('enter')
    print("Formulário preenchido com sucesso!")

if __name__ == "__main__":
    dados_formulario = {
        "Nome": "Ryan Mendes Braga",
        "Email": "ryan2018atual@email.com",
        "Telefone": "(92) 99408-1399",
        "Endereço": "Rua Tapucara, 19",
    }
    
    print("Posicione o cursor no primeiro campo do formulário e pressione 'F2'")
    keyboard.wait('F2')
    fill_form(dados_formulario)