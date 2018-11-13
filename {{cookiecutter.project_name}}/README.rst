==============================
{{cookiecutter.project_name}}
==============================

{{cookiecutter.project_description}}

项目成员
--------
- {{cookiecutter.author}}  <{{cookiecutter.email}}>

功能
-----
- TODO

本地环境
--------
- 命令行进入项目所在文件夹

::

 cd {{cookiecutter.project_name}}

- 执行初始化脚本

::

 bash ./env_init.sh

- 在你熟悉的IDE中打开，例如PyCharm

部署
-----
命令行进入项目所在文件夹

::

 cd {{cookiecutter.project_name}}

- 第一次部署时，执行初始化脚本

::

 bash ./env_init.sh

- 执行部署脚本

::

 bash ./deploy.sh
