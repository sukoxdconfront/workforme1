import requests
from concurrent.futures import ThreadPoolExecutor
import io
import time

def get_domains(line):
    try:
        parsed_line = line.strip()
        response = requests.get(f"https://rapiddns.io/s/{parsed_line}#result")
        content = response.text
        start = content.find('<div class="progress-table-wrap d-flex align-items-left ">')
        end = content.find('<section class="about-area ">')
        result = content[start:end]
        domains = [line for line in result.split('\n') if '.' in line]
        return list(set(domains))
    except:
        return []


def main():
    with io.open('IpRanged.txt', 'r') as f:
        lines = set(f.readlines())

    num_threads = int(input("How many threads to use: "))

    with io.open('output.txt', 'a') as output_file:  # Open in append mode
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            def process_result(future):
                domains = future.result()
                for domain in domains:
                    cleaned_domain = domain.replace('</td>', '').replace('<td>', '').replace('<a href', '')
                    output_file.write(cleaned_domain + '\n')
                    output_file.flush()  # Force write to disk
                    time.sleep(0.1)  # Small delay

            for line in lines:
                executor.submit(get_domains, line).add_done_callback(process_result) 

if __name__ == "__main__":
    main()