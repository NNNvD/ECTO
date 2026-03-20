from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = REPO_ROOT / "docs" / "versions.json"
VERSION_PATTERN = re.compile(r"^### Version\s+(.+?)\s*$")


def load_config(path: Path) -> dict[str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    docs = data.get("documents", {})
    if not isinstance(docs, dict):
        raise ValueError("'documents' must be an object in docs/versions.json")
    return {str(k): str(v) for k, v in docs.items()}


def save_config(path: Path, documents: dict[str, str]) -> None:
    payload = {"documents": dict(sorted(documents.items()))}
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def update_version_line(doc_path: Path, version: str) -> bool:
    lines = doc_path.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise ValueError(f"Document is empty: {doc_path}")

    version_line = f"### Version {version}"

    if len(lines) > 1 and VERSION_PATTERN.match(lines[1]):
        changed = lines[1] != version_line
        lines[1] = version_line
    else:
        lines.insert(1, version_line)
        changed = True

    if changed:
        doc_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return changed


def cmd_sync(config_path: Path) -> int:
    documents = load_config(config_path)
    changed = 0
    for relative_path, version in documents.items():
        doc_path = REPO_ROOT / "docs" / relative_path
        if update_version_line(doc_path, version):
            changed += 1
            print(f"updated {relative_path} -> {version}")
        else:
            print(f"ok      {relative_path} -> {version}")
    print(f"\nSynced {len(documents)} documents ({changed} changed).")
    return 0


def cmd_set(config_path: Path, doc: str, version: str) -> int:
    documents = load_config(config_path)
    documents[doc] = version
    save_config(config_path, documents)
    print(f"set {doc} -> {version}")
    return cmd_sync(config_path)


def cmd_list(config_path: Path) -> int:
    documents = load_config(config_path)
    for doc, version in sorted(documents.items()):
        print(f"{doc}: {version}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Single-source version management for docs/*.md files."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help="Path to version config JSON (default: docs/versions.json)",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("sync", help="Sync version headings into docs files.")

    set_parser = subparsers.add_parser(
        "set", help="Update one document version and sync all docs."
    )
    set_parser.add_argument("doc", help="Document name relative to docs/ (e.g., projectDescription.md)")
    set_parser.add_argument("version", help="Version string (e.g., 1.0.3)")

    subparsers.add_parser("list", help="List tracked document versions.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    config_path = args.config

    if args.command == "sync":
        return cmd_sync(config_path)
    if args.command == "set":
        return cmd_set(config_path, args.doc, args.version)
    if args.command == "list":
        return cmd_list(config_path)
    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
