import os

TEXT = (
    "The oldest tree alive was old before the first city, and a human life "
    "is a narrow band of its rings. It grows a hair's width in a good year. "
    "It has never hurried. It is still growing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
