import M2Crypto.EVP

cipher = M2Crypto.EVP.Cipher('rc4', ''.join([chr(x) for x in range(0, 16)]),
                             '', 1, key_as_bytes=0, d='md5', salt=None, i=1,
                             padding=1)
print cipher.update('\0\1\2\3\4\5').encode('hex')