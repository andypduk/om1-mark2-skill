#!/usr/bin/env bash
# Reassemble the guide from its parts.
set -euo pipefail
cd "$(dirname "$0")"
cat parts/part-01.md parts/part-02.md parts/part-03.md parts/part-04.md parts/part-05.md > om1-mark2.md
echo "built om1-mark2.md ($(wc -c < om1-mark2.md) bytes)"
