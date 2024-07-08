import requests
from bs4 import BeautifulSoup
import argparse
from colorama import Fore, Style, init
import ipaddress
import time

init(autoreset=True)

banner = f"""{Fore.LIGHTMAGENTA_EX}
  _
 | |
 | |__   ___  ___  ___ __ _ _ ___
 | '_ \ / _ \/ __|/ __/ _` | '_  \ 
 | | | |  __/\__ \ (_| (_| | | | |
 |_| |_|\___||___/\___\__,_|_| |_|
{Style.RESET_ALL}
      {Fore.RED}CODED BY @wh0l5th3r00t{Style.RESET_ALL} {Fore.YELLOW}|{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}V2.0{Style.RESET_ALL}
"""

print(banner)

def fetch_results(keyword):
    url = f"https://bgp.he.net/search?search%5Bsearch%5D={keyword}&commit=Search"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []

    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) >= 3:
            result = cols[0].text.strip()
            type_ = cols[1].text.strip()
            description = cols[2].text.strip()
            country_img = cols[2].find('img')
            country = country_img['title'] if country_img else 'Unknown'
            results.append((result, type_, description, country))

    return results

def filter_columns(results, ignore):
    filtered_results = []
    for result in results:
        filtered_result = []
        if 'result' not in ignore:
            filtered_result.append(result[0])
        if 'type' not in ignore:
            filtered_result.append(result[1])
        if 'description' not in ignore:
            filtered_result.append(result[2])
        if 'country' not in ignore:
            filtered_result.append(result[3])
        filtered_results.append(filtered_result)
    return filtered_results

def filter_by_country(results, country):
    return [result for result in results if result[3].lower() == country.lower()]

def print_results(results):
    for result in results:
        colored_result = []
        if len(result) > 0:
            colored_result.append(f"{Fore.GREEN}{result[0]}{Style.RESET_ALL}")
        if len(result) > 1:
            colored_result.append(f"{Fore.RED}{result[1]}{Style.RESET_ALL}")
        if len(result) > 2:
            colored_result.append(f"{Fore.CYAN}{result[2]}{Style.RESET_ALL}")
        if len(result) > 3:
            colored_result.append(f"{Fore.MAGENTA}{result[3]}{Style.RESET_ALL}")
        print(f" {Fore.YELLOW}|{Style.RESET_ALL} ".join(colored_result))

def write_results_to_file(results, output_file):
    with open(output_file, 'w') as f:
        for result in results:
            f.write(result[0] + "\n")

def generate_ip_combinations(results):
    ip_combinations = []
    for result in results:
        ip_range = result[0]
        try:
            network = ipaddress.ip_network(ip_range, strict=False)
            for ip in network:
                ip_combinations.append(str(ip))
        except ValueError:
            pass
    return ip_combinations

def write_all_ranges_to_file(ip_combinations, output_all_ranges_file):
    with open(output_all_ranges_file, 'w') as f:
        for ip in ip_combinations:
            f.write(ip + "\n")

def main():
    start_time = time.time()
    parser = argparse.ArgumentParser(
        description='Fetch and filter BGP results.',
        epilog='Example usage: python3 hescan.py -k Microsoft -o results.txt -c US'
    )
    parser.add_argument('-k', '--keyword', required=True, help='Keyword to search for.')
    parser.add_argument('-o', '--output', help='Output file to save the results (only ASN and IP).')
    parser.add_argument('-oar', '--output_all_ranges', help='Output file to save all IP combinations for the results.')
    parser.add_argument('-i', '--ignore', nargs='+', choices=['result', 'type', 'description', 'country'], help='Columns to ignore in the output.')
    parser.add_argument('-c', '--country', help='Filter results by country.')

    args = parser.parse_args()

    html = fetch_results(args.keyword)
    results = parse_results(html)

    if args.ignore:
        results = filter_columns(results, args.ignore)

    if args.country:
        results = filter_by_country(results, args.country)

    print_results(results)

    if args.output:
        write_results_to_file(results, args.output)

    if args.output_all_ranges:
        ip_combinations = generate_ip_combinations(results)
        write_all_ranges_to_file(ip_combinations, args.output_all_ranges)

    end_time = time.time()
    total_time = end_time - start_time
    minutes, seconds = divmod(total_time, 60)

    print(f"{Fore.CYAN}\nResults: {len(results)}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Time: {int(minutes)} min {int(seconds)} sec{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
