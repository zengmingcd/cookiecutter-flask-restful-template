#!/usr/bin/env bash
echo 初始化项目空间...
mkdir logs
code_dir=$(pwd)
cd ..
mkdir venv
cd venv
virtualenv -p python3 --no-site-packages ./{{cookiecutter.project_name}}
source {{cookiecutter.project_name}}/bin/activite
cd ${code_dir}
pip3 install -r requirements.txt
echo 初始化完毕.