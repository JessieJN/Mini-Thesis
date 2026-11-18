import pandas as pd
from zxcvbn import zxcvbn


def evaluate_zxcvbn(passwords):
    results = []

    for password in passwords:
        result = zxcvbn(password)

        results.append({
            "guesses": result["guesses"],
            "log10_guesses": result["guesses_log10"],
            "score": result["score"]
        })

    return pd.DataFrame(results)