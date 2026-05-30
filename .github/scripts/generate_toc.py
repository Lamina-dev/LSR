import os
import re

STORE_DIR = "store"
OLD_DIR = os.path.join(STORE_DIR, "old")


def get_title(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    return os.path.splitext(os.path.basename(filepath))[0]


def get_lsr_number(filename):
    match = re.search(r"LSR-(\d+)", filename)
    if match:
        return int(match.group(1))
    return 999


def collect_entries(directory, path_prefix):
    entries = []
    if not os.path.isdir(directory):
        return entries
    for filename in os.listdir(directory):
        if re.match(r"LSR-\d+\.md$", filename):
            filepath = os.path.join(directory, filename)
            title = get_title(filepath)
            link_path = f"{path_prefix}/{filename}"
            entries.append((get_lsr_number(filename), title, link_path))
    entries.sort(key=lambda x: x[0])
    return entries


def main():
    current_entries = collect_entries(STORE_DIR, "store")
    old_entries = collect_entries(OLD_DIR, "store/old")
    lines = []
    lines.append("# LSR目录")

    for num, title, path in current_entries:
        lines.append(f"- [{title}]({path})")

    lines.append("")
    lines.append("_由于Lamina项目的发展，部分LSR已被废弃。以下是旧的LSR列表，供参考。_")
    lines.append("")
    lines.append("## Old LSRs")

    for num, title, path in old_entries:
        lines.append(f"- [{title}]({path})")

    lines.append("")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("README.md updated successfully.")


if __name__ == "__main__":
    main()
