import webbrowser
import urllib.parse

def watch_show():
    query = input("Enter the movie or TV show name: ")
    
    if not query.strip():
        print("Please enter a valid name!")
        return

    encoded_query = urllib.parse.quote(query)
    url = f"https://google.com+{encoded_query}"

    print(f"Opening streaming search for: {query}...")
    webbrowser.open(url)

if __name__ == "__main__":
    watch_show()
