TIME_STAMP=$(date +%Y-%m-%d_%H:%M:%S)

commit_if_modified() {
    local message="$1"
    shift
    local files=("$@")

    git add "${files[@]}"
    if ! git diff --cached --quiet -- "${files[@]}"; then
        git commit -m "$message"
    fi
}

commit_if_modified "[pipeline.sh-$TIME_STAMP] Updated tests/test_visual_lankadata.data.json" \
    tests/test_visual_lankadata.data.json

rm -rf images
python3 -m pytest -x -v -p no:warnings "$*"
commit_if_modified "[pipeline.sh-$TIME_STAMP] Updated images" images

python3 workflows/readme_build.py
commit_if_modified "[pipeline.sh-$TIME_STAMP] Updated README.md" README.md