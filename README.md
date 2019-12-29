# Easy-BNU-Connector 0.1.0

连接北京师范大学校园网的Python程序

methods.py 是由 methods.js 通过 Js2Py 转换成的，methods.js 取自认证网关

程序运行不需有 methods.js

不支持 Linux


十分感谢 YooungJune 的测试


# 更新

现在可以双击 setup.cmd 进行安装

安装时，setup.cmd、setup.py 和文件夹 easy_bnu_connector 应在同一目录下

安装时，若未安装所需模块，需根据命令行提示确认安装

若 setup.cmd、setup.py 和文件夹 easy_bnu_connector 全部消失，出现Easy-BNU-Connector.cmd，说明安装成功

否则安装失败，可检查是否连接网络后再次运行 setup.cmd 进行安装


# 未来计划:

添加详尽的Docstring

使 Easy-BNU-Connector.cmd 运行时不出现 CMD 界面

开机自启

自动打开WLAN开关

禁止浏览器自动跳出登录界面

添加注销、自助服务功能

添加用户名错误、密码错误的提示

跨平台

……


# 不予考虑:

采用严重不符合规范的代码

不使用认证网关内的JavaScript和由认证网关内的JavaScript转换成的Python程序

