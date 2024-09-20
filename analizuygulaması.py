import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_data_from_db(query):
    try:
        conn = sqlite3.connect('satislar.db')
        df = pd.read_sql(query, conn)
    except Exception as e:
        print(f"Veritabanı hatası: {e}")
        return pd.DataFrame()
    finally:
        conn.close()
    return df

def check_missing_data(df, columns):
    missing_data = df[columns].isnull().sum()
    if missing_data.any():
        print("Eksik veriler:")
        print(missing_data[missing_data > 0])
    else:
        print("Eksik veri bulunmuyor.")

def plot_sales_trend(ax):
    query = 'SELECT tarih, satis_miktari FROM satislar'
    df = fetch_data_from_db(query)
    check_missing_data(df, ['tarih', 'satis_miktari'])

    if df.empty:
        ax.text(0.5, 0.5, 'Veri boş. Grafik oluşturulamıyor.', ha='center', va='center', fontsize=12)
        return

    df['tarih'] = pd.to_datetime(df['tarih'], errors='coerce')
    df = df.dropna(subset=['tarih'])
    
    zaman_serisi = df.groupby('tarih')['satis_miktari'].sum()
    
    sns.lineplot(x=zaman_serisi.index, y=zaman_serisi.values, marker='o', color='b', ax=ax)
    ax.set_title('Zaman Serisi Satış Analizi')
    ax.set_xlabel('Tarih')
    ax.set_ylabel('Toplam Satış Miktarı')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)

def plot_top_selling_brand(ax):
    query = 'SELECT marka, SUM(satis_miktari) as toplam_satis FROM satislar GROUP BY marka'
    df = fetch_data_from_db(query)
    check_missing_data(df, ['marka', 'toplam_satis'])
    
    if df.empty:
        ax.text(0.5, 0.5, 'Veri boş. Grafik oluşturulamıyor.', ha='center', va='center', fontsize=12)
        return

    sns.barplot(x='marka', y='toplam_satis', data=df, palette='viridis', ax=ax)
    ax.set_title('En Çok Satan Marka Analizi')
    ax.set_xlabel('Marka')
    ax.set_ylabel('Toplam Satış Miktarı')
    ax.tick_params(axis='x', rotation=45)

def plot_gender_distribution(ax):
    query = 'SELECT cinsiyet, SUM(satis_miktari) as toplam_satis FROM satislar GROUP BY cinsiyet'
    df = fetch_data_from_db(query)
    check_missing_data(df, ['cinsiyet', 'toplam_satis'])
    
    if df.empty:
        ax.text(0.5, 0.5, 'Veri boş. Grafik oluşturulamıyor.', ha='center', va='center', fontsize=12)
        return

    ax.pie(df['toplam_satis'], labels=df['cinsiyet'], autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue'])
    ax.set_title('Kadın ve Erkek Oranları Analizi')

def plot_age_group_analysis(ax):
    query = 'SELECT yas, SUM(satis_miktari) as toplam_satis FROM satislar GROUP BY yas'
    df = fetch_data_from_db(query)
    check_missing_data(df, ['yas', 'toplam_satis'])
    
    if df.empty:
        ax.text(0.5, 0.5, 'Veri boş. Grafik oluşturulamıyor.', ha='center', va='center', fontsize=12)
        return

    bins = [18, 25, 35, 45, 55, 65]
    labels = ['18-24', '25-34', '35-44', '45-54', '55-64']
    df['yas_grubu'] = pd.cut(df['yas'], bins=bins, labels=labels, right=False)

    age_group_df = df.groupby('yas_grubu')['toplam_satis'].sum()

    sns.barplot(x=age_group_df.index, y=age_group_df.values, palette='muted', ax=ax)
    ax.set_title('Yaş Grupları Analizi')
    ax.set_xlabel('Yaş Grubu')
    ax.set_ylabel('Toplam Satış Miktarı')

def plot_monthly_sales_analysis(ax):
    query = '''
    SELECT strftime('%Y-%m', tarih) AS ay, SUM(satis_miktari) AS toplam_satis
    FROM satislar
    GROUP BY ay
    ORDER BY ay
    '''
    df = fetch_data_from_db(query)
    check_missing_data(df, ['ay', 'toplam_satis'])
    
    if df.empty:
        ax.text(0.5, 0.5, 'Veri boş. Grafik oluşturulamıyor.', ha='center', va='center', fontsize=12)
        return

    sns.lineplot(x='ay', y='toplam_satis', data=df, marker='o', color='orange', ax=ax)
    ax.set_title('Aylık Satış Analizi')
    ax.set_xlabel('Ay')
    ax.set_ylabel('Toplam Satış Miktarı')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)

def main():
    fig, axs = plt.subplots(3, 2, figsize=(18, 18))

    plot_sales_trend(axs[0, 0])
    plot_top_selling_brand(axs[0, 1])
    plot_gender_distribution(axs[1, 0])
    plot_age_group_analysis(axs[1, 1])
    plot_monthly_sales_analysis(axs[2, 0])

    # Hide the empty subplot
    axs[2, 1].axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
