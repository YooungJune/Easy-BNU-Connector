# Easy-BNU-Connector 0.1.2

连接北京师范大学校园网的Python程序

methods.py 是由 methods.js 通过 Js2Py 转换成的，methods.js 取自认证网关

程序运行不需有 methods.js

不支持 Linux


十分感谢 YooungJune 的测试


# 特别公告:

程序阻止浏览器弹出网关页面，是通过强制关闭浏览器完成的。程序是通过遍历 BROWSERS 常量中的所有浏览器文件名，逐个尝试关闭，来完成任务的。但还有很多浏览器，文件名未被添加，因为不能确定它们的文件名是什么。

提供程序中未列出的正确的浏览器文件名，将被视为对本项目做出的贡献。


# 更新:

丰富了信息提示，增加了不成熟的阻止浏览器弹出网关页面的机制

现在可以双击 setup.cmd 进行安装

安装时，setup.cmd、setup.py 和文件夹 easy_bnu_connector 应在同一目录下

安装时，若未安装所需模块，需根据命令行提示确认安装

若 setup.cmd、setup.py 和文件夹 easy_bnu_connector 全部消失，出现 Easy-BNU-Connector.cmd，说明安装成功

否则安装失败，可检查是否连接网络后再次运行 setup.cmd 进行安装


# 未来计划:

添加详尽的Docstring

开机自启

完善阻止浏览器弹出网关页面的机制

添加注销、自助服务功能

进一步丰富提示信息

跨平台

……


# 不予考虑:

采用严重不符合规范的代码

不使用认证网关内的JavaScript和由认证网关内的JavaScript转换成的Python程序

