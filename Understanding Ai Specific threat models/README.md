2. MODULE README — Understanding AI Specific Threat Models
Location:
Understanding_AI_Specific_Threat_Models/README.md

Module 1 — Understanding AI‑Specific Threat Models
This module contains my reconstructed and expanded version of the Module 1 lab from the Coursera course:

Secure AI Threat Model & Test Endpoints — Module 1: Understanding AI‑Specific Threat Models

The goal of this module is to build a complete threat model for an LLM‑powered banking assistant (“SecureBank”), including:

AI‑specific attack surfaces

STRIDE analysis

Architecture diagrams

Prompt filtering logic

Guardrail enforcement

LLM simulation

Unit tests for guardrails and filters

The original lab provided only partial outputs. I rebuilt the entire module using the scan results and assignment instructions, adding missing components and expanding the technical depth.

Folder Structure
Code
Understanding_AI_Specific_Threat_Models/
└── Analyze_ThreatModel_SecureBanks_LLM_Infrastructure/
    ├── data/
    ├── sample_prompts/
    ├── notebooks/
    ├── src/
    ├── test/
    └── README.md
Key Components
SecureBank Threat Model Notebook
A complete walkthrough of:

System architecture

Trust boundaries

STRIDE analysis

Threat enumeration

Mitigation strategies

Source Code (src/)
Includes:

api_guard.py — API-level guardrails

prompt_filters.py — Prompt sanitization

policy_enforcer.py — Policy enforcement logic

llm_simulator.py — Lightweight LLM behavior simulator

architecture_securebank.py — Architecture definitions

stride_securebank.py — STRIDE threat definitions

Unit Tests (test/)
Covers:

Guardrail behavior

Prompt filtering

LLM simulator responses
