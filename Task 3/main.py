import sys
from pathlib import Path
from colorama import init, Fore, Back, Style

# colorama для кольорового виведення
init()

# Вивести всі аргументи командного рядка
print(f"Аргументи командного рядка: {sys.argv}")

def get_directory_path():
    if len(sys.argv) == 2:  # очікується один аргумент (шлях до каталогу)
        return sys.argv[1]  
    else:
        # Якщо аргумент не передано, використовується каталог сценарію
        script_dir = Path(__file__).parent
        print(f"{Fore.YELLOW}Аргумент не прийнято. Використовується поточний каталог: {script_dir}{Style.RESET_ALL}")
        return str(script_dir) 

# Перевірка, чи каталог/файл приховано
def is_hidden(path):
    return path.name.startswith('.')  

dir_path = get_directory_path()
dir_path_obj = Path(dir_path)

if not dir_path_obj.exists():
    print(f"{Fore.RED + Back.YELLOW}Помилка: Шлях '{dir_path}' не існує{Style.RESET_ALL}")
    sys.exit(1)

if not dir_path_obj.is_dir():
    print(f"{Fore.RED + Back.YELLOW}Помилка: '{dir_path}' не є директорією{Style.RESET_ALL}")
    sys.exit(1)

# Рекурсивне проходження каталогу та відображення його структури
def print_dir_structure(current_path, prefix="", show_hidden=False):
    items = sorted(current_path.iterdir(), key=lambda x: x.name.lower())
    for i, item in enumerate(items):
        if is_hidden(item) and not show_hidden:
            continue
        line = "└── " if i == len(items) - 1 else "├── "
        if item.is_dir():
            print(f"{prefix}{line}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
            print_dir_structure(item, prefix + "    ", show_hidden)
        else:
            print(f"{prefix}{line}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

# Відображення імені кореневого каталогу
print(f"{Fore.YELLOW + Back.CYAN}{dir_path_obj.name}{Style.RESET_ALL}")

show_hidden_files = input(f"{Fore.YELLOW}Показати приховані файли/папки? (y/n): {Style.RESET_ALL}")
show_hidden = show_hidden_files.lower() == "y"

# Структура каталогу
print_dir_structure(dir_path_obj, show_hidden=show_hidden)