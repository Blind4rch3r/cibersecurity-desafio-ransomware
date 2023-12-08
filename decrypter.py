import os
import pyaes
import click
import encrypter


def file_decrypter(crypt_data, key):
    ## palavra-chave para teste "testeransomwares"
    ## chave para descriptografia
    if len(key) < 16:
    	os._exit(-2)
    	
    if crypt_data == "":
    	os._exit(-1)
    	
    aes = pyaes.AESModeOfOperationCTR(bytes(key, "utf-8"))
    ## descriptografar o arquivo
    decrypt_data = aes.decrypt(crypt_data)
    return decrypt_data


def file_writer(file_name, decrypt_data):
    ## salvar o arquivo descriptografado
    new_file, extend = os.path.splitext(file_name)
    with open(f"{new_file}",'wb') as f:
        f.write(decrypt_data)


@click.command()
@click.option("--file", "-f", prompt="File to Decrypt", help="Path of File to Decrypt")
@click.option("--key", "-k", prompt="Key to Decrypt File", help="Necessary key to decrypt the target file")
def main(file, key):
    crypt_data = encrypter.file_opener(file)
    data = file_decrypter(crypt_data, key)
    file_writer(file, data)

if __name__ == '__main__':
    main()
