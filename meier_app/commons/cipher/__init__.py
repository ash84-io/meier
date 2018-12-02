# -*- coding:utf-8 -*-
from .aes256 import AES256


def hash_sha256(raw):
    import hashlib
    hash_object = hashlib.sha256(raw)
    return hash_object.hexdigest()


def enc_aes256(raw):
    """
    AES256 암호화, conf 저장된 키 이용
    :param raw: 암호화 대상 문자열
    :return: 암호화 된 값
    """
    from flask import current_app
    return enc_aes256_b64(key=current_app.config['AES256_KEY'],
                          raw=raw,
                          iv=current_app.config['AES256_IV'])


def dec_aes256(enc):
    """
    AES256 복호화, conf 저장된 키 이용
    :param enc: 복호화 대상 문자열
    :return: 복호화 된 값
    """
    from flask import current_app
    return dec_aes256_b64(key=current_app.config['AES256_KEY'],
                          enc=enc,
                          iv=current_app.config['AES256_IV'])


def enc_aes256_b64(raw, key, iv):
    """
    AES256 암호화 BASE64, CBC, PKCS5

    :param raw: 암호화 대상 문자열
    :param key: 암호화 키
    :param iv: 암호화 initial vector
    :return: 암호화된 문자열
    """
    aes256 = AES256()
    enc = aes256.encrypt_b64(value=raw,
                             key=key,
                             iv=iv)
    return enc


def dec_aes256_b64(enc, key, iv):
    """
    AES256 복호화 BASE64, CBC, PKCS5

    :param enc: 복호화 대상 문자열
    :param key: 암호화 키
    :param iv: 암호화 initial vector
    :return: 복호화된 문자열
    """
    aes256 = AES256()
    dec = aes256.decrypt_b64(value=enc,
                             key=key,
                             iv=iv)
    return dec
