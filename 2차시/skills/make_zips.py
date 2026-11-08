"""각 스킬 폴더를 claude.ai 업로드용 zip으로 묶는다.
구조: <name>.zip 안에 <name>/SKILL.md (+ 보조 파일). 폴더명 = frontmatter name.
실행: python3 make_zips.py
"""
import os, re, zipfile, sys
base = os.path.dirname(os.path.abspath(__file__))
for d in sorted(os.listdir(base)):
    p = os.path.join(base, d)
    if not os.path.isdir(p) or not os.path.exists(os.path.join(p, "SKILL.md")):
        continue
    fm = open(os.path.join(p, "SKILL.md"), encoding="utf-8").read().split("---")[1]
    name = re.search(r"^name:\s*(\S+)", fm, re.M).group(1)
    if name != d:
        sys.exit(f"폴더명 {d} != name {name}")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name) or "anthropic" in name or "claude" in name:
        sys.exit(f"name 규칙 위반: {name}")
    desc = re.search(r"^description:\s*(.+)$", fm, re.M).group(1)
    print(f"{name}: description {len(desc)}자")
    out = os.path.join(base, f"{name}.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(p):
            for f in files:
                if f.startswith("."):
                    continue
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, base))
    print("  ->", os.path.basename(out))
