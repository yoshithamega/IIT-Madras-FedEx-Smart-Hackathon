from model.decision_model import recommend_recovery_action

def process_overdue_case(case):
    """
    End-to-end recovery pipeline
    """

    action, sla = recommend_recovery_action(
        case["overdue_days"],
        case["amount"],
        case["past_behavior"]
    )

    assigned_dca = "DCA A (Trust Score: 85)"

    return {
        "recommended_action": action,
        "sla": sla,
        "assigned_dca": assigned_dca
    }
