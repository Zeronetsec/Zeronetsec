<!-- https://github.com/Zeronetsec/Zeronetsec -->

# Installation
`install.sh` optional options (can be used together):
- `--home=<path>`
- └── override `$HOME` value.
- `--backup`
- └── create a backup of the existing zeronetsec installation before replacing it.

### Usage
```bash
git clone https://github.com/Zeronetsec/Zeronetsec
bash Zeronetsec/install.sh <option>
```

# Uninstallation
`uninstall.sh` optional options (can be used together):
- `--home=<path>`
- └── override `$HOME` value.
- `--remove-backup`
- └── remove all backup found.

### Usage
```bash
export prefix="${PREFIX:-/usr}"
bash $prefix/opt/zeronetsec/uninstall.sh <option>
```

<!-- Copyright (c) 2026 Zeronetsec -->