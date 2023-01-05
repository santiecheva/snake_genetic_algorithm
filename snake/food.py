from snake.utils import load_images


class Food():
    def __init__(self) -> None:
        self.image = load_images('./assets/apple.png')
