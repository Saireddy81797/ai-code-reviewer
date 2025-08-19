import ast
from app.complexity import check_complexity
from app.security_checks import run_security_checks

def analyze_code(code: str):
    results = {
        "complexity": None,
        "security_issues": [],
        "ai_suggestions": []
    }

    try:
        # Run AST parsing
        tree = ast.parse(code)
        results["complexity"] = check_complexity(code)

        # Run security checks
        security_findings = run_security_checks(code)
        results["security_issues"].extend(security_findings)

    except Exception as e:
        results["ai_suggestions"].append(f"Parsing error: {str(e)}")

    return results
