# SPDX-License-Identifier: GPL-3.0-only
# Run: python test_neon_collection.py /path/to/fmini-1
import sys
from pathlib import Path
sys.path.insert(0, str(Path(sys.argv[1]).resolve() / "tools"))
from gen_fmini_presets import Bank, o, osc_off, co
import fmini_bank
from neon_collection import add_neon

factory = fmini_bank.build(Bank())
assert len(factory.p) == 200
neon = Bank()
add_neon(neon, o, osc_off, co)
assert len(neon.p) == 10
names = [p["name"] for p in neon.p]
assert len(set(names)) == 10
assert not set(names).intersection(p["name"] for p in factory.p)
for p in neon.p:
    assert len(p["name"]) <= 12
    assert len(p["g"]) == 24
    assert any(p["g"][8:12])
    assert 1 <= p["level"] <= 127
    assert all(0 <= x <= 127 for k in ("g","e","amp","send","fxg","arp","lfo") for x in p[k])
assert len(factory.p) == 200
print("10 experimental recipes encoded; 200 factory presets preserved in separate bank")
# This checks encoding only, not sound, storage, firmware build or hardware.
