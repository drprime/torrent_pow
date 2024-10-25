# Torent Proof of work

## Installation

### 1. Install python3.10 with venv

```sh
sudo apt-get install python3.7-dev python3.7-venv
```

If you'll get errors like: E: Couldn’t find any package by glob ‘python3.10’ , stating that the packages can not be installed
run the following commands below, then re-run the install command above:

```sh
apt update
```

```sh
sudo apt install software-properties-common
```

```sh
sudo add-apt-repository ppa:deadsnakes/ppa
```

### 2. Find out where your python 3.10 is located by this command:

```sh
which python3.10
```
Should be something like /usr/bin/python3.10

### 3. Create Virtual Environment in the Home directory.
```sh
cd
```

```sh
mkdir virtual_env
```

```sh
/usr/bin/python3.10 -m venv ~/virtual_env/venv_310
```

```sh
source ~/virtual_env/venv_30/bin/activate
```

### 4. Install torrentp

```sh
pip install torrentp
```

### 5. Change path to .torrent file and download folder in main.py file
```
torrent_file = "breaking_bad.torrent"
download_folder = "./downloads"
```
### 6. Run script
```sh
python3 main.py
```