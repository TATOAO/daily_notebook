
# jekyll build precommit example

cd .git/hooks

touch pre-commit
chmod +x pre-commit

```bash
#!/bin/sh

echo "Running Jekyll build..."
jekyll build
if [ $? -ne 0 ]; then
    echo "Jekyll build failed. Aborting commit."
    exit 1
fi

git add .
echo "Jekyll build succeeded. Proceeding with commit."
```
