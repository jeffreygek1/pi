import imaplib

M = imaplib.IMAP4_SSL("imap.gmail.com")
M.login("hogeschoolutrechtmail@gmail.com", "raspberry")
M.select()
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print (data)
M.close()
M.logout()