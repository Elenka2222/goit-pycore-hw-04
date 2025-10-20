def total_salary(path):
    try:
        line_number = 0
        with open(path, "r", encoding="utf-8") as file:
            salaries = []  
            for line in file:
                line_number += 1
                line = line.strip()  
                if line: 
                    parts = line.split(',')  
                    if len(parts) != 2:  
                        raise ValueError(f"Невірний формат рядка {line_number}: {line}")
                    name, salary_str = parts  
                try:
                    salary = float(salary_str)  
                    salaries.append(salary) 
                except ValueError:
                        raise ValueError(f"Невірний формат зарплати в рядку {line_number}: {salary_str}")
                 
            if not salaries:
                raise ValueError("Файл порожній або не містить валідних даних")
            
            total = sum(salaries)
            average = total / len(salaries)
            return total, average
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не знайдено: {path}")
    except ValueError as ve:
        raise ValueError(f"Помилка даних у файлі: {ve}")
    except Exception as e:
        raise RuntimeError(f"Непередбачена помилка: {e}")

try:
    total, average = total_salary("goit-pycore-hw-04\\salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except Exception as e:
    print(f"Помилка: {e}")