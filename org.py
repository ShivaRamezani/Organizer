import shutil
from utils import read_json
from pathlib import Path
from data import data_dir
import json

class OrganizerDir():
    """class to organize a directory.

    example:
    >>> obj = OrganizerDir()
    >>> obj.run(to_organize_directory)
    """
    suffix_dir = read_json(data_dir / "suffix_dir.json")

    def run(self, to_organize_dir):
        """runs the job of organizing

        :param to_organize_dir: the path of the directory
        :type to_organize_dir: Path
        """
        self.to_organize_dir = Path(to_organize_dir).resolve()
        for path in self.to_organize_dir.iterdir():
            if path.is_dir():
                #to skip the dirs we are making
                if path.name in OrganizerDir.suffix_dir.values():
                    continue

                dest = 'dirs'
                DEST_DIR = self.to_organize_dir / dest
                DEST_DIR.mkdir(exist_ok=True)
                shutil.move(str(path), str(DEST_DIR))

            elif path.is_file():
                suffix = path.suffix
                dest = OrganizerDir.suffix_dir.get(suffix)

                #to skip if for a suffix, there is no destination defined.
                if not dest:
                    continue

                DEST_DIR = self.to_organize_dir / dest
                DEST_DIR.mkdir(exist_ok=True)
                shutil.move(str(path), str(DEST_DIR))


if __name__ == "__main__":
    #enter your own path
    mypath = Path('/', 'mnt', 'c', 'Users', 'shvra', 'Downloads')
    organizer = OrganizerDir()
    organizer.run(mypath)