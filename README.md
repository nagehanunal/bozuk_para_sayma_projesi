# bozuk_para_sayma_projesi
Python ve OpenCV kütüphanesi kullanılarak geliştirdiğim yüklenen görseldeki bozuk paraları otomatik olarak tespit eden ve sayısını hesaplayan modüler bir görüntü işleme projesidir.

Proje okunabilirliği ve sürdürülebilirliği artırmak amacıyla modüler dosya yapısı kullanılmıştır:
bozuk_para_sayma_projesi/
├── goruntu_ayarlari.py     # Görüntü ön işleme (Gri tonlama ve Median Blur ile gürültü giderme)
├── cember_tespiti.py       # Hough Transform algoritması ile dairesel geometrilerin tespiti
├── sayiyi_bulma.py         # Ana program merkezi (Modülleri birleştirir ve sonucu ekrana yazar)
└── bozukparalar.jpg        # İşlenecek örnek girdi görseli
