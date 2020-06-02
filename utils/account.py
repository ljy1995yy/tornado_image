from bcrypt import hashpw, gensalt

#加密
# bool值判断：True为加密，False为解密
def pas_encryption(pwd,passwd=None,b=True):
    if b:
        # 加密过程
        # 随机生成盐
        salt = gensalt(12)

        # 通过盐加密
        passwd = hashpw(pwd.encode('utf8'),salt)
        return passwd
    else:
        # 解密过程
        return hashpw(pwd.encode('utf8'), passwd.encode('utf8'))