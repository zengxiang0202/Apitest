1.allure报告报错。

![4b494385fa45a477260952b64606d0c](https://github.com/user-attachments/assets/731ee6e5-8569-49ee-8c3a-6b99afbc19a9)
![c100dbbbf4a11eb9d89c37cdf15b3dc](https://github.com/user-attachments/assets/db028f12-8e78-41ab-a03c-f06b34eb37a7)
解决点是在 os.system 命令中用双引号包裹 {report_path} 变量，确保整个路径被视为一个字符串。因为打印了report_path路径是D:\Program Files\Delivery_System-master\outFiles\report\temp。虽然看似合理但问题就出在Program Files这两个单词有空格了
命令行会将其解析为：
allure serve D:\Program和Files\Delivery_System-master\outFiles\report\temp
因此，命令会失败。修改之后，allure报告能成功打开。
![506acd423550d6f7dce8dc3a287f085](https://github.com/user-attachments/assets/93217d58-4d1f-488e-bab1-79cf5d4ff56a)

2.安装完Jenkins启动时遇到的一些报错
2.1启动失败（Job for jenkins.service failed because the control process exited with error code. See "systemctl status jenkins.service" and "journalctl -xe" for details.）
打印了日志没有发现error，考虑是不是jdk配置的有什么问题？
[root@localhost ~]# update-alternatives --config java
   1           java-1.7.0-openjdk.x86_64 (/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.261-2.6.22.2.el7_8.x86_64/jre/bin/java)
*+ 2           java-1.8.0-openjdk.x86_64 (/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.262.b10-1.el7.x86_64/jre/bin/java)
发现这里没有显示我的jdk11信息，既然安装了 JDK 11，你需要将它添加到 update-alternatives 系统中
sudo update-alternatives --install /usr/bin/java java /usr/local/jdk-11.0.09/bin/java 1100
sudo update-alternatives --install /usr/bin/javac javac /usr/local/jdk-11.0.09/bin/javac 1100
并设为默认java版本
sudo update-alternatives --config java
sudo update-alternatives --config javac
再restart一下Jenkins，2.1问题解决但是却又一直卡在启动界面。
2.2Jenkins启动成功，打开浏览器卡在初始界面（please wait while Jenkins。。。）
![8e15e17a78da8a6f333c92ee0ab316e](https://github.com/user-attachments/assets/73cfdebd-830c-4386-b5d6-46ea7bedc9d1)
在csdn上搜索得知应该是Jenkins本地的源不稳定换一下国内的
vim /var/lib/jenkins/hudson.model.UpdateCenter.xml，把url换成https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json，保存退出再systemctl restart jenkins，成功进入Jenkins界面。
![7684b2366f07315c34431269b187ac1](https://github.com/user-attachments/assets/65045d13-185d-4f06-8a61-b6c4283a7535)

