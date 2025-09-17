# sha1sum_stdin.py

from typing import List
import hashlib
import pathlib
import sys

def process_file(filename: str) -> bytes:
    return pathlib.Path(filename).read_bytes()

def process_stdin() -> bytes:
    return bytes("".join(sys.stdin), "utf-8")

def sha1sum(data: bytes) -> str:
    sha1_hash = hashlib.sha1()
    sha1_hash.update(data)
    return sha1_hash.hexdigest()

def output_sha1sum(data: bytes, filename: str = "-") -> None:
    print(f"{sha1sum(data)}  {filename}")

def main(args: List[str]) -> None:
    if not args:
        args = ["-"]
    for arg in args:
        if arg == "-":
            output_sha1sum(process_stdin(), "-")
        else:
            output_sha1sum(process_file(arg), arg)

if __name__ == "__main__":
    main(sys.argv[1:])