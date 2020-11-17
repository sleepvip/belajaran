#BALAJAR WIKIPEDIA


import wikipedia as wiki
cari = input("Apa Yang Anda Cari : ")
wiki.set_lang('id')
print(wiki.summary(cari,sentences=5))