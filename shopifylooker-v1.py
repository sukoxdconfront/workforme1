import requests
from bs4 import BeautifulSoup
import threading
from queue import Queue

# Function to process each URL
def process_url(q):
    while not q.empty():
        url = q.get()
        try:
            # Ensure URL starts with https://
            if not url.startswith('https://'):
                url = 'https://' + url

            # Make a GET request to the URL
            response = requests.get(url)
            content = response.content
            soup = BeautifulSoup(content, 'html.parser')

            # Parse required data
            page_title = soup.title.string if soup.title else "No Title"
            status_code = response.status_code
            cloudflare_status = "Yes" if "cloudflare" in response.headers.get("Server", "").lower() else "No"
            shopify_found = "Shopify" in content.decode() or "Powered by Shopify" in content.decode()

            # Prepare the result string
            result = f"AUTHOR: https://github.com/darklytornadoxd | URL: {url} | PAGE TITLE: {page_title} | STATUS CODE: {status_code} | CLOUDFLARE: {cloudflare_status}\n"

            # Save the result based on Shopify presence
            if shopify_found:
                with open("valid_results.txt", "a") as valid_file:
                    valid_file.write(result)
            else:
                with open("invalid_results.txt", "a") as invalid_file:
                    invalid_file.write(result)
        except Exception as e:
            print(f"Error processing {url}: {e}")
        finally:
            q.task_done()

# Main function to read URLs and manage threads
def main():
    # Read URLs from file
    with open("input.txt", "r") as file:
        urls = [line.strip() for line in file.readlines()]

    # Ask for the number of threads to use
    num_threads = int(input("Enter the number of threads to use: "))

    # Create a queue and add all URLs to it
    q = Queue()
    for url in urls:
        q.put(url)

    # Create and start threads
    for _ in range(num_threads):
        worker = threading.Thread(target=process_url, args=(q,))
        worker.daemon = True
        worker.start()

    q.join()
    print("Completed processing all URLs.")

if __name__ == "__main__":
    main()
