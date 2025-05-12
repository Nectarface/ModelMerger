
def normalize_weights(weight_list):
    total = sum(weight_list)
    return [round(w / total, 6) for w in weight_list] if total > 0 else weight_list
