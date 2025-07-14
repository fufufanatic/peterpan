# Peter Pan Bus Confirmation Number Tester

A Python script that tests Peter Pan bus confirmation numbers to find valid ticket purchases.

## Description

This script systematically tests confirmation numbers for Peter Pan bus tickets by checking the reprint URL. It searches through a range of confirmation numbers and identifies which ones correspond to valid ticket purchases.

## Features

- Tests a range of confirmation numbers (18612850-18612900 by default)
- Uses mechanize browser automation for web requests
- Identifies valid confirmation numbers by checking for "Thank you for your purchase" message
- Outputs all valid confirmation number URLs found

## Requirements

### Dependencies
- Python 3.x
- `mechanize` library

### Installation

Install the required dependency:

```bash
pip install mechanize
```

## Usage

Run the script directly:

```bash
python peterpan.py
```

## How It Works

1. The script creates a mechanize browser instance
2. Iterates through confirmation numbers in the specified range
3. For each number, constructs the Peter Pan reprint URL
4. Checks if the page contains "Thank you for your purchase"
5. If found, adds the URL to the list of valid confirmation numbers
6. Outputs all valid confirmation number URLs

## Output Example

```
[*] Testing Confirmation Number: 18612850
[*] Testing Confirmation Number: 18612851
[*] Testing Confirmation Number: 18612852
...
[+] The following links contain valid confirmation numbers:
http://ws.peterpanbus.com/purchase/reprint.aspx?confnum=18612855
http://ws.peterpanbus.com/purchase/reprint.aspx?confnum=18612867
[+] Exiting program ...
```

## Configuration

To modify the confirmation number range, edit the `range()` function in the script:

```python
for confnum in range(18612850, 18612900):  # Change these numbers
```

## Important Notes

⚠️ **Legal and Ethical Considerations:**
- This script is for educational purposes only
- Testing confirmation numbers without authorization may violate terms of service
- Ensure you have permission before testing against live systems
- This tool should not be used for unauthorized access to ticket information

## Security Considerations

- The script makes HTTP requests to external servers
- Consider rate limiting to avoid overwhelming the target server
- Be aware of potential legal implications of automated testing

## Troubleshooting

### Common Issues

1. **Import Error for mechanize**: Install the library using `pip install mechanize`
2. **Connection Errors**: Check your internet connection and the target URL availability
3. **Type Errors**: The script may need updates for newer Python versions

### Linter Warnings

The script may show linter warnings about:
- `read()` method returning `None` - handled by the mechanize library
- String comparison with bytes - the mechanize library handles this conversion

## License

This script is provided as-is for educational purposes. Use responsibly and in accordance with applicable laws and terms of service.

## Disclaimer

This tool is intended for educational and authorized testing purposes only. Users are responsible for ensuring their use complies with all applicable laws and terms of service. 