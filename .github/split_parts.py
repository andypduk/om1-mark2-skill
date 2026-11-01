import hashlib
import os

# Split the assembled guide into the five sequential parts, preserving bytes
# exactly. Concatenating the parts in order reproduces om1-mark2.md byte for byte.
raw = open('om1-mark2.md', encoding='utf-8').read()
lines = raw.split('\n')
cuts = [107, 284, 562, 795]

prev = 0
parts = []
for c in cuts + [len(lines)]:
    seg = '\n'.join(lines[prev:c])
    if c < len(lines):
        seg += '\n'
    parts.append(seg)
    prev = c

assert ''.join(parts) == raw, 'part split is not byte-exact'

os.makedirs('parts', exist_ok=True)
for i, p in enumerate(parts, 1):
    path = f'parts/part-{i:02d}.md'
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(p)
    blob = hashlib.sha1(b'blob %d\0' % len(p.encode()) + p.encode()).hexdigest()
    print(f'{path} {len(p)} bytes blob={blob}')
