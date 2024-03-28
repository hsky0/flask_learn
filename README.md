# Flask学习

## 准备
- 安装虚拟环境：python3 -m venv venv

- 激活虚拟环境：source venv/bin/activate

- 安装Flask；pip install flask

- 开启debug模式：flask --app app run --debug

- 修改host：flask run --host=0.0.0.0

- 修改端口号：flask run --host=0.0.0.0 --port=8000

## 安装mysql数据库
### Windowns环境
- 官网下载mysql的安装包
- 下载完成后右键点击属性”--“兼容性”--“更改所有用户的设置”--“以兼容模式运行这个程序”--“确定”--“确定”  
- 接着就可以双击安装程序进行安装，会弹出一个提示，大概意思是“可选的 MySQL 安装程序升级可用”，可以不用管，直接选择“No”  
- 


### Linux环境（ubuntu）
- 安装mysql：apt-get install mysql
- 启动mysql：systemctl start mysql
- 关闭mysql: systemctl stop mysql
- 查看mysql状态：systemctl status mysql

- 设置mysql(version 8)的root密码:
  - 进入mysql：sudo mysql
  - 更新用户字段：update user set authentication_string='' where user='root';
  - 修改密码：ALTER user 'root'@'localhost' IDENTIFIED BY 'root'; 这里root为密码
  - 若遇到问题，输入命令：flush privileges;



## 使用数据库
- 安装数据库驱动
  - pip install pymysql
  - pip install flask-sqlalchemy

- 连接mysql

create user root@'%' identified by 'htl';

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'htl' WITH GRANT OPTION;

update user set plugin='mysq1_native_password' where user='root'; #修改其密码格式select user, plugin from user;#查询其用户
select user, plugin from user;


flush privileges;

alter user 'root'@'localhost' identified by 'htl';
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'htl';
host     = localhost
user     = debian-sys-maint
password = lu9Z1BYuphIxE0Pp


ALTER user 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'htl';
