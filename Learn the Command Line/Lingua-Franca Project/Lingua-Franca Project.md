# Task Group 1: Navigating the File System

### Task 1
cd ~/Downloads/lingua-franca-project/lingua-franca/

### Task 2
pwd

### Task 3
ls

### Task 4
mkdir world/

### Task 5
touch world/esperanto.txt
ls world/

# Task Group 2: Viewing and Changing the File System

### Task 6
ls -alt
Which directory would appear first?
The world directory

### Task 7
ls europe/
mv europe/chinese.txt asia/

### Task 8
cp spanish.txt europe/
cp spanish.txt northamerica/
cp spanish.txt southamerica/
rm spanish.txt

### Task 9
ls todo/*

### Task 10
cp todo/africa/* africa/
cp todo/asia/* asia/
cp todo/europe/* europe/

### Task 11
rm -r todo/*

# Task Group 3: Redirecting Input and Output

### Task 12
ls asia/ > todo/asian_language_files.txt

### Task 13
echo Welkom by die Lingua Franca vertaaldienste. > africa/afrikaans.txt

### Task 14
wc -l */*.txt | grep 0 > todo/empty_files.txt

### Task 15
cat todo/empty_files.txt

### Task 16
grep -Rl 'Lingua-Franca' */*.txt | wc -l
sed -i 's/Lingua-Franca/Lingua Franca/g' */*.txt

# Task Group 4: Configuring the Environment

### Task 17
nano .bash_profile

### Task 18
echo Welcome!

### Task 19
source .bash_profile

### Task 20
alias md='mkdir'
alias d='date'
alias hy='history'

### Task 21
source .bash_profile

### Task 22
md translations/
ls translations/
d
hy

### Task 23
Desde nano:
export PS1='> '

Desde Bash:
echo "export PS1='> '" >> .bash_profile

### Task 24
source .bash_profile

### Task 25
md folder/
ls folder/
d
hy

### Task 26
env
