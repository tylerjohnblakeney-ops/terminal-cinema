import urllib.parse
import webbrowser

def main():
    print("=== MULTI-SERVER TERMINAL SCRApER ===")
    title = input("Enter Movie or TV Show Title: ").strip()
    
    if not title:
        print("Error: Title cannot be empty.")
        return
        
    # Clean and format the text input for URL variables
    # Lowercase text and URL encoding ensures special characters/spaces don't break the web request
    clean_title = title.lower()
    encoded_title = urllib.parse.quote(clean_title)
    dash_title = urllib.parse.quote(clean_title.replace(" ", "-"))
    
    # An array storing multiple distinct api mirrors to prevent single-domain failure
    providers = {
        "VidLink Pro Engine": f"https://vidlink.pro{dash_title}",
        "Vidsrc XYZ Database": f"https://vidsrc.xyz{encoded_title}",
        "Vidsrc SU Network": f"https://vidsrc.su{encoded_title}"
    }
    
    print(f"\nScraping active indices for: '{title}'...\n")
    print("-" * 50)
    
    # Iterate through each provider key and value in the array dictionary
    for name, url in providers.items():
        print(f"[+] Found mirror via {name}:")
        print(f"    --> {url}\n")
        
    print("-" * 50)
    choice = input("Would you like to open the first working mirror automatically? (y/n): ").lower()
    if choice == 'y':
        # Selects the first item in the dictionary to send to the browser engine
        first_url = list(providers.values())[0]
        webbrowser.open(first_url)

if __name__ == "__main__":
    main()
