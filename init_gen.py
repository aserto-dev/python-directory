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
from typing import List, Tuple

Symbols = List[str]
Stubs = List[str]


@dataclass(frozen=True)
class Module:
    name: str
    symbols: Symbols
    stubs: Stubs


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
        symbols, stubs = parse_module(p)
        modules[p.parent].append(
            Module(name=parse_module_name(p, root_module), symbols=symbols, stubs=stubs)
        )

    for p, mods in modules.items():
        init = p / "__init__.py"

        with init.open("w") as f:
            f.write(generate_init(mods))


def parse_module_name(path: Path, root: str) -> str:
    parts = path.parts
    root_index = parts.index(root)
    return ".".join(parts[root_index:-1] + (path.stem,))


def parse_module(path: Path) -> Tuple[Symbols, Stubs]:
    with path.open() as f:
        tree = ast.parse(f.read())

    visitor = Visitor()
    visitor.visit(tree)

    return visitor.symbols, visitor.stubs


def generate_init(modules: List[Module]) -> str:
    lines: List[str] = [
        "# This file is generated by init_gen.py. Do not edit.",
        "",
    ]

    has_stubs = any(module.stubs for module in modules)
    if has_stubs:
        lines.append("from typing import TYPE_CHECKING")
        lines.append("")

    for module in modules:
        if module.symbols:
            lines.append(f"from {module.name} import (")
            lines.extend(f"    {symbol}," for symbol in module.symbols)
            lines.append(")")
            lines.append("")

        if module.stubs:
            lines.append("if TYPE_CHECKING:")
            lines.append(f"    from {module.name} import (")
            lines.extend(f"        {stub}," for stub in module.stubs)
            lines.append("    )")
            lines.append("")

    lines.append("__all__ = [")
    lines.extend(f'    "{symbol}",' for module in modules for symbol in module.symbols)
    lines.append("]")
    lines.append("")

    return "\n".join(lines)


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.symbols: Symbols = []
        self.stubs: Stubs = []
        self._in_const: bool = False

    def visit_ClassDef(self, node: ast.ClassDef):
        if self.is_public(node.name):
            if node.name.endswith("AsyncStub"):
                self.stubs.append(node.name)
            else:
                self.symbols.append(node.name)

    def is_public(self, name: str) -> bool:
        return not name.startswith("_")


if __name__ == "__main__":
    main()
