from abc import ABC, abstractmethod
from PIL import Image


# Базовый класс фабрики конвертеров
class ConverterFactory(ABC):
    @abstractmethod
    def create_converter(self):
        pass


# Конкретная реализация фабрики для конвертирования изображений в формат JPG
class JPGConverterFactory(ConverterFactory):
    def create_converter(self):
        return JPGConverter()


# Конкретная реализация фабрики для конвертирования изображений в формат JPEG
class JPEGConverterFactory(ConverterFactory):
    def create_converter(self):
        return JPEGConverter()


# Конкретная реализация фабрики для конвертирования изображений в формат PNG
class PNGConverterFactory(ConverterFactory):
    def create_converter(self):
        return PNGConverter()


# Конкретная реализация фабрики для конвертирования изображений в формат BMP
class BMPConverterFactory(ConverterFactory):
    def create_converter(self):
        return BMPConverter()


# Конкретная реализация фабрики для конвертирования изображений в формат ICO
class ICOConverterFactory(ConverterFactory):
    def create_converter(self):
        return ICOConverter()


# Конкретная реализация фабрики для конвертирования изображений в формат TIFF
class TIFFConverterFactory(ConverterFactory):
    def create_converter(self):
        return TIFFConverter()


# Конкретная реализация фабрики для конвертирования изображений в формат WebP
class WebPConverterFactory(ConverterFactory):
    def create_converter(self):
        return WebPConverter()


# Базовый класс конвертера изображений
class ImageConverter(ABC):
    @abstractmethod
    def convert(self, image_path, output_path):
        pass


# Конкретный класс конвертера для формата JPG
class JPGConverter(ImageConverter):
    def convert(self, image_path, output_path):
        img = Image.open(image_path)
        img.save(output_path + "jpg", "JPEG")

# Конкретный класс конвертера для формата JPEG
class JPEGConverter(ImageConverter):
    def convert(self, image_path, output_path):
        try:
            img = Image.open(image_path)
            img.save(output_path + ".jpeg", "JPEG")
        except Exception as e:
            raise RuntimeError(f"Ошибка при конвертации изображения {image_path}: {str(e)}")


# Конкретный класс конвертера для формата PNG
class PNGConverter(ImageConverter):
    def convert(self, image_path, output_path):
        try:
            img = Image.open(image_path)
            img.save(output_path + ".png", "PNG")
        except Exception as e:
            raise RuntimeError(f"Ошибка при конвертации изображения {image_path}: {str(e)}")


# Конкретный класс конвертера для формата BMP
class BMPConverter(ImageConverter):
    def convert(self, image_path, output_path):
        try:
            img = Image.open(image_path)
            img.save(output_path + ".bmp", "BMP")
        except Exception as e:
            raise RuntimeError(f"Ошибка при конвертации изображения {image_path}: {str(e)}")


# Конкретный класс конвертера для формата ICO
class ICOConverter(ImageConverter):
    def convert(self, image_path, output_path):
        try:
            img = Image.open(image_path)
            img.save(output_path + ".ico", "ICO")
        except Exception as e:
            raise RuntimeError(f"Ошибка при конвертации изображения {image_path}: {str(e)}")


# Конкретный класс конвертера для формата TIFF
class TIFFConverter(ImageConverter):
    def convert(self, image_path, output_path):
        try:
            img = Image.open(image_path)
            img.save(output_path + ".tiff", "TIFF")
        except Exception as e:
            raise RuntimeError(f"Ошибка при конвертации изображения {image_path}: {str(e)}")


# Конкретный класс конвертера для формата WebP
class WebPConverter(ImageConverter):
    def convert(self, image_path, output_path):
        try:
            img = Image.open(image_path)
            img.save(output_path + ".webp", "WebP")
        except Exception as e:
            raise RuntimeError(f"Ошибка при конвертации изображения {image_path}: {str(e)}")
