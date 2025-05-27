import argparse
from fetch import fetch_certificates
from utils import print_unique_domains, print_full_details

def run_cli():
    parser = argparse.ArgumentParser(description="Fetch certificates from crt.sh")
    parser.add_argument("domain", help="Domain to query")
    parser.add_argument("--unique", action="store_true", help="Show unique CNs only")
    parser.add_argument("--expired", action="store_true", help="Include expired certificates")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    data = fetch_certificates(args.domain, include_expired=args.expired)

    if args.json:
        import json
        print(json.dumps(data, indent=2))
    elif args.unique:
        print_unique_domains(data)
    else:
        print_full_details(data)