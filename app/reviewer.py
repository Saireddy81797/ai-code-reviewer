import ast
from app.complexity import check_complexity
from app.security_checks import run_security_checks


def analyze_code(code: str):
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return {"error": f"Syntax error: {e}"}

    complexity_result = check_complexity(tree)
    security_result = run_security_checks(tree)

    return {
        "complexity": complexity_result,
        "security": security_result,
    }
