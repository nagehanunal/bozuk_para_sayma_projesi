import cember_tespiti as c

if c.cemberler is None:
    para_sayisi=0
else:
    para_sayisi=len(c.cemberler[0])    
#çok katmanlı sonuç döndüğünden 0 kullanıyoruzki en dış katmandan direkt ulaşalım

print(f"görseldeki bozuk para sayısı: {para_sayisi} ")