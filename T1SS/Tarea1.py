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

    bytes = text.encode()
    init_vector = (0).to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CBC(init_vector), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(bytes) + encryptor.finalize()

    # Entregar últimos 16 bytes
    return ct[-16:]


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


text = "texto de pruebastexto de pruebas"
key = os.urandom(32)
a = CbcMac(text, key)
print(a)
print(invCbcMac(a, key))
