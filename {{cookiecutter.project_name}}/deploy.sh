#!/usr/bin/env bash
echo 开始部署项目...
git pull
sleep 1
export {{cookiecutter.project_name}}_CONFIG=production
echo ${{cookiecutter.project_name}}_CONFIG
code_dir=$(pwd)
echo ${code_dir}
kill -9 `ps -ef|grep {{cookiecutter.project_name}} | grep -v "grep"|awk '{print   $2}'`
sleep 1
source ../venv/{{cookiecutter.project_name}}/bin/activate
python3 manage.py db migrate
python3 manage.py db upgrade
nohup gunicorn run:{{cookiecutter.project_name}} -c gunicorn.conf.py >nohup.out 2>&1 &
echo 服务已经启动