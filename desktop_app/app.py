import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt6.QtGui import QPixmap, QImage, QColor
from PyQt6.QtCore import Qt


class PhotoProcessingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Interfejs użytkownika
        self.setWindowTitle('Photo Processing App')
        self.setGeometry(100, 100, 600, 400)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setScaledContents(True)

        self.load_button = QPushButton('Wybierz zdjęcie', self)
        self.load_button.clicked.connect(self.load_image)

        self.process_button = QPushButton('Przetwórz zdjęcie', self)
        self.process_button.clicked.connect(self.process_image)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.load_button)
        layout.addWidget(self.process_button)

        self.setLayout(layout)

    def load_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.FileDialogOption.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, 'Wybierz zdjęcie', '',
                                                   'Images (*.png *.jpg *.bmp *.gif);;All Files (*)', options=options)

        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap)

    def process_image(self):
        # Przykładowe przetwarzanie obrazu (zmiana jasności)
        if hasattr(self, 'image_label') and self.image_label.pixmap():
            original_pixmap = self.image_label.pixmap()
            original_image = original_pixmap.toImage()

            # Przetwarzanie obrazu
            processed_image = self.process_photo(original_image)

            # Wyświetlenie przetworzonego obrazu
            processed_pixmap = QPixmap.fromImage(processed_image)
            self.image_label.setPixmap(processed_pixmap)

    def process_photo(self, image):
        # Tutaj dodaj kod przetwarzania obrazu
        # Przykład: zmiana jasności
        for x in range(image.width()):
            for y in range(image.height()):
                color = QColor(image.pixel(x, y))
                brightness = color.lightness()
                color.setHsl(color.hslHue(), color.hslSaturation(), brightness + 20)
                image.setPixelColor(x, y, color)

        return image


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PhotoProcessingApp()
    window.show()
    sys.exit(app.exec())
