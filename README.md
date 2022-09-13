
# CadenceOSHW

Collect Cadence open-source hardware (OSHW) projects, libraries and similar for verification purposes.

Click the link to view the corresponding design table.

[**Designs**](/repos_table.md)


## Distributed with OrCAD/Allegro

Some non OSHW files are provided in

- `C:\Cadence\SPB_17.4\share\orcad\examples\pcbdesign`
- `C:\Cadence\SPB_17.4\share\pcb\pcb_lib\symbols`

## Other Lists

- [KiCad Test-Boards](https://gitlab.com/kicad/code/kicad/-/wikis/Test-Boards)

## Setup

### Install Linux Requirements

```bash
sudo apt install git git-lfs
```

### Install Python Requirements

```bash
python -m pip install -r requirements.txt
```

### Adding new Entries to the Database

1. Fork the repository and use the naming `<author>_<name>`
2. Modify `sql_db.py` to add your designs
3. Run `python sql_db.py` to add the entries
4. Run `python repos_to_md.py` to regenerate the markdown table
