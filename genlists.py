import requests, json, os, sys

domain_ownership = json.loads(open("ownership.json").read())

domain_owner_map = {}

for domain in domain_ownership:
    owner = domain_ownership[domain]
    if owner not in domain_owner_map:
        domain_owner_map[owner] = []
    domain_owner_map[owner].append(domain)

try:
    os.mkdir("data")
except:
    pass

for owner in domain_owner_map:
    try:
        outfile = open(f"data/{owner}.txt", 'w', encoding="UTF-8")
        outfile.write("\n".join(domain_owner_map[owner]))
        outfile.close()
    except Exception as err:
        print(err)
