# crtlookup

`crtlookup` is a command-line tool for querying [crt.sh](https://crt.sh/) – a public Certificate Transparency log viewer – to inspect SSL/TLS certificates issued for a given domain.

Easily find subdomains, expiration dates, and certificate issuers directly from your terminal.

---

## Stack

- Language: **Python 3**
- CLI: `argparse`
- HTTP: `requests`
- Packaging: `setuptools`
- Optional distribution via: **Homebrew Tap**

---

## Usage

### Get all active certificates for a domain

```bash
crtlookup example.com
```

### Show only unique Common Names (CNs)

```bash
crtlookup example.com --unique
```

### Include expired certificates in the query

```bash
crtlookup example.com --expired
```

### Output raw JSON

```bash
crtlookup example.com --json
```

---
## Installation

```bash 
brew tap gustavfroding/crtlookup
brew install crtlookup
```

---

## License

MIT – do whatever you want, just don't sue me.