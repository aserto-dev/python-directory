#!/usr/bin/env python3
"""
Generate __init__.py files for grpc bindings.
"""

import argparse
import ast
import os
import sys
from collections import defaultdict as ddict
from dataclasses import dataclass
from pathlib import Path
from typing import List

Symbols = List[str]


@dataclass(frozen=True)
class Module:
    name: str
    symbols: Symbols


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", help="Root path")

    args = parser.parse_args()

    path = Path(args.root)
    if not path.exists():
        print(f"Path {path} does not exist", file=sys.stderr)

    root_module = os.path.basename(args.root.rstrip(os.sep))

    modules: ddict[Path, List[Module]] = ddict(list)
    for p in path.glob("**/*.pyi"):
        modules[p.parent].append(
            Module(name=parse_module_name(p, root_module), symbols=parse_module(p))
        )

    for p, mods in modules.items():
        init = p / "__init__.py"

        with init.open("w") as f:
            f.write(generate_init(mods))


def parse_module_name(path: Path, root: str) -> str:
    parts = path.parts
    root_index = parts.index(root)
    return ".".join(parts[root_index:-1] + (path.stem,))


def parse_module(path: Path) -> Symbols:
    with path.open() as f:
        tree = ast.parse(f.read())

    visitor = Visitor()
    visitor.visit(tree)

    return visitor.symbols


def generate_init(modules: List[Module]) -> str:
    lines: List[str] = [
        "# This file is generated by init_gen.py. Do not edit.",
        "",
    ]

    for module in modules:
        if not module.symbols:
            continue

        lines.append(f"from {module.name} import (")
        lines.extend(f"    {symbol}," for symbol in module.symbols)
        lines.append(")")
        lines.append("")

    lines.append("__all__ = [")
    lines.extend(f'    "{symbol}",' for module in modules for symbol in module.symbols)
    lines.append("]")

    return "\n".join(lines)


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.symbols: Symbols = []
        self._in_const: bool = False

    def visit_ClassDef(self, node: ast.ClassDef):
        if self.is_public(node.name):
            self.symbols.append(node.name)

    def is_public(self, name: str) -> bool:
        return not name.startswith("_")


if __name__ == "__main__":
    main()
