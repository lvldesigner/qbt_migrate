"""qBt Migrate, change the paths of existing torrents in qBittorrent, as well as convert paths to Windows/Linux/Mac"""

import logging
import os


__version__ = "2.3.2" + os.getenv("VERSION_TAG", "")


def __getattr__(name):
    """Lazy import to avoid circular dependencies during build."""
    if name == "FastResume":
        from qbt_migrate.classes import FastResume

        return FastResume
    elif name == "QBTBatchMove":
        from qbt_migrate.classes import QBTBatchMove

        return QBTBatchMove
    elif name == "convert_slashes":
        from qbt_migrate.methods import convert_slashes

        return convert_slashes
    elif name == "discover_bt_backup_path":
        from qbt_migrate.methods import discover_bt_backup_path

        return discover_bt_backup_path
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


logging.getLogger(__name__).addHandler(logging.NullHandler())
