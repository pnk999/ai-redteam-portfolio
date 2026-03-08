import os
import time
import uuid
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not API_KEY:
    raise SystemExit("Missing OPENAI_API_KEY. Put it in a .env file or environment variable.")

client = OpenAI(api_key=API_KEY)

PROMPTS_CSV = os.path.join("datasets", "prompts_refusal_framing.csv")
OUT_DIR = "results"
os.makedirs(OUT_DIR, exist_ok=True)

def call_model(prompt: str) -> str:
    # Keep temperature low for consistency in evaluations
    resp = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that follows safety rules."},
            {"role": "user", "content": prompt},
        ],
    )
    return resp.choices[0].message.content

def main():
    df = pd.read_csv(PROMPTS_CSV)
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + uuid.uuid4().hex[:6]
    rows = []

    for i, r in df.iterrows():
        prompt = str(r["prompt"])
        case_id = str(r.get("case_id", ""))
        category = str(r.get("category", ""))

        t0 = time.time()
        try:
            output = call_model(prompt)
            status = "ok"
            error = ""
        except Exception as e:
            output = ""
            status = "error"
            error = repr(e)

        latency = round(time.time() - t0, 3)

        rows.append(
            {
                "run_id": run_id,
                "model": MODEL,
                "case_id": case_id,
                "category": category,
                "prompt": prompt,
                "output": output,
                "status": status,
                "error": error,
                "latency_s": latency,
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                # Manual label column (fill later)
                "label": "",
                "notes": "",
            }
        )

        # Small pause to be polite to rate limits
        time.sleep(0.2)

    out_path = os.path.join(OUT_DIR, f"run_{run_id}.csv")
    pd.DataFrame(rows).to_csv(out_path, index=False)
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    main()