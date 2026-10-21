import urllib.parse
import webbrowser


STREAMING_SERVICES = {
    "Netflix": "netflix.com",
    "Prime Video": "primevideo.com",
    "Disney+": "disneyplus.com",
    "Hulu": "hulu.com",
    "Apple TV": "tv.apple.com",
}


def watch_show():
    title = input("Enter a movie or TV show name: ").strip()
    if not title:
        print("Please enter a valid name.")
        return

    country = input("Country code for JustWatch (for example, US or GB) [US]: ")
    country = country.strip().lower() or "us"

    encoded_title = urllib.parse.quote_plus(title)
    links = [
        (
            "JustWatch — check availability",
            f"https://www.justwatch.com/{country}/search?q={encoded_title}",
        )
    ]

    for service, domain in STREAMING_SERVICES.items():
        search = urllib.parse.urlencode({"q": f'site:{domain} "{title}"'})
        links.append((f"{service} search", f"https://www.google.com/search?{search}"))

    print(f"\nLinks for: {title}")
    for number, (label, url) in enumerate(links, start=1):
        print(f"{number}. {label}: {url}")

    choice = input("\nEnter a link number to open it, or press Enter to quit: ").strip()
    if not choice:
        return

    try:
        index = int(choice) - 1
        if not 0 <= index < len(links):
            raise ValueError
    except ValueError:
        print("Please enter one of the listed numbers.")
        return

    webbrowser.open(links[index][1])


if __name__ == "__main__":
    watch_show()
