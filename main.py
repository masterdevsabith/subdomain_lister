import requests


website_url = input("enter target website url: ").strip().lower()


def find_subdomain(url):
    count = 0
    with open('db/available_subdomain.txt', 'r+') as delete_this:
        delete_this.truncate()
    with open('data/subdomain_small_list.txt', 'r') as file:
        for line in file:
            try:
                sub = line.strip()
                x = requests.get(f"https://{sub}.{url}/", timeout=5)
                if x.status_code == 200:
                    with open('db/available_subdomain.txt', 'a') as file2:
                        file2.write(line)
                    count += 1
                else:
                    pass
            except requests.exceptions.RequestException:
                continue
    return f'{count} subdomains found'


result = find_subdomain(website_url)
print(result)


# geeksforgeeks.org
