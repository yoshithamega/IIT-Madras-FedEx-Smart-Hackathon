def recommend_action(overdue_days, amount, past_behavior):
    if overdue_days <= 15 and past_behavior == "Good":
        return "Email Reminder", "72 hours"
    elif overdue_days <= 30:
        return "Phone Call Follow-up", "48 hours"
    else:
        return "Settlement / Escalation", "24 hours"

