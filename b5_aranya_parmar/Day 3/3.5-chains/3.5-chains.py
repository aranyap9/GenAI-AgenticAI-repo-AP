# ============================================================
# USE CASE: AI-POWERED CYBERSECURITY INCIDENT TRIAGE SYSTEM
# ============================================================
# This LangChain pipeline simulates a SOC (Security Operations Center) assistant.
#
# WHAT IT DOES:
# 1. Takes raw security incident logs as input
# 2. Summarizes the incident
# 3. Classifies the cyber threat type
# 4. Assesses incident severity
# 5. Generates a SOC response plan
#
# REAL-WORLD USE CASES:
# - SOC alert triage
# - SIEM alert enrichment
# - Incident response automation
# - Security analyst assistance
#
# INPUT:
# A raw cybersecurity incident description/log
#
# OUTPUT:
# Structured cybersecurity incident report
# ============================================================


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# LOAD OPENAI API KEY

f = open(r"C:\Users\DELL\Desktop\ai-upskill-5\share\ey-ai-upskill-b4-11052026-main\key-vault\openai\api.key")
apikey = f.read().strip()
f.close()


# INITIALIZE LLM

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=apikey,
    temperature=0
)


# CHAIN 1: INCIDENT SUMMARY

summary_template = """
You are a cybersecurity analyst.

Summarize the following cybersecurity incident in 3-4 lines.

Incident:
{incident}
"""

summary_prompt = ChatPromptTemplate.from_template(summary_template)

summary_chain = summary_prompt | llm


# CHAIN 2: THREAT CLASSIFICATION

classification_template = """
You are a SOC analyst.

Based on the incident summary below, classify the cyber threat type.

Possible Categories:
- Phishing
- Malware
- Brute Force Attack
- Insider Threat
- Data Exfiltration
- Suspicious Activity

Incident Summary:
{summary}

Return ONLY the threat category name.
"""

classification_prompt = ChatPromptTemplate.from_template(classification_template)

classification_chain = classification_prompt | llm


# CHAIN 3: SEVERITY ASSESSMENT

severity_template = """
You are a cybersecurity risk analyst.

Given the following:

Incident Summary:
{summary}

Threat Type:
{threat_type}

Assign severity level:
- Low
- Medium
- High
- Critical

Also provide a short justification.
"""

severity_prompt = ChatPromptTemplate.from_template(severity_template)

severity_chain = severity_prompt | llm


# CHAIN 4: RESPONSE PLAN

response_template = """
You are a SOC incident response expert.

Based on:

Threat Type:
{threat_type}

Severity:
{severity}

Generate a step-by-step incident response plan.

Include:
- Detection
- Containment
- Eradication
- Recovery
"""

response_prompt = ChatPromptTemplate.from_template(response_template)

response_chain = response_prompt | llm


# MAIN PIPELINE FUNCTION

def build_pipeline(incident):

    # STEP 1: INCIDENT SUMMARY
    summary = summary_chain.invoke({
        "incident": incident
    }).content

    # STEP 2: THREAT CLASSIFICATION
    threat_type = classification_chain.invoke({
        "summary": summary
    }).content

    # STEP 3: SEVERITY ASSESSMENT
    severity = severity_chain.invoke({
        "summary": summary,
        "threat_type": threat_type
    }).content

    # STEP 4: RESPONSE PLAN
    response_plan = response_chain.invoke({
        "threat_type": threat_type,
        "severity": severity
    }).content

    # RETURN STRUCTURED OUTPUT
    return {
        "summary": summary.strip(),
        "threat_type": threat_type.strip(),
        "severity": severity.strip(),
        "response_plan": response_plan.strip()
    }


# TAKE INCIDENT INPUT FROM USER

incident_text = input("Enter Cybersecurity Incident:\n")


# RUN PIPELINE

result = build_pipeline(incident_text)

# ---------------------------
# PRINT STRUCTURED REPORT
# ---------------------------
print("\n")
print("        AI CYBERSECURITY INCIDENT REPORT")

print("\nINCIDENT SUMMARY:")
print(result["summary"])

print("\nTHREAT TYPE:")
print(result["threat_type"])

print("\nSEVERITY ASSESSMENT:")
print(result["severity"])

print("\nRESPONSE PLAN:")
print(result["response_plan"])

print("\n==================================================")