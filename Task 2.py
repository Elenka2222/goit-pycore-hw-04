def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                
                if line:
                    cat_id, name, age = line.split(',')
                    
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    
                    cats_list.append(cat_info)
                    
        return cats_list
    
    except FileNotFoundError:
        print(f"Помилка: Файл {path} не знайдено")
        return []
    
    except ValueError:
        print("Помилка: Некоректний формат даних у файлі")
        return []
    
    except Exception as e:
        print(f"Виникла помилка: {str(e)}")
        return []

if __name__ == "__main__":
    file_path = "goit-pycore-hw-04\\cats_file.txt"
    
    cats_info = get_cats_info(file_path)
    
    for cat in cats_info:
        print(cat)