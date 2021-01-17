
"""
Napisz program, który w wybranej lokalizacji odczyta wszystkie pliki graficzne (w określonych formatach, np. 
jpg, png, bmp itp.), następnie zmniejszy ich rozdzielczość o 50% i zapisze je w podkatalogu “smaller” z 
odpowiednimi nazwami. Wykorzystaj pillow lub inną bibliotekę do pracy z obrazami. 
Propozycja rozszerzenia: Oblicz ile miejsca na dysku można oszczędzić po kompresji (odczytaj rozmiar plików w 
pierwotnym folderze oraz "smaller" i porównaj obie wartości - bezwzględnie i w %)

"""

from PIL import Image
import os


paths = 'C:\Python Scripts\Projects\images'
small = 'C:\Python Scripts\Projects'
extension = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')

small_path = os.path.join(small, 'smaller')
os.makedirs(small_path, exist_ok=True)


def image_resize(paths):
    for filename in os.listdir(paths):
        if os.path.splitext(filename)[1] in extension:
            file_path = os.path.join(paths, filename)
        try:
            with Image.open(file_path) as img:
                 width, height = img.size
                 img.thumbnail((int(width * 0.5), int(height * 0.5)))
                 filename = filename.partition('.')[0] + '_sm.' + filename.partition('.')[2]
                 new_path = os.path.join(small_path, filename)
                 img.save(new_path, 'JPEG')
        except OSError:
            pass
        

def check_size(path):
    count = 0
    for file in os.listdir(path):
        if file.endswith(extension):
            count += os.path.getsize(f'{path}/{file}')
    return count


image_resize(paths)    
before_size = check_size(paths)
after_size = check_size(small_path)
ratio = (after_size/before_size) * 100

print(f'Size before is {before_size/1048576:.2f} Mb and size after compression is {after_size/1048576:.2f} Mb, ratio is {ratio:.2} %')



    