# Nama  : Samsul Rizal
# NIM   : F1D02310025
# Kelas : [Isi Kelas Anda]

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QComboBox, QPushButton, QLabel,
    QMessageBox, QFileDialog, QSplitter, QFrame
)
from PySide6.QtCore import Qt
from data_loader import DataLoader
from chart_widget import DashboardCharts

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kaggle Supermarket Analytics Dashboard")
        self.resize(1200, 800)
        
        self.data_loader = DataLoader()
        self.setup_ui()
        self.muat_data()

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        header_layout = QHBoxLayout()
        
        lbl_judul = QLabel("📊 Supermarket Dashboard")
        lbl_judul.setStyleSheet("font-size: 24px; font-weight: bold; color: #222f3e;")
        
        self.combo_branch = QComboBox()
        self.combo_branch.addItems(self.data_loader.get_branches())
        self.combo_branch.currentTextChanged.connect(self.muat_data)
        
        self.combo_product = QComboBox()
        self.combo_product.addItems(self.data_loader.get_products())
        self.combo_product.currentTextChanged.connect(self.muat_data)
        
        self.btn_refresh = QPushButton("🔄 Refresh")
        self.btn_refresh.setObjectName("btnRefresh")
        self.btn_refresh.clicked.connect(self.muat_data)
        
        self.btn_export = QPushButton("💾 Export PNG")
        self.btn_export.setObjectName("btnExport")
        self.btn_export.clicked.connect(self.export_chart)
        
        header_layout.addWidget(lbl_judul)
        header_layout.addStretch()
        header_layout.addWidget(QLabel("<b>Branch:</b>"))
        header_layout.addWidget(self.combo_branch)
        header_layout.addWidget(QLabel("  <b>Product:</b>"))
        header_layout.addWidget(self.combo_product)
        header_layout.addWidget(self.btn_refresh)
        header_layout.addWidget(self.btn_export)
        
        main_layout.addLayout(header_layout)

        cards_layout = QHBoxLayout()
        
        self.card_sales = self.buat_kartu("Total Penjualan", "$ 0", "#10ac84") 
        self.card_trx = self.buat_kartu("Total Transaksi", "0", "#ff9f43")    
        self.card_rating = self.buat_kartu("Rata-rata Rating", "0.0", "#5f27cd") 
        
        cards_layout.addWidget(self.card_sales)
        cards_layout.addWidget(self.card_trx)
        cards_layout.addWidget(self.card_rating)
        main_layout.addLayout(cards_layout)

        splitter = QSplitter(Qt.Orientation.Vertical)
        
        # A. Grafik
        self.charts = DashboardCharts(self)
        splitter.addWidget(self.charts)
        
        # B. Tabel
        self.tabel = QTableWidget()
        self.tabel.setAlternatingRowColors(True)
        self.tabel.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabel.setShowGrid(False)
        splitter.addWidget(self.tabel)
        
        # Proporsi Splitter (Grafik lebih besar sedikit dari tabel)
        splitter.setSizes([400, 300])
        main_layout.addWidget(splitter)

    def buat_kartu(self, judul, nilai_awal, warna_aksen):
        """Helper untuk membuat kartu beraksen garis di sebelah kiri (Modern Left-Border)."""
        kartu = QFrame()
        kartu.setObjectName("summaryCard")
        kartu.setStyleSheet(f"""
            QFrame#summaryCard {{
                background-color: white;
                border-radius: 6px;
                border-left: 6px solid {warna_aksen};
                border-top: 1px solid #c8d6e5;
                border-right: 1px solid #c8d6e5;
                border-bottom: 1px solid #c8d6e5;
            }}
        """)
        layout = QVBoxLayout(kartu)
        
        lbl_judul = QLabel(judul)
        lbl_judul.setStyleSheet("color: #8395a7; font-size: 13px; font-weight: bold; border: none;")
        
        lbl_nilai = QLabel(nilai_awal)
        lbl_nilai.setStyleSheet("color: #222f3e; font-size: 22px; font-weight: bold; border: none;")
        
        kartu.lbl_nilai = lbl_nilai # Simpan referensi untuk diupdate
        layout.addWidget(lbl_judul)
        layout.addWidget(lbl_nilai)
        return kartu

    def muat_data(self):
        if self.data_loader.df.empty:
            QMessageBox.critical(self, "Error", "File CSV tidak ditemukan!")
            return

        cabang = self.combo_branch.currentText()
        produk = self.combo_product.currentText()
        
        # Ambil data yang difilter
        df_filtered = self.data_loader.get_filtered_data(cabang, produk)
        
        # 1. Update Kartu
        val_sales, val_trx, val_rating = self.data_loader.get_summary_stats(df_filtered)
        self.card_sales.lbl_nilai.setText(val_sales)
        self.card_trx.lbl_nilai.setText(val_trx)
        self.card_rating.lbl_nilai.setText(val_rating + " / 10")
        
        # 2. Update Tabel (Maksimal 150 baris agar cepat)
        limit = min(150, len(df_filtered))
        self.tabel.setRowCount(limit)
        self.tabel.setColumnCount(len(df_filtered.columns))
        self.tabel.setHorizontalHeaderLabels(df_filtered.columns)
        
        for i in range(limit):
            for j, col in enumerate(df_filtered.columns):
                self.tabel.setItem(i, j, QTableWidgetItem(str(df_filtered.iloc[i][col])))
                
        self.tabel.resizeColumnsToContents()
        
        # 3. Update Chart
        self.charts.update_charts(df_filtered)

    def export_chart(self):
        filepath, _ = QFileDialog.getSaveFileName(self, "Save Chart", "dashboard_chart.png", "PNG Image (*.png)")
        if filepath:
            self.charts.export_to_png(filepath)
            QMessageBox.information(self, "Sukses", f"Chart berhasil disimpan ke:\n{filepath}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Global QSS Styling
    app.setStyleSheet("""
        QMainWindow { background-color: #f1f2f6; }
        
        /* Tombol */
        QPushButton { padding: 6px 15px; border-radius: 4px; font-weight: bold; font-size: 13px; }
        QPushButton#btnRefresh { background-color: #2e86de; color: white; }
        QPushButton#btnRefresh:hover { background-color: #0984e3; }
        QPushButton#btnExport { background-color: #10ac84; color: white; }
        QPushButton#btnExport:hover { background-color: #1dd1a1; }
        
        /* Filter ComboBox */
        QComboBox { padding: 5px; border: 1px solid #c8d6e5; border-radius: 4px; background: white; min-width: 130px; }
        
        /* Tabel */
        QTableWidget { border: 1px solid #c8d6e5; border-radius: 6px; background-color: white; alternate-background-color: #f8f9fa; }
        QHeaderView::section { background-color: #dfe4ea; color: #2f3542; font-weight: bold; border: none; padding: 6px; }
    """)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())