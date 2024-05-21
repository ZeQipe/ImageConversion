from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from core.image_converter import (JPEGConverterFactory, PNGConverterFactory, BMPConverterFactory, ICOConverterFactory,
                                TIFFConverterFactory, WebPConverterFactory, JPGConverterFactory)


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Инициализируем и конфигурируем UI пользователя
        """
        super().__init__()
        self.setWindowTitle("Image Converter")

        # Устанавливаем фиксированный размер окна
        self.setFixedSize(500, 300)

        # Создаем главный layout
        main_layout = QHBoxLayout()

        # Левый вертикальный layout для кнопки выбора изображения и кнопки сброса
        left_layout = QVBoxLayout()
        left_layout.addStretch()
        self.select_button = QPushButton("Выбрать изображение")
        self.select_button.setFixedSize(200, 50)
        self.select_button.clicked.connect(self.select_image)
        left_layout.addWidget(self.select_button, alignment=Qt.AlignCenter)

        # Добавляем кнопку "Сбросить"
        self.reset_button = QPushButton("Сбросить")
        self.reset_button.setFixedSize(200, 25)
        self.reset_button.clicked.connect(self.reset_selection)
        left_layout.addWidget(self.reset_button, alignment=Qt.AlignCenter)

        left_layout.addStretch()

        # Правый вертикальный layout для кнопок конвертирования
        right_layout = QVBoxLayout()
        right_layout.addStretch()
        self.convert_buttons = {
            "PNG": QPushButton("Конвертировать в PNG"),
            "JPEG": QPushButton("Конвертировать в JPEG"),
            "JPG": QPushButton("Конвертировать в JPG"),
            "BMP": QPushButton("Конвертировать в BMP"),
            "ICO": QPushButton("Конвертировать в ICO"),
            "TIFF": QPushButton("Конвертировать в TIFF"),
            "WebP": QPushButton("Конвертировать в WebP")
        }

        for button in self.convert_buttons.values():
            button.setEnabled(False)
            button.setFixedSize(200, 25)
            button.clicked.connect(self.convert_image)
            right_layout.addWidget(button, alignment=Qt.AlignCenter)
        right_layout.addStretch()

        # Добавляем левый и правый layout в главный layout
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Переменные для хранения информации о выбранном файле и формате конвертации
        self.selected_file = None
        self.output_format = None

    # Метод для выбора изображения
    def select_image(self) -> None:
        """
        Вызывается при выборе изображений для конвертирования. Позволяет выбрать несколько файлов, но преобразован будет
        только один.
        Активирует кнопки, которые отличаются от формата выбранного изображения.
        """
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp *.jpeg *.webp)")
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            file_formats = [file_path.split('.')[-1].upper() for file_path in file_paths]
            majority_format = max(set(file_formats), key=file_formats.count) if file_formats else None
            for fmt, button in self.convert_buttons.items():
                if fmt != majority_format:
                    button.setEnabled(True)
                else:
                    button.setEnabled(False)
            self.selected_file = file_paths[0] if file_paths else None

    # Метод для сброса выбранного файла и отключения всех кнопок конвертирования
    def reset_selection(self) -> None:
        """
        Кнопка сброса программы в начальное состояние.
        """
        self.selected_file = None
        for button in self.convert_buttons.values():
            button.setEnabled(False)

    # Метод для конвертации изображения
    def convert_image(self) -> None:
        """
        Выбираем путь для сохранения.
        Запрашивает конвертер у абстрактных фабрик. При этом, мы ничего не знаем о конечном продукте.
        Просим конвертер сохранить файл в другом формате по указанному адресу.
        В случае ошибки - выдаем окошко с ошибкой. В случае проблемы с фабрикой - так же выдаем соответсвующее окошко.
        """
        sender = self.sender()
        if sender:
            self.output_format = sender.text().split()[-1].upper()
            file_dialog = QFileDialog()
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_dialog.setFileMode(QFileDialog.FileMode.Directory)
            if file_dialog.exec_():
                output_directory = file_dialog.selectedFiles()[0]
                factory = None
                if self.output_format == "JPEG":
                    factory = JPEGConverterFactory()
                elif self.output_format == "JPG":
                    factory = JPGConverterFactory()
                elif self.output_format == "PNG":
                    factory = PNGConverterFactory()
                elif self.output_format == "BMP":
                    factory = BMPConverterFactory()
                elif self.output_format == "ICO":
                    factory = ICOConverterFactory()
                elif self.output_format == "TIFF":
                    factory = TIFFConverterFactory()
                elif self.output_format == "WEBP":
                    factory = WebPConverterFactory()

                if factory:
                    converter = factory.create_converter()
                    try:
                        converter.convert(self.selected_file, output_directory)
                        QMessageBox.information(self, "Успех", f"Изображение успешно сконвертировано в {self.output_format}")
                    except Exception as e:
                        QMessageBox.critical(self, "Ошибка", f"Ошибка при конвертации изображения: {str(e)}")
                else:
                    QMessageBox.warning(self, "Предупреждение", f"Не удалось найти фабрику для формата {self.output_format}")
