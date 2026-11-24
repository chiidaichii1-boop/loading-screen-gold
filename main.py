"""Loading Screen Gold: A Tip in 200 Characters — make.fun entry.

Writes one loading-screen tip for stressed developers and AI coding
agents to /output/entry.txt.
"""

import os

TIP = (
    "Stuck at 99%? The bar is not frozen — it is thinking. Take one "
    "breath, read the last log line, and remember: every deploy you "
    "survived started exactly like this."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
