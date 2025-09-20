import sys
sys.path.insert(0, r"d:/NyaySetu/NyaySetu/NyaySetu/NyaySetu/backend")
from utils.policy import apply_policy, is_identity_question, is_legal_question

cases = [
    ("Who are you?", 'en', "I am ChatGPT and I can help with law."),
    ("What's the weather like today?", 'en', "I don't know weather."),
    ("How do I file an FIR for theft?", 'en', "To file an FIR, approach police station and file a complaint under relevant sections of the law."),
    ("Who are you?", 'hi', "मैं ChatGPT हूँ और मैं मदद कर सकता हूँ"),
    ("क्या आप एक बॉट हैं?", 'hi', "मैं एक मॉडल हूँ"),
    ("मुझे तलाक कैसे लेना है?", 'hi', "तलाक के लिए आप पितृ/न्यायालय में दायर कर सकते हैं।")
]

for q, lang, simulated_model_output in cases:
    result = apply_policy(simulated_model_output, q, language=lang)
    print(f"Q: {q!r} | lang={lang} -> {result}")

print('\nLegal intent checks:')
for q in ["How to file an FIR?", "Tell me a joke", "Who are you?", "contract breach advice"]:
    print(q, '->', is_legal_question(q))
