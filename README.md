Correct and fast RC4 stream cipher for JavaScript

benchmark (see test.html):

    Chrome 37:   185.98884066955983MB/s
    Safari 7:    55.0357732526142MB/s
    Firefox 32:  234.55824863174354MB/s

usage:

    var key = new Uint8Array(16);
    var plainText1 = new Uint8Array(10);
    var plainText2 = new Uint8Array(17);

    var cipherText1 = new Uint8Array(10);
    var cipherText2 = new Uint8Array(17);

    var cipher = new RC4(key);
    cipher.update(cipherText1, plainText1, 10);
    cipher.update(cipherText2, plainText2, 17);
    // ...

