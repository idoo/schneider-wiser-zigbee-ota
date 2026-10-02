# Schneider Electric Wiser Zigbee firmware

Backup of the official Schneider Electric Wiser Zigbee OTA images, plus an index so Home Assistant ZHA can install them.

All files come from Schneider's own CDN (`wiserheat-pkgs.se-ssl-cloud.com`), byte for byte. The set matches the Wiser hub release matrix (system release 4.48.2) and [Koenkk/zigbee-OTA#1324](https://github.com/Koenkk/zigbee-OTA/pull/1324). `sources.json` has the original URL, CDN date and sha of every file.

## Home Assistant (ZHA)

Add to `configuration.yaml` and restart:

```yaml
zha:
  zigpy_config:
    ota:
      extra_providers:
        - type: zigpy_remote
          url: https://raw.githubusercontent.com/idoo/schneider-wiser-zigbee-ota/main/index.json
          manufacturer_ids: [0x105E]
```

Updates show up as normal update entities on the device page. Battery devices only pick them up when they wake.

Zigbee2MQTT already gets these from Koenkk's index. `z2m-index.json` is the same list in Z2M format, in case you want to pin it via `ota.zigbee_ota_override_index_location`.

## Folders

- `images/`: current released firmware. Everything with manufacturer `0x105E` is in the indexes.
- `older/`: earlier versions that used to be in Koenkk's index under `Tuya/`. Kept for downgrades, not indexed.
- `unreleased/`: files that sit on Schneider's CDN but are not in the hub release matrix (OMS 0.0.30–0.0.38, FIP 1.4.7 whose header says `R&D`). Not indexed. Don't flash these unless you know why.

The Wiser smart plug image (`120B-210B…`, Heiman manufacturer code) is backed up but kept out of the index, so it can't be offered to regular Heiman plugs.

## Firmware

File names follow Schneider's convention `manufacturer-imageType-fileVersion-hwMin-hwMax` in hex. HW ranges in the index come from the file name and match the OTA headers.

Schneider doesn't publish which image type belongs to which product. Most images carry the Zigbee model strings they serve, so this part is read from the firmware itself:

| Image type | Devices (Zigbee model) |
|---|---|
| 0x0010, 0x0012 | NHPB/SWITCH/1, NHPB/SHUTTER/1 |
| 0x0011 | NHPB/DIMMER/1, NHPB/UNIDIM/1 |
| 0x0013 | NHROTARY/DIMMER/1, NHROTARY/UNIDIM/1 |
| 0x0014 | NHMOTION/SWITCH/1 |
| 0x0015 | NHMOTION/DIMMER/1, NHMOTION/UNIDIM/1 |
| 0x000D | PUCK/SWITCH/1, PUCK/DIMMER/1, PUCK/SHUTTER/1 |
| 0x000B / 0x000C | Merten 1GANG/\* / 2GANG/\* (switch, dimmer, shutter, DALI) |
| 0x0016 / 0x003D | FLS/SYSTEM-M/4 / FLS/AIRLINK/4 |
| 0x003F / 0x0040 | SOCKET/OUTLET/1 / SOCKET/OUTLET/2 |
| 0x0051 | EVSCKT/OUTLET/1 |
| 0x0043 | W599001 smoke alarm |
| 0x0024 | CCT591011_AS door sensor (0x0025–0x0027: the other `_AS` sensors) |
| 0x0035–0x0037, 0x004F | Clipsal Iconic CH10AX/\*, CH2AX/SWITCH/1, CH/DIMMER/\*, CH/DALI/1, CHFAN/SWITCH/1 |
| 0x1200–0x1204 | Floor heating thermostats (EKO07259, WDE002497, WDE011680, S520619), going by the folder name and version scheme |

The rest (iTRV, RTR/RTR2 room thermostats, UFH, BoilerRelay, 16A, PMM, FIP, OMS, CLO, PTC, SEFF) only has the folder name to go on.

ZHA only offers an image whose type and HW range match what the device itself reports, so this list is just for reading.

| Family (Schneider folder) | Image type | Version | HW range | Published | File |
|---|---|---|---|---|---|
| 16A | 0x0E00 | 1.8.12 | 0000–00FF | 2024-07-19 | [105E-0E00-01080C00-0000-00FF.zigbee](images/105E-0E00-01080C00-0000-00FF.zigbee) |
| BoilerRelay | 0x0800 | 1.0.2 | 0100–01FF | 2024-10-16 | [105E-0800-01000200-0100-01FF.zigbee](images/105E-0800-01000200-0100-01FF.zigbee) |
| C4Bond | 0x000B | 3.1.1 | 0100–02FF | 2026-05-05 | [105E-000B-030101FF-0100-02FF.zigbee](images/105E-000B-030101FF-0100-02FF.zigbee) |
| C4Bond | 0x000C | 3.1.1 | 0100–02FF | 2026-05-05 | [105E-000C-030101FF-0100-02FF.zigbee](images/105E-000C-030101FF-0100-02FF.zigbee) |
| CFMT | 0x1200 | 1.0.71 | 0000–00FF | 2024-06-28 | [105E-1200-01004700-0000-00FF.zigbee](images/105E-1200-01004700-0000-00FF.zigbee) |
| CFMT | 0x1201 | 1.0.71 | 0000–00FF | 2024-06-28 | [105E-1201-01004700-0000-00FF.zigbee](images/105E-1201-01004700-0000-00FF.zigbee) |
| CFMT | 0x1202 | 1.0.71 | 0000–00FF | 2024-06-28 | [105E-1202-01004700-0000-00FF.zigbee](images/105E-1202-01004700-0000-00FF.zigbee) |
| CFMT | 0x1203 | 1.0.71 | 0000–00FF | 2024-06-28 | [105E-1203-01004700-0000-00FF.zigbee](images/105E-1203-01004700-0000-00FF.zigbee) |
| CFMT | 0x1204 | 1.0.71 | 0000–00FF | 2024-06-28 | [105E-1204-01004700-0000-00FF.zigbee](images/105E-1204-01004700-0000-00FF.zigbee) |
| CLO | 0x005D | 1.0.0 | 0100–0100 | 2025-12-12 | [105E-005D-010000FF-0100-0100.zigbee](images/105E-005D-010000FF-0100-0100.zigbee) |
| EVSO | 0x0051 | 3.0.0 | 0000–00FF | 2025-01-24 | [105E-0051-030000FF-0000-00FF.zigbee](images/105E-0051-030000FF-0000-00FF.zigbee) |
| FanControl | 0x004F | 2.3.0 | 0000–01FF | 2025-03-27 | [105E-004F-020300FF-0000-01FF.zigbee](images/105E-004F-020300FF-0000-01FF.zigbee) |
| FIP | 0x1402 | 1.4.4 | 0102–01FF | 2023-09-01 | [105E-1402-01040400-0102-01FF.zigbee](images/105E-1402-01040400-0102-01FF.zigbee) |
| FIP | 0x1403 | 1.4.2 | 020F–02FF | 2023-09-01 | [105E-1403-01040200-020F-02FF.zigbee](images/105E-1403-01040200-020F-02FF.zigbee) |
| FLS | 0x0016 | 3.0.0 | 0000–01FF | 2025-01-24 | [105E-0016-030000FF-0000-01FF.zigbee](images/105E-0016-030000FF-0000-01FF.zigbee) |
| FLS | 0x003D | 3.0.0 | 0000–01FF | 2025-01-24 | [105E-003D-030000FF-0000-01FF.zigbee](images/105E-003D-030000FF-0000-01FF.zigbee) |
| Iconic/10AX | 0x0035 | 2.10.9 | 0000–01FF | 2024-04-10 | [105E-0035-020A09FF-0000-01FF.zigbee](images/105E-0035-020A09FF-0000-01FF.zigbee) |
| Iconic/2AX | 0x0036 | 2.5.10 | 0000–01FF | 2024-04-10 | [105E-0036-02050AFF-0000-01FF.zigbee](images/105E-0036-02050AFF-0000-01FF.zigbee) |
| Iconic/PB_Dimmer | 0x0037 | 2.3.13 | 0000–01FF | 2024-07-19 | [105E-0037-02030DFF-0000-01FF.zigbee](images/105E-0037-02030DFF-0000-01FF.zigbee) |
| Iconic/Twin_Socket | 0x003E | 1.1.15 | 0000–01FF | 2024-05-24 | [105E-003E-01010F02-0000-01FF.zigbee](images/105E-003E-01010F02-0000-01FF.zigbee) |
| iTRV | 0x0201 | 0.62.0 | 0000–0000 | 2023-09-21 | [105E-0201-0000F230-0000-0000.zigbee](images/105E-0201-0000F230-0000-0000.zigbee) |
| NewHorizon | 0x0010 | 3.0.1 | 0000–01FF | 2025-01-24 | [105E-0010-030001FF-0000-01FF.zigbee](images/105E-0010-030001FF-0000-01FF.zigbee) |
| NewHorizon | 0x0011 | 3.0.1 | 0000–02FF | 2025-01-24 | [105E-0011-030001FF-0000-02FF.zigbee](images/105E-0011-030001FF-0000-02FF.zigbee) |
| NewHorizon | 0x0012 | 3.0.1 | 0000–01FF | 2025-01-24 | [105E-0012-030001FF-0000-01FF.zigbee](images/105E-0012-030001FF-0000-01FF.zigbee) |
| NewHorizon | 0x0013 | 3.0.1 | 0000–02FF | 2025-01-24 | [105E-0013-030001FF-0000-02FF.zigbee](images/105E-0013-030001FF-0000-02FF.zigbee) |
| NewHorizon | 0x0014 | 3.0.1 | 0000–01FF | 2025-01-24 | [105E-0014-030001FF-0000-01FF.zigbee](images/105E-0014-030001FF-0000-01FF.zigbee) |
| NewHorizon | 0x0015 | 3.0.1 | 0000–02FF | 2025-01-24 | [105E-0015-030001FF-0000-02FF.zigbee](images/105E-0015-030001FF-0000-02FF.zigbee) |
| OMS | 0x0052 | 0.0.28 | any | 2025-01-22 | [105E-0052-00001C02.zigbee](images/105E-0052-00001C02.zigbee) |
| PMM | 0x1400 | 1.6.2 | 0301–8131 | 2026-01-05 | [105E-1400-01060200-0301-8131.zigbee](images/105E-1400-01060200-0301-8131.zigbee) |
| PMM | 0x1401 | 1.6.3 | 0302–03FF | 2025-12-17 | [105E-1401-01060300-0302-03FF.zigbee](images/105E-1401-01060300-0302-03FF.zigbee) |
| PTC | 0x0033 | 2.13.20 | any | 2024-12-09 | [105E-0033-020D1467.zigbee](images/105E-0033-020D1467.zigbee) |
| Puck | 0x000D | 3.0.0 | 0000–01FF | 2025-01-24 | [105E-000D-030000FF-0000-01FF.zigbee](images/105E-000D-030000FF-0000-01FF.zigbee) |
| RTR | 0x04E1 | 0.42.2 | 0000–0009 | 2020-10-13 | [105E-04E1-0000A412-0000-0009.zigbee](images/105E-04E1-0000A412-0000-0009.zigbee) |
| RTR2 | 0x04E1 | 0.65.4 | 0100–01FF | 2025-08-22 | [105E-04E1-0000FDEC-0100-01FF.zigbee](images/105E-04E1-0000FDEC-0100-01FF.zigbee) |
| SEFF | 0x05E1 | 0.0.25 | 0000–0200 | 2025-08-22 | [105E-05E1-00000019-0000-0200.zigbee](images/105E-05E1-00000019-0000-0200.zigbee) |
| Sensor | 0x0024 | 1.7.5 | 0000–0000 | 2024-11-29 | [105E-0024-01070542-0000-0000.zigbee](images/105E-0024-01070542-0000-0000.zigbee) |
| Sensor | 0x0025 | 1.7.5 | 0000–0000 | 2024-11-29 | [105E-0025-01070542-0000-0000.zigbee](images/105E-0025-01070542-0000-0000.zigbee) |
| Sensor | 0x0026 | 1.7.5 | 0000–0000 | 2024-11-29 | [105E-0026-01070542-0000-0000.zigbee](images/105E-0026-01070542-0000-0000.zigbee) |
| Sensor | 0x0027 | 1.7.5 | 0000–0000 | 2024-11-29 | [105E-0027-01070542-0000-0000.zigbee](images/105E-0027-01070542-0000-0000.zigbee) |
| SmartPlug | 0x210B | 0.0.34 | 0000–FFFF | 2022-06-30 | [120B-210B-00000022-0000-FFFF.zigbee](images/120B-210B-00000022-0000-FFFF.zigbee) |
| SmartSocket | 0x003F | 3.0.0 | 0000–01FF | 2025-01-25 | [105E-003F-030000FF-0000-01FF.zigbee](images/105E-003F-030000FF-0000-01FF.zigbee) |
| SmartSocket | 0x0040 | 3.0.0 | 0000–01FF | 2025-01-25 | [105E-0040-030000FF-0000-01FF.zigbee](images/105E-0040-030000FF-0000-01FF.zigbee) |
| SmokeAlarm | 0x0043 | 2.7.6 | 0000–0000 | 2023-01-11 | [105E-0043-020706FF-0000-0000.zigbee](images/105E-0043-020706FF-0000-0000.zigbee) |
| UFH | 0x0A00 | 0.32.2 | 0000–0000 | 2022-04-19 | [105E-0A00-00007D02-0000-0000.zigbee](images/105E-0A00-00007D02-0000-0000.zigbee) |
| Zigbee | 0x04B0 | 1.0.4 | 0000–00FF | 2022-08-12 | [105E-04b0-01000400-0000-00FF.zigbee](images/105E-04b0-01000400-0000-00FF.zigbee) |

Going from 2.x to 3.x on NewHorizon switches and dimmers is a big jump. Update one device first.

## Rebuild the index

```sh
uv run --with zigpy tools/build_index.py
```
