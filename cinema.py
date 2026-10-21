import webbrowser
import urllib.parse


def watch_show():
    query = input("Enter the movie or TV show name: ").strip()

    if not query:
        print("Please enter a valid name!")
        return

    url = f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}"

    print(f"Opening streaming search for: {query}...")
    webbrowser.open(url)


if __name__ == "__main__":
    watch_show()
