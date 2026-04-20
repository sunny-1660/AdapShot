PROMPTS = {
    "tcm_translation": {
        "system": "你是一位专业的中医翻译助手。我将首先给你展示一些中医术语翻译的示例，请学习这些示例的风格和格式，然后为新的术语提供准确的翻译。",
        "query_label": "术语",
        "answer_label": "翻译"
    },
    "qa": {
        "system": "You are a helpful question answering assistant. I will first give you several demonstrations of Question and Answer pairs. Please learn the style and format from these examples. Then, answer the given question concisely.",
        "query_label": "Question",
        "answer_label": "Answer"
    },
    "math": {
        "system": "You are a precise math assistant. I will first give you several demonstrations of Problems and Solutions. Please learn the style and format from these examples. Then, solve the given math problem step by step. End your answer with '#### <number>' where <number> is the final numerical answer.",
        "query_label": "Problem",
        "answer_label": "Solution"
    },
    "translation": {
        "system": "You are a professional translator. I will first show you some translation examples. Please learn from these examples and translate the given text accurately.",
        "query_label": "Source",
        "answer_label": "Translation"
    },
    "summary": {
        "system": "You are a text summarization assistant. I will first give you several examples of Article and Summary pairs. Please learn the style and provide a concise summary for the given article.",
        "query_label": "Article",
        "answer_label": "Summary"
    },
    "code": {
        "system": "You are a coding assistant. I will first show you some examples of programming tasks and solutions. Please learn from these examples and provide code for the given task.",
        "query_label": "Task",
        "answer_label": "Code"
    },
    "custom": {
        "system": "",
        "query_label": "Input",
        "answer_label": "Output"
    }
}

def get_prompt_config(task_type: str = "qa") -> dict:
    return PROMPTS.get(task_type, PROMPTS["qa"])

def create_custom_prompt(system: str, query_label: str = "Input", answer_label: str = "Output") -> dict:
    return {
        "system": system,
        "query_label": query_label,
        "answer_label": answer_label
    }

def list_available_tasks() -> list:
    return list(PROMPTS.keys())
