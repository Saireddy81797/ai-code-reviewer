import ast
from app.complexity import check_complexity
from app.security_checks import run_security_checks

def analyze_code(code: str):
    """
    Run AST parsing, complexity check, and security checks.
    Returns dict with issues + suggestions.
    """
    results = {
        "security_issues": run_security_checks(code),
        "complexity": check_complexity(code),
        "ai_suggestions": []
    }

    # Placeholder AI suggestions (can connect to OpenAI API later)
    try:
        tree = ast.parse(code)
        if len(tree.body) > 5:
            results["ai_suggestions"].append("Consider splitting code into smaller functions.")
        if "print(" in code:
            results["ai_suggestions"].append("Avoid print statements, use logging instead.")
    except Exception as e:
        results["ai_suggestions"].append(f"Parsing error: {str(e)}")

    return results
