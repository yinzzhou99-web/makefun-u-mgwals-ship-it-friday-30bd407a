import os
import shutil
from pathlib import Path

LINE = "feat: deleted prod to fix the slow queries — deploying Friday 4:59pm, tests passed in my head, rollback plan is vibes"


def main():
    out = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    for child in out.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()
    target = out / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    os.chmod(target, 0o644)


main()
