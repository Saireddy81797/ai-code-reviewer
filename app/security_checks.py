import re

def run_security_checks(code: str):
    issues = []

    # Example: Detect hardcoded API keys
    if re.search(r'["\'](AKIA|AIza|sk-)[A-Za-z0-9]{10,}["\']', code):
        issues.append("⚠️ Hardcoded secret/API key detected.")

    # Example: Dangerous eval usage
    if "eval(" in code:
        issues.append("⚠️ Use of eval() is unsafe, consider alternatives.")

    # Example: OS command injection
    if "os.system(" in code:
        issues.append("⚠️ os.system() can lead to command injection.")

    return issues
