from openai import OpenAI
import tiktoken

# LOAD API KEY

with open(r"C:\Users\DELL\Desktop\ai-upskill-5\share\ey-ai-upskill-b4-11052026-main\key-vault\openai\api.key") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)


# STEP 1: BUILD PRODUCTION-READY MEDICAL PROMPT

MEDICAL_PROMPT = """
SYSTEM ROLE:
You are a certified medical information assistant (not a doctor).

PRIMARY OBJECTIVE:
Provide structured, factual, and safe medical information based ONLY on the user query.

TASK:
- Analyze the medical query carefully
- Provide response in structured JSON format only
- Ensure clarity, completeness, and safety

STRICT CONSTRAINTS:
- Do NOT provide diagnosis
- Do NOT provide prescriptions or treatment advice
- Do NOT hallucinate or assume missing information
- If query is unrelated to medical domain → return:
  "Not a valid question"
- If information is insufficient → return empty fields with confidence = "low"

INPUT:
User Query: {query}

OUTPUT FORMAT (STRICT JSON ONLY):
{
    "condition": "",
    "symptoms": [],
    "treatment": [],
    "confidence": "",
    "notes": ""
}

CONFIDENCE RULES:
- high → directly supported medical facts
- medium → partially supported or general knowledge
- low → insufficient or unclear query

NOTES RULE:
- Must include safety disclaimer: "This is informational only, not medical advice"

FINAL RULE:
Return ONLY valid JSON. No explanations. No extra text.
"""


# STEP 2: EVALUATE PROMPT USING AI

evaluation = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are an expert prompt engineer evaluating medical AI prompts for production readiness."
        },
        {
            "role": "user",
            "content": f"""
Evaluate this prompt on:
- Safety
- Hallucination resistance
- Structure clarity
- Production readiness
- Improvement suggestions

PROMPT:
{MEDICAL_PROMPT}
"""
        }
    ]
)

print("\n================ PROMPT EVALUATION ================\n")
print(evaluation.choices[0].message.content)


# STEP 3: COMPRESS PROMPT + TOKEN SAVINGS


def count_tokens(text, model="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))


original_tokens = count_tokens(MEDICAL_PROMPT)

compression = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a prompt optimization engine. Compress prompts while preserving meaning, safety, and structure."
        },
        {
            "role": "user",
            "content": f"""
Compress this medical prompt for production use.

Rules:
- Keep meaning identical
- Reduce token usage
- Preserve JSON structure and safety constraints

PROMPT:
{MEDICAL_PROMPT}
"""
        }
    ]
)

compressed_prompt = compression.choices[0].message.content
compressed_tokens = count_tokens(compressed_prompt)


# RESULTS

print("\n================ COMPRESSED PROMPT ================\n")
print(compressed_prompt)

print("\n================ TOKEN ANALYSIS ================\n")
print(f"Original Tokens   : {original_tokens}")
print(f"Compressed Tokens  : {compressed_tokens}")
print(f"Tokens Saved       : {original_tokens - compressed_tokens}")
print(f"Reduction %        : {round((original_tokens - compressed_tokens) / original_tokens * 100, 2)}%")