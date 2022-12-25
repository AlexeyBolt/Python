# Модуль для выполнения операций
import sympy 

def execute_expr(expr: str) -> str:         # (5+3)*10 -> 80
    """Принимает на вход строку-пример.
    Возвращает результат примера."""
    
    return str(eval(expr))

def solve_eq(expr: str) -> str:                    # x**3 - 8 = 0 -> "2"
                                                    # x**2 - 1  -> "1,-1"
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    
    try:
        x = sympy.Symbol('x')
        res = sympy.solve(expr, x)
        res = list(map(str, res))
        return " || ".join(res)
    except ValueError:
        return 'Incorrect input'

def simpify_pol(expr: str) -> str:           # x**2 + 3*x**2 + 4 -> 4*x**2 + 4
    """Упрощает введенный многочлен"""
    
    return str(sympy.simplify(expr))