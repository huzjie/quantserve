# -*- coding: utf-8 -*-
"""Minimal YAML subset parser (stdlib-only).

Supports the common config shapes QuantServe needs: nested mappings via
indentation, block lists via "- ", inline lists "[a, b]", scalars (str/int/
float/bool/null), comments, and quoted strings.  Not a full YAML parser —
use PyYAML if you need the full spec (auto-detected and preferred).
"""
from __future__ import annotations

import re


class MiniYAMLError(Exception):
    pass


def _strip_comment(line: str) -> str:
    in_s = in_d = False
    for i, ch in enumerate(line):
        if ch == "'" and not in_d:
            in_s = not in_s
        elif ch == '"' and not in_s:
            in_d = not in_d
        elif ch == "#" and not in_s and not in_d:
            return line[:i]
    return line


def _scalar(v: str):
    v = v.strip()
    if v == "" or v == "~" or v.lower() == "null":
        return None
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    low = v.lower()
    if low in ("true", "false"):
        return low == "true"
    if re.fullmatch(r"[-+]?\d+", v):
        return int(v)
    if re.fullmatch(r"[-+]?\d*\.\d+([eE][-+]?\d+)?", v):
        return float(v)
    return v


def _parse_inline_list(v: str):
    v = v.strip()
    if not (v.startswith("[") and v.endswith("]")):
        return None
    inner = v[1:-1].strip()
    if not inner:
        return []
    out = []
    buf = ""
    depth = 0
    for ch in inner:
        if ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(_scalar(buf))
            buf = ""
        else:
            buf += ch
    if buf.strip():
        out.append(_scalar(buf))
    return out


def load(text: str):
    """Parse a YAML subset string into Python objects."""
    lines = [l for l in text.splitlines()]
    lines = [_strip_comment(l).rstrip() for l in lines]
    # strip leading document marker
    if lines and lines[0].strip() == "---":
        lines = lines[1:]

    root = {}
    stack = [(root, -1)]  # (mapping, indent)

    i = 0
    while i < len(lines):
        raw = lines[i]
        if not raw.strip():
            i += 1
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()
        if line.startswith("- "):
            # list item -> belongs to most recent list context
            item = line[2:].strip()
            val = _parse_inline_list(item)
            if val is None:
                val = _scalar(item.split(":", 1)[0]) if ":" in item and " " not in item[: item.index(":")].strip() else _scalar(item)
            # simplest: scalar item
            val = _scalar(item)
            stack[-1][0].append(val)
            i += 1
            continue
        if ":" in line:
            key, _, rest = line.partition(":")
            key = key.strip().strip('"').strip("'")
            rest = rest.strip()
            # pop stack to matching indent
            while len(stack) > 1 and stack[-1][1] >= indent:
                stack.pop()
            parent = stack[-1][0]
            if rest == "":
                # decide block mapping vs list by peeking next non-empty line
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                child_indent = len(lines[j]) - len(lines[j].lstrip(" ")) if j < len(lines) else indent
                if j < len(lines) and lines[j].strip().startswith("- "):
                    parent[key] = []
                    stack.append((parent[key], indent))
                else:
                    parent[key] = {}
                    stack.append((parent[key], indent))
            else:
                inline = _parse_inline_list(rest)
                parent[key] = inline if inline is not None else _scalar(rest)
        i += 1
    return root
