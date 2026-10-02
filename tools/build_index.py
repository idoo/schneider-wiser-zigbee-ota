"""Rebuild index.json (zigpy/ZHA) and z2m-index.json from sources.json.

    uv run --with zigpy tools/build_index.py
"""

import hashlib
import json
import pathlib
import re

import zigpy.ota.image

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = "https://raw.githubusercontent.com/idoo/schneider-wiser-zigbee-ota/main/"
HW_IN_NAME = re.compile(r"-([0-9A-Fa-f]{4})-([0-9A-Fa-f]{4})\.zigbee$")


def entry(name: str, meta: dict) -> tuple[dict, dict]:
    data = (ROOT / meta["path"]).read_bytes()
    image, rest = zigpy.ota.image.parse_ota_image(data)
    assert not rest, name
    header = image.header

    hw = {}
    if match := HW_IN_NAME.search(name):
        hw = {"min": int(match[1], 16), "max": int(match[2], 16)}
    elif header.minimum_hardware_version is not None:
        hw = {
            "min": header.minimum_hardware_version,
            "max": header.maximum_hardware_version,
        }

    url = RAW + meta["path"]
    zigpy_fw = {
        "binary_url": url,
        "manufacturer_id": header.manufacturer_id,
        "image_type": header.image_type,
        "file_version": header.file_version,
        "file_size": len(data),
        "checksum": "sha3-256:" + hashlib.sha3_256(data).hexdigest(),
        "release_url": meta["url"],
    }
    z2m_fw = {
        "fileName": name,
        "fileVersion": header.file_version,
        "fileSize": len(data),
        "url": url,
        "originalUrl": meta["url"],
        "imageType": header.image_type,
        "manufacturerCode": header.manufacturer_id,
        "sha512": hashlib.sha512(data).hexdigest(),
        "otaHeaderString": bytes(header.header_string).rstrip(b"\x00").decode(),
    }
    if hw:
        zigpy_fw |= {"min_hardware_version": hw["min"], "max_hardware_version": hw["max"]}
        z2m_fw |= {"hardwareVersionMin": hw["min"], "hardwareVersionMax": hw["max"]}
    return zigpy_fw, z2m_fw


def main() -> None:
    sources = json.loads((ROOT / "sources.json").read_text())
    pairs = [entry(name, meta) for name, meta in sources.items() if meta["in_index"]]
    (ROOT / "index.json").write_text(
        json.dumps({"firmwares": [p[0] for p in pairs]}, indent=2) + "\n"
    )
    (ROOT / "z2m-index.json").write_text(
        json.dumps([p[1] for p in pairs], indent=2) + "\n"
    )
    print(f"{len(pairs)} images indexed")


if __name__ == "__main__":
    main()
