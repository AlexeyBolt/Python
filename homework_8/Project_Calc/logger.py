# Модуль для записи резуьтатов вычислений

def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open('history.csv', 'a') as h:
        h.write(f'\n{expr};{result}')


def get_history() -> str:
    """Возвращает содержимое файла с результатами вычислений"""
    with open('history.csv', 'r') as h:
        return h.read()