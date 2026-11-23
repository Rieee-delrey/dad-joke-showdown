import os

JOKE = "I told my wife the vacuum was broken. My son said, 'It sucks.' I said, 'No, that's the problem - it doesn't.'"


def main():
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "entry.txt must read back byte-identical to the joke"
    assert written.encode("utf-8") == JOKE.encode("utf-8")


if __name__ == "__main__":
    main()
