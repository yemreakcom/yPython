import os
from urllib.parse import quote


def remove_extension(filepath: str) -> str:
    """Dosya uzantısını kaldırma

    Args:
        filepath (str): Dosya yolu

    Returns:
        str: Uzantsız dosya yolu
    """

    filepath, _ = os.path.splitext(filepath)
    return filepath


def create_link(path: str, header=None) -> str:
    """Verilen yola uygun kodlanmış markdown linki oluşturma

    Args:
        pathname (str): Yol

    Returns:
        str: Oluşturulan link metni
    """

    def barename(path: str) -> str:
        """Dosya veya dizin yolundan, yol ve uzantıyı temizleme

        Args:
            filepath (str): Dosya yolu

        Returns:
            str: Sadece dosya ismi
        """

        pathname = path
        if os.path.isfile(path):
            pathname = remove_extension(path)

        pathname = os.path.basename(pathname)

        return pathname

    def relativepath(path: str) -> str:
        """ Statik yol verisini dinamik yol verisine dönüştürme

        Args:
            pathname (str): Yol ismi

        Returns:
            str: Dönüştürülen metin
        """

        return path.replace(os.getcwd(), '.')

    def encodedpath(path: str) -> str:
        """ Verilen yolu url formatında kodlama

        Windows için gelen '\\' karakteri '/' karakterine çevrilir

        Args:
            pathname (str): Yol ismi

        Returns:
            str: Kodlanmış metin
        """

        return quote(path.replace("\\", "/"))

    pathname = barename(path) if not header else header
    path = relativepath(path)
    path = encodedpath(path)

    link = f"- [{pathname}]({path})\n"
    return link


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


def link_folder(startpath):

    def find_level(root):
        return root.replace(startpath, '').count(os.sep)

    def create_indent(level, size=4):
        return ' ' * size * (level)

    lines = []
    for root, dirs, files in os.walk(startpath):
        if root == startpath:
            continue

        if any(name in root for name in [".git", "res"]):
            continue

        level = find_level(root)
        indent = create_indent(level, size=2)

        if "README.md" in files:
            dirlink = create_link(os.path.join(
                root, "README.md"), header=os.path.basename(root))
        else:
            dirlink = create_link(root)

        lines.append('{}{}'.format(indent, dirlink))

        subindent = create_indent(level + 1, size=2)
        for f in files:
            if "README.md" in f:
                continue

            name = os.path.splitext(f)[0]
            lines.append('{}{}'.format(
                subindent, create_link(os.path.join(root, f))))

    return lines


def create_summary(path):
    with open("SUMMARY.md", "w", encoding="utf-8") as file:
        file.write("".join(link_folder(path)))


if __name__ == "__main__":
    create_summary(os.getcwd())
