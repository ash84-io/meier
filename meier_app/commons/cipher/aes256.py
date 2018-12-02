# -*- coding: utf-8 -*-


class AES256:
    """
    AES256 암호화/복호화 클래스
    BLOCK_SIZE = 16
    """

    BLOCK_SIZE = 16

    def pkcs5_pad(self, s):
        """
        pkcs5 padding function

        :param s: padding 대상
        :return: padding 결과
        """
        bs = self.BLOCK_SIZE

        return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

    def pkcs5_unpad(self, s):
        """
        pkcs5 padding function

        :param s: unpadding 대상
        :return: unpadding 결과
        """

        return s[0:-ord(s[-1])]

    def encrypt(self, key, value, iv):
        """
        AES256 암호화

        :param key: 키
        :param value: 값
        :param iv: IV(Initial vector)
        :return: AES256 암호화된 문자열
        """
        from Crypto.Cipher import AES
        cipher = AES.new(key, AES.MODE_CBC, iv)
        crypted = cipher.encrypt(self.pkcs5_pad(value))
        return crypted

    def decrypt(self, key, value, iv):
        """
        AES256 복호화

        :param key: 키
        :param value: 값
        :param iv: IV(Initial vector)
        :return: AES256 복호화된 문자열
        """
        from Crypto.Cipher import AES
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return self.pkcs5_unpad(cipher.decrypt(value))

    def encrypt_b64(self, key, value, iv):
        """
        AES256 암호화후, Base64 인코딩

        :param key: 키
        :param value: 값
        :param iv: IV(Initial vector)
        :return: AES256 암호화후 Base64 인코딩 된 문자열
        """
        import base64
        return base64.b64encode(self.encrypt(key, value, iv))

    def decrypt_b64(self, key, value, iv):
        """
        Base64후 AES256 복호화

        :param key: 키
        :param value: 값
        :param iv: IV(Initial vector)
        :return:  Base64후 AES256 복호화된 문자열
        """
        import base64
        b64_decoded = base64.standard_b64decode(value)
        return self.decrypt(key, b64_decoded, iv)
