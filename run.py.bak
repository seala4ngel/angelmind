#!/usr/bin/env python3
import sys
import json
import argparse
from core.engine import ArsenalEngine
from modules.recon import SubHunter, PortProbe, Fingerprint
from modules.exploit import SQLi, XSS, SSRF, SSTI, GraphQL, Deser, AuthBypass, Chain, VulnTrigger
from modules.scanner import Misconfig, LeakScan, BucketScan
from modules.fuzz import WebFuzz, APIFuzz
from modules.c2 import Implant, Beacon
from modules.post import Privesc, Lateral, Cleanup, Persist
from modules.attack import Phishing, ExploitPayload
from modules.research import Weaponize, Diff, Crash
from modules.phish import MailCraft, Pretext

def main():
    parser = argparse.ArgumentParser(description='Arsenal Apik v3.0 — 33 Custom Modules')
    parser.add_argument('--module', '-m', required=True,
                        choices=[
                            'subhunter', 'portprobe', 'fingerprint',
                            'sqli', 'xss', 'ssrf', 'ssti', 'graphql', 'deser', 'authbypass', 'chain', 'vulntrigger',
                            'misconfig', 'leakscan', 'bucketscan',
                            'webfuzz', 'apifuzz',
                            'implant', 'beacon',
                            'privesc', 'lateral', 'cleanup', 'persist',
                            'phishing', 'exploit_payload',
                            'weaponize', 'diff', 'crash',
                            'mailcraft', 'pretext'
                        ],
                        help='Module to run')
    parser.add_argument('--target', '-t', required=True, help='Target URL or domain')
    parser.add_argument('--param', '-p', help='Parameter name or additional data')
    parser.add_argument('--interval', '-i', type=int, default=60, help='Beacon interval')
    parser.add_argument('--jitter', '-j', type=int, default=10, help='Beacon jitter')
    parser.add_argument('--ip', help='IP address')
    parser.add_argument('--port', help='Port')
    parser.add_argument('--platform', default='linux', help='linux/windows')
    parser.add_argument('--mode', default='reverse', help='reverse/bind')
    parser.add_argument('--cve', help='CVE ID')
    parser.add_argument('--exploit-type', default='rce', help='Exploit type')
    parser.add_argument('--before', help='Before hash for diff')
    parser.add_argument('--after', help='After hash for diff')
    parser.add_argument('--template', default='invoice', help='Email template type')
    parser.add_argument('--scenario', default='it_support', help='Pretext scenario')
    parser.add_argument('--os-type', default='linux', help='linux/windows')
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
    elif args.module == 'beacon':
        result = Beacon(engine).scan(args.target, args.interval, args.jitter)
    elif args.module == 'privesc':
        result = Privesc(engine).scan(args.target)
    elif args.module == 'lateral':
        result = Lateral(engine).scan(args.target)
    elif args.module == 'cleanup':
        result = Cleanup(engine).scan(args.target)
    elif args.module == 'persist':
        result = Persist(engine).scan(args.target, args.param, args.os_type)
    elif args.module == 'phishing':
        result = Phishing(engine).scan(args.target, args.param.split(',') if args.param else [], {})
    elif args.module == 'exploit_payload':
        result = ExploitPayload(engine).scan(args.target, args.ip, args.port, args.platform, args.mode)
    elif args.module == 'weaponize':
        result = Weaponize(engine).scan(args.target, args.cve, args.exploit_type)
    elif args.module == 'diff':
        result = Diff(engine).scan(args.target, args.before, args.after)
    elif args.module == 'crash':
        result = Crash(engine).scan(args.target, args.param)
    elif args.module == 'mailcraft':
        result = MailCraft(engine).generate(args.target, args.template)
    elif args.module == 'pretext':
        result = Pretext(engine).generate(args.target, args.scenario)
    else:
        print(f"Error: Unknown module '{args.module}'")
        sys.exit(1)
    
    print(json.dumps(result, indent=2) if args.output == 'json' else result)

if __name__ == '__main__':
    main()
