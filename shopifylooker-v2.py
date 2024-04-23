import requests
from bs4 import BeautifulSoup
import threading
from queue import Queue

# Using a session for efficient requests
session = requests.Session()

# Function to process each URL
def process_url(q):
    while not q.empty():
        url = q.get()
        try:
            # Ensure URL starts with https://
            if not url.startswith('https://'):
                url = 'https://' + url

            # Make a GET request (using the session)
            response = session.get(url)
            content = response.content
            soup = BeautifulSoup(content, 'html.parser')

            # Efficiently parse required data
            page_title = soup.title.string if soup.title else "No Title"
            status_code = response.status_code
            cloudflare_status = "Yes" if "cloudflare" in response.headers.get("Server", "").lower() else "No"
            shopify_found = soup.find(text=lambda text: "Shopify" in text or "Powered by Shopify" in text) is not None

            # Prepare the result string
            result = f"AUTHOR: https://github.com/darklytornadoxd | URL: {url} | PAGE TITLE: {page_title} | STATUS CODE: {status_code} | CLOUDFLARE: {cloudflare_status}"

            # Efficient file writing (single file, buffered)
            with open("results.txt", "a") as results_file:
                if shopify_found:
                    results_file.write(f"{result} | VALID\n")
                else:
                    results_file.write(f"{result} | INVALID\n")

        except Exception as e:
            print(f"Error processing {url}: {e}")
        finally:
            q.task_done()

# Main function to read URLs and manage threads
def main():
    # Read URLs from file
    with open("output.txt", "r") as file:
        urls = [line.strip() for line in file.readlines()]

    # Experiment with thread count for optimal performance
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