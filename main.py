"""Write one dad joke to /output/entry.txt for make.fun's Dad Joke Showdown."""

from pathlib import Path

JOKE = "I told my wife the vacuum was broken. My son said, 'It sucks.' I said, 'No, that's the problem - it doesn't.'"

OUTPUT_PATH = Path("/output/entry.txt")


def validate_joke(joke: str) -> str:
    """Return the joke unchanged if it is a non-blank 1-200 character string."""
    text = joke.strip()
    if not text:
        raise ValueError("joke must not be blank")
    if len(text) < 1 or len(text) > 200:
        raise ValueError("joke must be 1-200 characters")
    return text


def write_joke() -> None:
    joke = validate_joke(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(joke, encoding="utf-8")
    expected = joke.encode("utf-8")
    actual = OUTPUT_PATH.read_bytes()
    if actual != expected:
        raise AssertionError("entry.txt bytes do not match the joke")
    if OUTPUT_PATH.read_text(encoding="utf-8") != joke:
        raise AssertionError("entry.txt text does not match the joke")


def main() -> None:
    write_joke()


if __name__ == "__main__":
    main()
