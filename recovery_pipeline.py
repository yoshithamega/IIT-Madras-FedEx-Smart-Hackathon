from model.decision_model import recommend_action

def run_pipeline(case):
    action, sla = recommend_action(
        case["overdue_days"],
        case["amount"],
        case["past_behavior"]
    )

    return {
        "action": action,
        "sla": sla,
        "dca": "DCA A",
        "trust_score": 85
    }

