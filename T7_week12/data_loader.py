# Nama  : Samsul Rizal
# NIM   : F1D02310025
# Kelas : [Isi Kelas Anda]

import pandas as pd
import os

class DataLoader:
    def __init__(self, file_name='supermarket_sales.csv'):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(current_dir, file_name)
        
        try:
            self.df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"Error: File {self.file_path} tidak ditemukan!")
            self.df = pd.DataFrame()

    def get_branches(self):
        if 'Branch' in self.df.columns:
            return ['Semua Cabang'] + sorted(self.df['Branch'].unique().tolist())
        return ['Semua Cabang']
        
    def get_products(self):
        if 'Product line' in self.df.columns:
            return ['Semua Produk'] + sorted(self.df['Product line'].unique().tolist())
        return ['Semua Produk']

    def get_filtered_data(self, branch='Semua Cabang', product='Semua Produk'):
        df_filtered = self.df.copy()
        if not df_filtered.empty:
            if branch != 'Semua Cabang':
                df_filtered = df_filtered[df_filtered['Branch'] == branch]
            if product != 'Semua Produk':
                df_filtered = df_filtered[df_filtered['Product line'] == product]
        return df_filtered
        
    def get_summary_stats(self, df_filtered):
        """Menghitung data untuk 3 Kartu Ringkasan di atas"""
        if df_filtered.empty:
            return "$ 0.00", "0", "0.0"
            
        total_sales = df_filtered['Sales'].sum() if 'Sales' in df_filtered.columns else 0
        total_trx = len(df_filtered)
        avg_rating = df_filtered['Rating'].mean() if 'Rating' in df_filtered.columns else 0
        
        return f"$ {total_sales:,.2f}", str(total_trx), f"{avg_rating:.1f}"