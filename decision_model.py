def recommend_recovery_action(overdue_days, amount, past_behavior):
    """
    Simple AI decision logic to recommend recovery action
    """

    if overdue_days < 15 and past_behavior == "Good":
        return "Send Email Reminder", "72 hours"

    elif overdue_days < 30:
        return "Phone Call Follow-up", "48 hours"

    else:
        return "Settlement Offer / Escalation", "24 hours"
