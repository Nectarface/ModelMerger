
def relay_prompt(current_output):
    return {
        "next_model": "DeepSeek",
        "prompt": f"Continue reasoning from: {current_output}"
    }
