#!/usr/bin/env python3
"""Read-only FMini-1 protocol 4 backup audit. No MIDI or restore operations."""
import argparse
import hashlib
import json
import re
from pathlib import Path

def validate(obj):
    if not isinstance(obj, dict) or type(obj.get("fmini1bkp")) is not int or obj["fmini1bkp"] != 1 or type(obj.get("protocol")) is not int or obj["protocol"] != 4:
        raise ValueError("Expected FMini-1 protocol 4 backup")
    slots = obj.get("slots")
    if not isinstance(slots, list) or len(slots) != 200:
        raise ValueError("Expected exactly 200 slots")
    for i, x in enumerate(slots):
        if not isinstance(x, dict) or type(x.get("slot")) is not int or x["slot"] != i or not isinstance(x.get("rec"), str) or not re.fullmatch(r"(?:[0-9a-f]{2}){1,128}", x["rec"]):
            raise ValueError(f"Invalid slot {i}")
    return [{"slot": i, "bytes": len(bytes.fromhex(x["rec"])), "sha256": hashlib.sha256(bytes.fromhex(x["rec"])).hexdigest()} for i, x in enumerate(slots)]

def self_test():
    import copy
    good = {"fmini1bkp": 1, "protocol": 4, "slots": [{"slot": i, "rec": "00ff"} for i in range(200)]}
    assert len(validate(json.loads(json.dumps(good)))) == 200
    for key, value in [("protocol", 3), ("fmini1bkp", True), ("slots", good["slots"][:-1])]:
        bad = copy.deepcopy(good); bad[key] = value
        try: validate(bad)
        except ValueError: pass
        else: raise AssertionError(key)
    for key, value in [("slot", 1), ("rec", "0"), ("rec", "GG"), ("rec", "00"*129), ("rec", "")]:
        bad = copy.deepcopy(good); bad["slots"][0][key] = value
        try: validate(bad)
        except ValueError: pass
        else: raise AssertionError(key)
    print("9 synthetic cases passed")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("backup", nargs="?")
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()
    if a.self_test: self_test()
    elif a.backup:
        raw = Path(a.backup).read_bytes()
        print(json.dumps({"file_sha256": hashlib.sha256(raw).hexdigest(), "slots": validate(json.loads(raw))}, indent=2))
    else: p.error("Provide backup or --self-test")
