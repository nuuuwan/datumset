TIME_STAMP=$(date +%Y-%m-%d_%H:%M:%S)
rm -rf images
python3 -m pytest -x -v -p no:warnings "$*";
git add images
git commit -m "[pipeline.sh-$TIME_STAMP] Updated images";

python3 workflows/readme_build.py;
git add README.md
git commit -m "[pipeline.sh-$TIME_STAMP] Updated README.md";