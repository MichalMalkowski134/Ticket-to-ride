import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import ImageToBoard 
import RoadDefineScript
import numpy as np

class PhotoProcessingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Interfejs użytkownika
        self.setWindowTitle('Photo Processing App')
        self.setGeometry(100, 100, 800, 400)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setScaledContents(True)

        self.load_button = QPushButton('Wybierz zdjęcie', self)
        self.load_button.clicked.connect(self.load_image)

        self.process_button = QPushButton('Przetwórz zdjęcie', self)
        self.process_button.clicked.connect(self.process_image)

        # Panel boczny z nazwą koloru i ilością punktów
        self.side_panel = QVBoxLayout()

        # Dodaj dodatkowy QHBoxLayout do ułożenia kolorów poziomo
        colors_layout = QHBoxLayout()

        self.colors_labels = {}
        for color_name in ['Purple', 'Yellow', 'Red', 'Black', 'Green', 'Blue']:
            color_label = QLabel(f'Gracz {color_name}: 0', self)
            self.colors_labels[color_name] = color_label
            colors_layout.addWidget(color_label)

        # Dodaj colors_layout do side_panel
        self.side_panel.addLayout(colors_layout)

        # Główny layout z panelem bocznym
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.image_label)
        main_layout.addLayout(self.side_panel)

        control_layout = QVBoxLayout()
        control_layout.addWidget(self.load_button)
        control_layout.addWidget(self.process_button)
        main_layout.addLayout(control_layout)

        self.setLayout(main_layout)

        # Define image attribute
        self.image = None
        self.points = 0
        self.color_name = 'Brak'

    def load_image(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter('Images (*.png *.jpg *.bmp *.gif);;All Files (*)')

        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            file_name = file_dialog.selectedFiles()[0]

            if file_name:
                pixmap = QPixmap(file_name)
                scaled_pixmap = pixmap.scaledToHeight(400)
                self.image = scaled_pixmap.toImage()
                self.image_label.setPixmap(scaled_pixmap)

    def process_image(self):
        if self.image is not None:
            image_path = 'dataset/age_of_steam/board/original3.jpg'
            model_path = 'Roboflow_model/best.pt'
            model_grid_path = 'Roboflow_model/best_grid.pt'
            folder_path = 'runs/detect/predict'
            folder_path2 = 'runs/detect/predict2'

            image_to_board = ImageToBoard.ImageToBoard(image_path, model_path, model_grid_path, folder_path, folder_path2)
            tab , tabNp = image_to_board.run()

            processed_pixmap = QPixmap("board.png")
            self.image_label.setPixmap(processed_pixmap)

    def update_side_panel(self):
        color_name = self.get_color_name()
        self.color_label.setText(f'Kolor: {color_name}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PhotoProcessingApp()
    window.show()
    sys.exit(app.exec())
