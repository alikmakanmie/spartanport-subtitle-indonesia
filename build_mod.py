#!/usr/bin/env python3
"""Build the Subtitle Indonesia mod WAD from YOUR OWN original R_LANG_EN.WAD.

No game files are included in this repo. You supply your own dump's
EXEC/WAD/PS4_LE/R_LANG_EN.WAD (456.432 byte, CUSA01623 01.02) and this
script transplants the Indonesian translations from translations.json
into it, entry by entry. The result is byte-identical in size
(456.432 byte) because every translation was budgeted to delta 0 in
total -- the SpartanPort loader rejects any other size.

Texts are handled as latin-1, which round-trips every byte exactly
(including the few UTF-8 symbols such as (R) and em-dash, stored here
as unicode escapes in translations.json).

Usage:
  python3 build_mod.py <original_R_LANG_EN.WAD> <output_R_LANG_EN.WAD>
Then zip the output as mods/Subtitle Indonesia (see README.md).
"""
import json, re, struct, sys, pathlib
TEXT_START, RIVER_END, SIZE_OFF = 0xDCB, 0x4EA08, 0xD84
MARK = re.compile(rb"\*(\d+)(T)?\*\r\n")

def main() -> int:
    src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    data = src.read_bytes()
    assert len(data) == 456432, f"unexpected original size: {len(data)}"
    assert struct.unpack_from("<I", data, SIZE_OFF)[0] == 318537
    table = json.load(open(pathlib.Path(__file__).parent / "translations.json"))
    stream = data[TEXT_START:RIVER_END]
    parts = re.split(MARK, stream)
    buf = []
    changed = 0
    for j in range(1, len(parts) - 1, 3):
        eid = int(parts[j]); txt = parts[j + 2]
        crlf = txt.endswith(b"\r\n")
        if crlf: txt = txt[:-2]
        if str(eid) in table:
            txt = table[str(eid)].encode("latin-1"); changed += 1
        buf.append(b"*" + parts[j] + (parts[j + 1] or b"") + b"*\r\n")
        buf.append(txt + (b"\r\n" if crlf else b""))
    # NOTE: parts[-1] is the last entry's text, already handled in the loop.
    new_stream = b"".join(buf)
    assert len(new_stream) == len(stream), (len(new_stream), len(stream))
    out = data[:TEXT_START] + new_stream + data[RIVER_END:]
    assert len(out) == 456432
    dst.write_bytes(out)
    print(f"changed {changed} entries; wrote {dst} ({len(out)} bytes)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
