import typer


def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(
        False, "--formal", "-f",
        help="Использовать формальное приветствие.",
    ),
):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    """
    # Выбираем приветствие по флагу formal.
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")


if __name__ == "__main__":
    # Запускаем CLI и обрабатываем аргументы.
    typer.run(main)
