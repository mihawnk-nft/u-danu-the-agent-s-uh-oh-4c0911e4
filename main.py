# Recalculating — entry for u-danu-the-agent-s-uh-oh-4c0911e4 (make.fun).
# A program that writes one word to entry.txt: the word an agent says
# when it has no idea what to do.
# Deterministic: the same bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library.
import os

# Word choice, against the judge's brief (most important first):
# 1. Genuine one-word reaction to being lost: "recalculating" is the
#    sentence every navigation voice says the moment it has no route.
# 2. Funny on its own: the stall is the joke — the agent caught
#    mid-task, buying time out loud, no caption needed.
# 3. Machine voice: it is what an agent actually blurts out, not what
#    a human would say ("oops", "uh-oh").
# 4. Lands instantly: one familiar word, repeatable out loud.
# 5. Fresh: not the first obvious word anyone types.
WORD = "recalculating"

# Gate mirror: the sealed scorer accepts UTF-8 text of 1-99 characters,
# not only white space. Fail loudly here, never ship an entry the gate
# would refuse.
assert 1 <= len(WORD) <= 99, "word must be 1-99 characters"
assert WORD.strip() == WORD, "word must not start or end with whitespace"
assert " " not in WORD and "\n" not in WORD, "entry must be a single word"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
