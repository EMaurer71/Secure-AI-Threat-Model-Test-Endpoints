"""
stride.py
Machine-readable STRIDE threat dictionary.
"""

stride_threats = {
    "api_endpoints": {
        "Spoofing": "Attacker spoofs clinician identity.",
        "Tampering": "X-ray images or metadata modified.",
        "Repudiation": "Clinician denies submitting X-ray.",
        "Information Disclosure": "API leaks patient data.",
        "Denial of Service": "Flooding inference API.",
        "Elevation of Privilege": "Misconfig allows admin access."
    },
    "training_pipeline": {
        "Spoofing": "Attacker impersonates trusted data source.",
        "Tampering": "Labels or images altered (data poisoning).",
        "Repudiation": "Data provider denies dataset.",
        "Information Disclosure": "Training data leaks PHI.",
        "Denial of Service": "ETL or training jobs disrupted.",
        "Elevation of Privilege": "Attacker gains training environment access."
    },
    "inference_engine": {
        "Spoofing": "Fake inference service returns bogus results.",
        "Tampering": "Model weights modified.",
        "Repudiation": "No traceability to model version.",
        "Information Disclosure": "Logs leak PHI.",
        "Denial of Service": "Heavy inputs overload engine.",
        "Elevation of Privilege": "Runtime exploit → host access."
    },
    "output_interface": {
        "Spoofing": "Phishing UI mimics dashboard.",
        "Tampering": "Reports altered before EHR.",
        "Repudiation": "Clinician denies viewing diagnosis.",
        "Information Disclosure": "UI exposes excessive data.",
        "Denial of Service": "Dashboard unavailable.",
        "Elevation of Privilege": "UI vulnerability escalates privileges."
    }
}

