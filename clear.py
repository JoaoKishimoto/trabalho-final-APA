import os

def clear_cmd():
    # 'nt' indica o sistema operacional Windows
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)