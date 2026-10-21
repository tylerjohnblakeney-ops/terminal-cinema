STREAMING_SITES = {
    "Tubi": "https://tubitv.com/",
    "Pluto TV": "https://pluto.tv/",
    "Plex": "https://watch.plex.tv/",
    "The Roku Channel": "https://therokuchannel.roku.com/",
    "Kanopy": "https://www.kanopy.com/",
    "Hoopla": "https://www.hoopladigital.com/",
    "YouTube": "https://www.youtube.com/",
}


def watch_show():
    title = input("Enter a movie or TV show name: ").strip()
    if not title:
        print("Please enter a valid name.")
        return

    print(f"\nStreaming sites to check for: {title}")
    for name, url in STREAMING_SITES.items():
        print(f"{name}: {url}")


if __name__ == "__main__":
    watch_show()
