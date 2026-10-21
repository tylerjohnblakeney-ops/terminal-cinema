import urllib.parse
import webbrowser


STREAMING_SERVICES = {
    "Netflix": "netflix.com",
    "Prime Video": "primevideo.com",
    "Disney+": "disneyplus.com",
    "Hulu": "hulu.com",
    "Apple TV": "tv.apple.com",
}


def make_google_search(query):
    return "https://www.google.com/search?" + urllib.parse.urlencode(
        {"q": query}
    )


def watch_show():
    title = input("Enter a movie or TV show name: ").strip()
    if not title:
        print("Please enter a valid name.")
        return

    country = input("Country or region (for example, US or GB) [US]: ").strip()
    country = country or "US"

    links = [
        (
            "JustWatch availability search",
            make_google_search(f'"{title}" JustWatch where to watch {country}'),
        )
    ]

    for service, domain in STREAMING_SERVICES.items():
        links.append(
            (
                f"{service} search",
                make_google_search(f'site:{domain} "{title}"'),
            )
        )

    print(f"\nSearch links for: {title}")
    for number, (label, url) in enumerate(links, start=1):
        print(f"{number}. {label}\n   {url}")

    while True:
        choice = input("\nEnter a number to open a link, or 0 to quit: ").strip()

        if choice == "0":
            return

        try:
            index = int(choice) - 1
            if not 0 <= index < len(links):
                raise ValueError
        except ValueError:
            print(f"Enter a number from 1 to {len(links)}, or 0 to quit.")
            continue

        opened = webbrowser.open_new_tab(links[index][1])
        if not opened:
            print("Could not open a browser here. Copy the URL printed above.")
        return


if __name__ == "__main__":
    watch_show()
