# TODO Найдите количество книг, которое можно разместить на дискете
num_page_in_one_book = 100
num_string_per_page = 50
num_symbol_per_string = 25

volume_per_symbol = 4   #байт
available_volume = float(1.44)   #Мбайт

total_volume_per_book = num_page_in_one_book * num_string_per_page * num_symbol_per_string * volume_per_symbol
num_books = int(available_volume * 1024 * 1024 // total_volume_per_book)

print("Количество книг, помещающихся на дискету:", num_books)
