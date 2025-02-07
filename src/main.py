from src.hello import hello


def main(msg) -> str:
    return hello(msg)


if __name__ == "__main__":
    _ = main("Hello from bootstrap-python-project!")
