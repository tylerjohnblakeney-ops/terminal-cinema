import urllib.parse
import webbrowser

def main():
    print("=== UNIVERSAL TERMINAL CINEMA ===")
    title = input("Enter Movie or TV Show Title: ")
    
    # Cleans and formats the text input into a URL format
    encoded_title = urllib.parse.quote(title.lower().strip())
    url = f"https://vidsrc.to{encoded_title}"
    
    print(f"\nOpening stream link in your default browser...")
    # This function automatically detects if the user is on Windows, Mac, or Linux
    webbrowser.open(url)

if __name__ == "__main__":
    main()
