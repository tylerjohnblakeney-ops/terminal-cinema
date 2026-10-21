import urllib.parse


STREAMING_SERVICES = {
    "Tubi (free with ads)": "tubitv.com",
    "Pluto TV (free with ads)": "pluto.tv",
    "Plex (free with ads)": "watch.plex.tv",
    "The Roku Channel (free with ads)": "therokuchannel.roku.com",
    "Kanopy (library access)": "kanopy.com",
    "Hoopla (library access)": "hoopladigital.com",
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
