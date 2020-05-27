function create() {
    cd
    python create.py $1
    cd Downloads/myScrap/pyLab_myLab/$1
    git init
    git remote add origin https://github.com/jeff007ali/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    echo "Opening VS Code....."
    code .
}
