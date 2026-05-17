# Nama  : Samsul Rizal
# NIM   : F1D02310025
# Kelas : [Isi Kelas Anda]

import matplotlib
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class DashboardCharts(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=8, height=3, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.patch.set_facecolor('#ffffff') 
        
        self.ax1 = self.fig.add_subplot(121)
        self.ax2 = self.fig.add_subplot(122)
        super().__init__(self.fig)
        
    def update_charts(self, df):
        self.ax1.clear()
        self.ax2.clear()
        
        if df.empty:
            self.draw()
            return

        # 1. Bar Chart: Penjualan per Kategori
        if 'Product line' in df.columns and 'Sales' in df.columns:
            sales = df.groupby('Product line')['Sales'].sum().sort_values()
            
            # Warna biru keunguan (Indigo) yang elegan
            sales.plot(kind='barh', ax=self.ax1, color='#5f27cd', edgecolor='none')
            
            self.ax1.set_title("Total Penjualan per Kategori", pad=15, fontweight='bold', color='#222f3e')
            self.ax1.set_xlabel("Total Penjualan ($)", color='#576574')
            self.ax1.set_ylabel("")
            self.ax1.tick_params(axis='both', colors='#576574', labelsize=9)
            
            self.ax1.spines['top'].set_visible(False)
            self.ax1.spines['right'].set_visible(False)
            self.ax1.spines['left'].set_color('#c8d6e5')
            self.ax1.spines['bottom'].set_color('#c8d6e5')
        
        # 2. Pie Chart: Tipe Pelanggan (Berbeda dengan teman Anda)
        if 'Customer type' in df.columns:
            cust_counts = df['Customer type'].value_counts()
            
            # Palet warna mencolok: Cyan & Vibrant Orange
            modern_colors = ['#0abde3', '#ff9f43']
            
            self.ax2.pie(
                cust_counts, 
                labels=cust_counts.index, 
                autopct='%1.1f%%', 
                startangle=140,
                colors=modern_colors,
                textprops={'color': '#222f3e', 'fontsize': 10, 'fontweight': 'bold'},
                wedgeprops={'edgecolor': 'white', 'linewidth': 2} # Efek jarak antar potongan
            )
            self.ax2.set_title("Distribusi Tipe Pelanggan", pad=15, fontweight='bold', color='#222f3e')
            
        self.fig.tight_layout(pad=2.0)
        self.draw()
        
    def export_to_png(self, filename):
        self.fig.savefig(filename, bbox_inches='tight', dpi=300)