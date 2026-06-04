"""
architecture.py
ASCII architecture diagram for the X-Ray AI system.
"""

architecture_diagram = r"""
Clinician Workstation
        |
        v
+------------------+
|   API Gateway    |
+------------------+
        |
        v
+------------------+
| Preprocessing    |
+------------------+
        |
        v
+------------------+
| Model Inference  |
+------------------+
        |
        v
+------------------+
|   EHR System     |
+------------------+
"""

def print_architecture():
    print(architecture_diagram)

