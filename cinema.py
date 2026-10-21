import webbrowser
import urllib.parse

def watch_show():
    # 1. Ask the user what they want to watch
    query = input("Enter the movie or TV show name: ")
    
    if not query.strip():
        print("Please enter a valid name!")
        return

    # 2. Clean the input and encode spaces properly
    # This turns "Breaking Bad" into "Breaking%20Bad" for search engines
    encoded_query = urllib.parse.quote(query)
    
    # 3. Choose your target search format
    # OPTION A: Take them directly to a Google Search for that show on your streaming site
    url = f"https://google.com+{encoded_query}"
    
    # OPTION B: If your site has a direct search URL format (like ://site.com)
    # url = f"https://cinevu.icu{encoded_query}"

    print(f"Opening streaming search for: {query}...")
    
    # 4. Open it automatically in the default web browser
    webbrowser.open(url)

if __name__ == "__main__":
    watch_show()
