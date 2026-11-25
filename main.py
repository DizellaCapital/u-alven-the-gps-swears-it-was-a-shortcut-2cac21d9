"""The GPS Swears It Was a Shortcut — entry program.

Writes the GPS's own excuse for sending the driver down the wrong road
to MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only. One line, 1-200 characters.
"""

import os
import sys

# The GPS, smug and defensive, blaming its map: the cornfield is still
# Route 9 on paper, and the lake at the end had the better view.
# The em dash keeps it one breath aloud; no dialogue tag, no setup.
LINE = "I didn't take the wrong road \u2014 my map still lists that cornfield as Route 9, and the lake at the end had a better view than your highway ever did."


def main():
    if not 1 <= len(LINE) <= 200:
        print("entry must be 1-200 characters, got %d" % len(LINE), file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
