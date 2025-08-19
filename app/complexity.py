import radon.complexity as cc

def check_complexity(code: str):
    """
    Analyze cyclomatic complexity of given code.
    """
    try:
        results = []
        blocks = cc.cc_visit(code)
        for block in blocks:
            results.append({
                "name": block.name,
                "complexity": block.complexity,
                "rank": cc.cc_rank(block.complexity)
            })
        return results
    except Exception as e:
        return [{"error": str(e)}]
