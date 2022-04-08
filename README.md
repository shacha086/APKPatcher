# APKPatcher
这是一个使用**Github Actions**来进行自动化打包apk的工具。

**适用于：**
* 对apk的重新打包。

**不适用于：**
* 未编译的apk源码。

**使用方法：**
1. ``Fork``或``Import``本仓库。
2. 将 [Actions 脚本](https://github.com/shacha086/APKPatcher/blob/main/.github/workflows/build.yml) 中的 env 按照提示修改。
3. 在 [你的仓库地址]/settings/secrets/actions 处添加如下 secrets：
* ``ACCESS_TOKEN`` (在[个人通行证](https://github.com/settings/tokens)页面申请，必要的权限是 repo)
* ``KEYSTORE_B64`` (把你自己的签名证书 base64 处理一下，粘贴进来)
* ``KEYSTORE_PASS`` (签名密码)
* ``KEYSTORE_B64`` (签名的别名的密码)
4. 新开一个私人仓库，里面存放需要打包进apk的资源信息。
5. 将此库``clone``到本地后，在此仓库新建一个``submodule``连接刚刚创建的数据仓库，需要注意的是连接到此仓库的模块文件夹名称为打包后在 apk 内的名称。
6. 复制[这个 Actions 脚本](https://github.com/shacha086/APKPatcher/blob/assets/.github/workflows/dispatch_event.yml)到你的数据仓库并按照提示修改相关变量，这样数据仓库有新push时本仓库的自动化即可被触发。
7. **（可选）** 新开一个``release``仓库，用来存放打包后的apk。如果您决定直接在本仓库release，请将 [Actions 脚本](https://github.com/shacha086/APKPatcher/blob/main/.github/workflows/build.yml) 中的``RELEASE_REPO``设置为本仓库的地址。

**常见问题：**
Q:怎么获取签名密钥？

A:[查看链接](https://developer.android.com/studio/command-line/apksigner)。

Q:怎么生成base64？

A:[查看链接](https://base64.supfree.net/)。

Q:为什么要这么做？

A:因为签名密钥中有大量不可见和非法字符，直接粘贴到``secret``里面是用不了的。

Q:那为什么不直接把签名文件上传到仓库？

A:因为**安全性考虑**。如果你这个仓库是公开的，而你直接上传了密钥的话，那你可以考虑换个密钥了。

文档待补充
