def process_github_event(event: dict):
    """
    Process GitHub webhook event for PRs.
    (For now, just a stub. Later: fetch PR code & analyze.)
    """
    action = event.get("action", "unknown")
    pr_number = event.get("number", None)

    return {
        "message": "Webhook received",
        "action": action,
        "pull_request_number": pr_number
    }
