import urllib.parse


STREAMING_SERVICES = {
    "Netflix": "netflix.com",
    "Prime Video": "primevideo.com",
    "Disney+": "disneyplus.com",
    "Hulu": "hulu.com",
    "Apple TV": "tv.apple.com",
}


def google_search_url(query):
    return "https://www.google.com/search?" + urllib.parse.urlencode(
        {"q": query}
    )


def watch_show():
    title = input("Enter a movie or TV show name: ").strip()
    if not title:
        print("Please enter a valid name.")
        return

    links = [
        (
            "Check availability on JustWatch",
            google_search_url(f'"{title}" JustWatch where to watch'),
        )
    ]

    for service, domain in STREAMING_SERVICES.items():
        links.append(
            (
                f"Search {service}",
                google_search_url(f'site:{domain} "{title}"'),
            )
        )

    print(f"\nSearch links for: {title}")
    for number, (label, url) in enumerate(links, start=1):
        print(f"\n{number}. {label}\n   {url}")


if __name__ == "__main__":
    watch_show()
