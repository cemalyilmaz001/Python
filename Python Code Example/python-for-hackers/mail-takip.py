import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com') # e-posta sağlayıcınıza bağlı olarak değiştirin
mail.login('daslşsadsa@yaani.com', 'password') # e-posta adresinizi ve şifrenizi girin
mail.select('inbox') # takip edilecek klasörü seçin, bu örnekte inbox (gelen kutusu) olarak ayarlanmıştır.

typ, data = mail.search(None, 'FROM', '"Kemal DADSA"') # John Doe'dan gelen tüm e-postaları arar 

for num in data[0].split():
    typ, msg_data = mail.fetch(num, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            print(msg['subject'])
            print(msg['from'])

mail.close()
mail.logout()
