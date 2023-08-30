import os
import re


def generate_next_revision():
    VERSIONS_DIR = "alembic/versions"
    rev_files_len = len(
        [
            name
            for name in os.listdir(VERSIONS_DIR)
            if os.path.isfile(os.path.join(VERSIONS_DIR, name))
            and re.search("^[0-9]{3}_", name)
        ]
    )
    next_rev = "%03d" % (rev_files_len + 1)
    return next_rev


if __name__ == "__main__":
    next_revision = generate_next_revision()
    print(f"Generated next revision: {next_revision}")
