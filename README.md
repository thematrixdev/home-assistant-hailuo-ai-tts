# MINIMAX (HaiLuo) TTS Home-Assistant Custom-Component

## Prerequisite

API Key from Hailuo AI

International https://intl.minimaxi.com/

China https://platform.minimaxi.com/

## Features

- Multiple language support:
  - Spanish
  - French
  - Portuguese
  - Korean
  - Indonesian
  - German
  - Japanese
  - Italian
  - Chinese
  - Cantonese
  - Auto-detect

- Multiple voice

- Two model:
  - Turbo
  - HD

- Adjustable speech parameters:
  - Speed (0.5-2.0)
  - Volume (0-10)
  - Pitch (-12 to 12)

- Optional emotion settings:
  - Happy
  - Sad
  - Angry
  - Fearful
  - Disgusted
  - Surprised
  - Neutral

- English normalization option

## Add to HACS

1. Setup `HACS` https://hacs.xyz/docs/setup/prerequisites
2. In `Home Assistant`, click `HACS` on the menu on the left
3. Select `custom components`
4. Click the menu button in the top right hand corner
5. Choose `custom repositories`
6. Enter `https://github.com/thematrixdev/home-assistant-hailuo-ai-tts` and choose `Integration`, click `ADD`
7. Find and click on `Hailuo-AI TTS` in the `custom repositories` list
8. Click the `DOWNLOAD` button in the bottom right hand corner
9. Restart Home Assistant

## Install

1. Go to `Settings`, `Devices and Services`
2. Click the `Add Integration` button
3. Search `Hailuo-AI TTS`
4. Go through the configuration flow:

## Debug

- Add these lines to `configuration.yaml`

```yaml
logger:
  logs:
    custom_components.hailuo_ai_tts: debug
```

- Restart Home Assistant
- On Home Assistant, go to `Settings` -> `Logs`
- Click the `Show RAW logs` button
- Search `hailuo_ai_tts`

## Support

- Open an issue on GitHub
- Specify:
    - What's wrong
    - Home Assistant version
    - Hailuo-AI TTS custom-component version
    - Configuration (without sensitive data)
    - Logs

## Unofficial support

- Telegram Group https://t.me/smarthomehk

## Tested on

- Ubuntu 24.10
- Home Assistant Container 2025.02
