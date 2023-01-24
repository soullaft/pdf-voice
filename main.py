from PyPDF2 import PdfReader
from pathlib import Path
from gtts import gTTS


def get_content_pdf(filePath):
    pathToFile = Path(filePath)
    if not pathToFile.is_file() or not pathToFile.suffix == '.pdf':
        raise Exception(
            '[!] Некорректный путь до файла \n или файл имеет некорректный тип')

    reader = PdfReader(pathToFile)
    text = ''
    for page in reader.pages:
        text += page.extract_text()

    return text


def convert_text_to_audio(text, language):
    return gTTS(text=text, lang=language, slow=False)


def main():
    filePath = input('[~]Укажите полный путь до .pdf файла:')
    language = input(
        '[~]Укажите язык в формате en, rus, es и т.д. на который следует озвучить:')
    try:
        pdfText = get_content_pdf(filePath)
    except Exception:
        print(
            '[!]Что-то пошло не так, удостоверьтесь, что файл имеет корректный тип и он' +
            f'\n существует по пути {filePath}')
    print('[+] Этап преобразования из текста в mp3...')
    audioConverted = convert_text_to_audio(text=pdfText, language=language)
    file_name = Path(filePath).stem
    audioConverted.save(f'{file_name}.mp3')
    print(f'[+] Файл успешно был озвучен и сохранён по пути {file_name}.mp3')


if __name__ == '__main__':
    main()
