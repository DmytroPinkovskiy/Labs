import emoji


def show_emoji():
    """Перетворює короткі назви на емодзі."""
    print(emoji.emojize("[emoji] Python :rocket: :snake:", language="alias"))
