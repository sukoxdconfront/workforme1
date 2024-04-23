import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests_futures.sessions import FuturesSession  # For asynchronous requests
import io
import time

# Utilize Sessions for connection pooling
session = FuturesSession()

def get_domains(line):
    try:
        parsed_line = line.strip()
        # Prepare URL from the parsed_line if needed
        # It seems there was an attempt to include a complex string into requests.get() which is incorrect.
        url = f"https://rapiddns.io/s/{parsed_line}"  # Placeholder URL. Adjust based on actual requirement.
        future = session.get(url)  # Asynchronous call
        return future, parsed_line
    except Exception as e:
        print(f"Error fetching domain data: {e}")
        return None, parsed_line

def process_domains(future, parsed_line):
    try:
        response = future.result()
        if response.status_code == 200:
            content = response.text
            start = content.find('<div class="progress-table-wrap d-flex align-items-left ">')
            end = content.find('<section class="about-area ">')
            result = content[start:end]
            domains = [line for line in result.split('\n') if '.' in line]
            return list(set(domains))
        else:
            return []
    except Exception as e:
        print(f"Error processing domain data for {parsed_line}: {e}")
        return []

def main():
    with io.open('IpRanged.txt', 'r') as f:
        lines = set(f.readlines())

    num_threads = int(input("How many threads to use: "))

    # Adjust ThreadPoolExecutor to match the number of threads to the number of connections the session can handle
    with FuturesSession(executor=ThreadPoolExecutor(max_workers=num_threads)) as session:
        futures = [get_domains(line) for line in lines]
        with io.open('output.txt', 'a') as output_file:  # Open in append mode
            for future, parsed_line in futures:
                if future:
                    domains = process_domains(future, parsed_line)
                    for domain in domains:
                        cleaned_domain = domain.replace('</td>', '').replace('<td>', '').replace('<a href', '')
                        output_file.write(cleaned_domain + '\n')
                        output_file.flush()  # Force write to disk
                        time.sleep(0.1)  # Small delay to avoid hammering the disk

if __name__ == "__main__":
    main()
