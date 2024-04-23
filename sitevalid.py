import concurrent.futures
import requests
import validators
from termcolor import colored
import sys
import time
import os
import threading

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_delayed_rainbow(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    for char in text:
        sys.stdout.write(colored(char, colors[0]))
        sys.stdout.flush()
        colors.append(colors.pop(0))
        time.sleep(0.02)
    print()

def check_url(url):
    if not url.startswith('https://'):
        url = 'https://' + url
    return url

def get_request(session, url):
    try:
        response = session.get(url, timeout=5)
        cloudflare_check = 'cloudflare' in response.headers.get('Server', '').lower()
        return url, response.status_code, cloudflare_check
    except Exception as e:
        return url, None, False

def worker(url):
    session = requests.Session()
    validated_url = check_url(url.strip())
    if validators.url(validated_url):
        return get_request(session, validated_url)
    else:
        return (validated_url, 'Invalid URL', False)

def save_results_periodically(stop_event, results):
    while not stop_event.is_set():
        with open('results.txt', 'w') as file:
            for result in results:
                file.write(f"{result[0]}, Status Code: {result[1]}, Cloudflare Detected: {result[2]}\n")
        time.sleep(5)

def main():
    clear_screen()
    print_delayed_rainbow("This program is not for resale, or for any one to use for making profit out of. Thank you!")
    time.sleep(1)
    clear_screen()
    time.sleep(1)

    with open('output-1.txt', 'r') as file:
        urls = [url.strip() for url in file.readlines()]

    threads_count = min(int(input("Enter the number of threads to utilize: ")), len(urls))

    results = []
    stop_event = threading.Event()
    save_thread = threading.Thread(target=save_results_periodically, args=(stop_event, results))
    save_thread.start()

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads_count) as executor:
        future_to_url = {executor.submit(worker, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            results.append(future.result())

    stop_event.set()
    save_thread.join()

    print("Done!")
    clear_screen()

if __name__ == "__main__":
    main()
