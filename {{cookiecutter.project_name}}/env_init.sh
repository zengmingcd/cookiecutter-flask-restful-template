#!/usr/bin/env bash
echo "开始初始化项目空间，这需要一些时间，请耐心等待。"
mkdir logs
code_dir=$(pwd)
cd ..
mkdir venv
cd venv
virtualenv -p python3 --no-site-packages ./{{cookiecutter.project_name}}
source {{cookiecutter.project_name}}/bin/activate || { echo "source error"; exit 1; }
cd ${code_dir}
pip3 install -r requirements.txt
echo 初始化完毕.
