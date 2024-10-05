import os
import time


# Конфигурация
CHUNK_READ_SIZE = 10  # Количество строк для чтения за раз
BUFFER_WRITE_SIZE = 21  # Буфер, при заполнении которого происходит запись в файл
READ_FILE = 'big_data_input.txt'  # Входной файл
WRITE_FILE = 'big_data_output.txt'  # Выходной файл
DELAY = 3  # Задержка в секундах для визуализации


def process_chunk(chunk):
    """
    Пример обработки данных перед записью.
    Можно добавить логику для фильтрации, изменения данных и т.д.
    """
    return [line.strip().upper() for line in chunk]  # Пример: приведение всех строк к верхнему регистру


def read_in_chunks(file_path, chunk_size):
    """
    Считывает файл чанками указанного размера.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        chunk = []
        for line in file:
            chunk.append(line)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk


def write_buffer_to_file(buffer, file_path):
    """
    Записывает содержимое буфера в файл и очищает буфер.
    """
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write('\n'.join(buffer) + '\n')
    print(f"Записано {len(buffer)} строк в файл.")


def estimate_line_count(file_path, sample_size=1024):
    """
    Оценивает количество строк в файле на основе небольшого сэмпла.
    Т.Е. оцениваем среднюю длину строки и на основе этого делаем предположение
    о количестве строк в файле.

    Работает лучше для файлов, в которых строки имеют примерно одинаковую длину

    Если строки отличаются по длине, но не радикально (например, от 80 до 120 символов),
    метод всё равно даст довольно точную оценку, хотя и с некоторой погрешностью

    """
    total_size = os.path.getsize(file_path)  # Размер файла в байтах
    with open(file_path, 'r', encoding='utf-8') as file:
        sample = file.read(sample_size)  # Читаем первые sample_size байтов
        average_line_length = len(sample) / sample.count('\n') if sample.count('\n') > 0 else len(sample)

    # Оцениваем количество строк
    estimated_lines = total_size // average_line_length
    return int(estimated_lines)


def main():

    # Оценка количества строк НЕПРАВИЛЬНО (ДОЛГО)
    start_time = time.perf_counter() # Засекаем время
    with open(READ_FILE, 'r', encoding='utf-8') as file:
        total_lines = sum(1 for _ in file)
    print(f"\n\nВсего строк в файле: {total_lines}")
    print(f"Подсчитано 1 способом за: {time.perf_counter() - start_time} секунд.\n")

    # Оценка количества строк ПРАВИЛЬНО (БЫСТРО)
    start_time = time.perf_counter() # Засекаем время
    estimated_lines = estimate_line_count(READ_FILE)
    print(f"Примерно строк в файле: {estimated_lines}")
    print(f"Подсчитано 2 способом за: {time.perf_counter() - start_time} секунд.\n")
    time.sleep(DELAY)  # Задержка для визуализации записи в файл

    print(f"Будем читать по {CHUNK_READ_SIZE} строк за раз.")
    print(f"Запись с буфера в файл каждые {BUFFER_WRITE_SIZE} строк.\n")

    buffer = []  # Буфер для временного хранения данных

    # Чтение данных из файла чанками
    for chunk in read_in_chunks(READ_FILE, CHUNK_READ_SIZE):
        print(f"Прочитано {len(chunk)} строк:")
        for line in chunk:
            print(f"Буфер: {len(buffer)} / {BUFFER_WRITE_SIZE} - {line.strip()}")
            buffer.append(line.strip())  # Добавляем строку в буфер

            # Если буфер достиг заданного размера, записываем его в файл
            if len(buffer) >= BUFFER_WRITE_SIZE:
                print(f"Буфер достиг {BUFFER_WRITE_SIZE} строк. Записываем в файл...")
                write_buffer_to_file(buffer, WRITE_FILE)
                buffer.clear()  # Очищаем буфер после записи

        time.sleep(DELAY)  # Задержка для визуализации записи в файл

    # Если остались данные в буфере после завершения чтения, записываем их в файл
    if buffer:
        print(f"Записываем оставшиеся {len(buffer)} строк из буфера в файл...")
        write_buffer_to_file(buffer, WRITE_FILE)

    print("Чтение и запись завершены.")


if __name__ == "__main__":
    main()
