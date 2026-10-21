import urllib.parse


STREAMING_SITES = {
    "Tubi": "https://tubitv.com/",
    "Pluto TV": "https://pluto.tv/",
    "Plex": "https://watch.plex.tv/",
    "The Roku Channel": "https://therokuchannel.roku.com/",
    "Kanopy": "https://www.kanopy.com/",
    "Hoopla": "https://www.hoopladigital.com/",
    "YouTube": "https://www.youtube.com/",
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

    print(f"\nFree streaming sites to check for: {title}")
    for name, url in STREAMING_SITES.items():
        print(f"{name}: {url}")

    print("\nOpen a link and search for the title on that site's page.")

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
