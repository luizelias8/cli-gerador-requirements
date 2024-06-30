import argparse
import subprocess
import os
import sys

__version__ = '1.0.0'

def instalar_pipreqs():
    """
    Verifica se o pipreqs está instalado e o instala se necessário.
    """
    try:
        # Tenta verificar a versão do pipreqs para ver se está instalado
        subprocess.run(['pipreqs', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print('pipreqs já está instalado.')
    except subprocess.CalledProcessError:
        print('pipreqs não está instalado. Instalando...')
        # Instala o pipreqs usando pip
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'pipreqs'], check=True)
        print('pipreqs instalado com sucesso.')

def gerar_requirements_txt(diretorio):
    """
    Gera o arquivo requirements.txt no diretório especificado usando o pipreqs.
    """
    try:
        # Comando para gerar o requirements.txt usando pipreqs
        comando = ['pipreqs', '--force', diretorio]

        # Executa o comando
        subprocess.run(comando, check=True)

        print(f"Arquivo requirements.txt gerado com sucesso em: {diretorio}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar o requirements.txt: {e}")
    except FileNotFoundError:
        print("pipreqs não está instalado ou não foi encontrado no PATH. Tentando instalar pipreqs...")
        instalar_pipreqs()
        # Tenta gerar o requirements.txt novamente após a instalação
        try:
            subprocess.run(comando, check=True)
            print(f"Arquivo requirements.txt gerado com sucesso em: {diretorio}")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao gerar o requirements.txt após instalação do pipreqs: {e}")

def main():
    parser = argparse.ArgumentParser(description='Gerador de requirements.txt')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

    args = parser.parse_args()

    # Obtém o diretório atual
    diretorio_atual = os.getcwd()

    # Chama a função para gerar o requirements.txt no diretório atual
    gerar_requirements_txt(diretorio_atual)

if __name__ == '__main__':
    main()