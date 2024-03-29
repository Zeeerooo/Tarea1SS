import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def CbcMac(text: str, key: bytes) -> bytes:
    '''
    Calculador de MAC a traves del modelo CBC, usando cifrador de bloque AES.
    Hasta ahora funciona sólo con textos de tamaño múltiplo 16 bytes.
    :param text: Texto a encriptar
    :param key: Clave a utilizar en AES
    :return: mac del texto
    '''

    #bytes = text.encode()
    init_vector = (0).to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CBC(init_vector), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(text) + encryptor.finalize()

    # Entregar últimos 16 bytes
    return ct[-16:]


def AesEcrypt(text: str, key: bytes):
    '''
    Encriptador de texto con AES en modo CBC
    :param text: texto a encriptar, multiplo de 16 bytes
    :param key: clave de aes, 16 bytes
    :return: encriptación del texto
    '''

    #bytes = text.encode()
    init_vector = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(init_vector), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(text) + encryptor.finalize()
    return init_vector, ct


def invCbcMac(cif: bytes, key: bytes) -> str:
    '''
    Sólo funciona en casos en los cuales el texto encriptado es de 16 bytes. Sino, dado que el mac es de 16 bytes,
    no es posible obtener el texto completo.

    :param cif: texto cifrado
    :param key: Clave usada en AES
    :return: Texto desencriptado
    '''
    init_vector = (0).to_bytes(16, byteorder='big')
    decryptor = Cipher(algorithms.AES(key), modes.CBC(init_vector), backend=default_backend()).decryptor()
    return decryptor.update(cif) + decryptor.finalize()

# text = "texto de pruebas"
# key = os.urandom(16)
# a = CbcMac(text, key)
# print(a)
# print(invCbcMac(a, key))
