# Satış Analizi ve Tahmin Modeli

Bu proje, SQLite veritabanındaki satış verilerini analiz etmek ve gelecekteki satışları tahmin etmek amacıyla iki bölümden oluşmaktadır. İlk bölümde satış verilerini çeşitli grafiklerle analiz ederken, ikinci bölümde fiyat ve kampanya bilgilerine dayalı olarak satış tahminleri yapılmaktadır.

## İçindekiler
- [Satış Analizi Dashboard'u](#satış-analizi-dashboardu)
- [Satış Tahmini Modeli](#satış-tahmini-modeli)

## Satış Analizi Dashboard'u

Bu bölüm, veritabanındaki satış verilerini görselleştiren bir Python uygulamasıdır. Aşağıdaki analizler yapılmaktadır:

- Zaman Serisi Satış Analizi
- En Çok Satan Marka Analizi
- Kadın ve Erkek Oranları Analizi
- Yaş Grupları Analizi
- Aylık Satış Analizi
![Figure_1](https://github.com/user-attachments/assets/23884817-84b2-406e-a28c-0f3f13af1ab2)
> **Not**: Grafikler, `Matplotlib` ve `Seaborn` kullanılarak oluşturulmuştur.

## Satış Tahmini Modeli

Bu bölümde, fiyat ve kampanya bilgilerini kullanarak satışları tahmin eden bir Lineer Regresyon modeli geliştirilmiştir. Model, eğitim verisiyle eğitildikten sonra test verisi üzerinde performansı değerlendirilir.

### Örnek Tahmin Sonuçları
Gerçek ve tahmin edilen satış miktarları bir scatter plot ile görselleştirilmiştir.
![Figure_1](https://github.com/user-attachments/assets/eb55230f-dcb9-4fb1-92d6-dbb5e8755953)
