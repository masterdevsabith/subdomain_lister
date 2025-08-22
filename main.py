import requests
import threading
from tqdm import tqdm


lock = threading.Lock()


website_url = input("enter target website url: ").strip().lower()


def find_subdomain(url, sub_list, results, index):
    count = 0
    for sub in tqdm(sub_list, desc=f"Thread-{index+1}", position=index):
        try:
            # print(f'going through {sub}')
            req = requests.get(f"https://{sub}.{url}/", timeout=5)
            if req.status_code == 200:
                with open('db/available_subdomain.txt', 'a') as file2:
                    file2.write(sub + '\n')
                    count += 1
        except requests.exceptions.RequestException:
            continue
    results[index] = count


with open('data/subdomain_list.txt', 'r') as f:
    subdomains = [line.strip() for line in f]
    half = len(subdomains) // 2
    part1 = subdomains[:half]
    part2 = subdomains[half:]


results = [0, 0]
t1 = threading.Thread(target=find_subdomain, args=(
    website_url, part1, results, 0))
t2 = threading.Thread(target=find_subdomain, args=(
    website_url, part2, results, 1))

t1.start()
t2.start()


t1.join()
t2.join()


print(f"Total subdomains found: {sum(results)}")

# geeksforgeeks.org
