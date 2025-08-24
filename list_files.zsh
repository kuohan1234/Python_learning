#!/bin/zsh

echo "\n=== Python 檔案 (.py) ==="
for file in *.py; do
    if [[ -f "$file" ]]; then
        echo "- $file"
    fi
done

echo "\n=== 非 Python 檔案 ==="
for file in *; do
    if [[ -f "$file" && "$file" != *.py ]]; then
        echo "- $file"
    fi
done
