ERR_MSG = "Operação inválida: divisão por zero."


def divide(a: float, b: float) -> float:
    if float(b) == float(0):
        raise ZeroDivisionError(ERR_MSG)
    return a / b
