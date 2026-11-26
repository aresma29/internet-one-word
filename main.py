from pathlib import Path


def main():
    # Print the one-word entry byte for byte, exactly as stored,
    # resolving entry.txt relative to this file so the script
    # works from any working directory.
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    print(entry_path.read_text(encoding="utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
