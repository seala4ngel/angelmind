#!/usr/bin/env python3
import sys
import json
import argparse
from core.engine import ArsenalEngine
from modules.recon import SubHunter, PortProbe, Fingerprint
from modules.exploit import SQLi, XSS, SSRF, SSTI, GraphQL, Deser, AuthBypass, Chain, VulnTrigger
from modules.scanner import Misconfig, LeakScan, BucketScan
from modules.fuzz import WebFuzz, APIFuzz
from modules.c2 import Implant
from modules.post import Privesc

def main():
    parser = argparse.ArgumentParser(description='Arsenal Apik v2.0 — 17 Custom Modules')
    parser.add_argument('--module', '-m', required=True,
                        choices=[
                            'subhunter', 'portprobe', 'fingerprint',
                            'sqli', 'xss', 'ssrf', 'ssti', 'graphql', 'deser', 'authbypass', 'chain', 'vulntrigger',
                            'misconfig', 'leakscan', 'bucketscan',
                            'webfuzz', 'apifuzz',
                            'implant', 'privesc'
                        ],
                        help='Module to run')
    parser.add_argument('--target', '-t', required=True, help='Target URL or domain')
    parser.add_argument('--param', '-p', help='Parameter name for exploit modules')
    parser.add_argument('--output', '-o', default='json', help='json or text')
    
    args = parser.parse_args()
    engine = ArsenalEngine()
    result = {}
    
    if args.module == 'subhunter':
        result = SubHunter(engine).scan(args.target)
    elif args.module == 'portprobe':
        result = PortProbe(engine).scan(args.target)
    elif args.module == 'fingerprint':
        result = Fingerprint(engine).scan(args.target)
    elif args.module == 'sqli':
        result = SQLi(engine).scan(args.target, args.param)
    elif args.module == 'xss':
        result = XSS(engine).scan(args.target, args.param)
    elif args.module == 'ssrf':
        result = SSRF(engine).scan(args.target, args.param)
    elif args.module == 'ssti':
        result = SSTI(engine).scan(args.target, args.param)
    elif args.module == 'graphql':
        result = GraphQL(engine).scan(args.target)
    elif args.module == 'deser':
        result = Deser(engine).scan(args.target, args.param)
    elif args.module == 'authbypass':
        result = AuthBypass(engine).scan(args.target)
    elif args.module == 'chain':
        result = Chain(engine).scan(args.target)
    elif args.module == 'vulntrigger':
        result = VulnTrigger(engine).scan(args.target, args.param)
    elif args.module == 'misconfig':
        result = Misconfig(engine).scan(args.target)
    elif args.module == 'leakscan':
        result = LeakScan(engine).scan(args.target)
    elif args.module == 'bucketscan':
        result = BucketScan(engine).scan(args.target)
    elif args.module == 'webfuzz':
        result = WebFuzz(engine).scan(args.target)
    elif args.module == 'apifuzz':
        result = APIFuzz(engine).scan(args.target)
    elif args.module == 'implant':
        result = Implant(engine).generate(args.target)
    elif args.module == 'privesc':
        result = Privesc(engine).scan(args.target)
    else:
        print(f"Error: Unknown module '{args.module}'")
        sys.exit(1)
    
    print(json.dumps(result, indent=2) if args.output == 'json' else result)

if __name__ == '__main__':
    main()
