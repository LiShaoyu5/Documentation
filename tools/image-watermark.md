# 图片水印

> 更新时间：2025-08-14

图片水印可以帮助您保护企业图片的版权、防止图片泄露等。在使用图片水印时，您需要将图片水印SDK嵌入到业务系统，或使用网页端的图片水印服务，给图片添加水印。在发生信息泄露时，可以通过水印信息定位出泄露人员。本文介绍如何使用图片水印功能。

当前支持在图片上嵌入明水印和暗水印。

* 如果嵌入的是明水印，可以直接在图片上看到明水印信息，定位泄露人员。
* 如果嵌入的是暗水印，无法通过肉眼直接看到暗水印信息，所以您需要在通过SDK或网页端的图片水印服务提取暗水印信息，然后定位出泄露人员。


## **在业务系统中嵌入图片水印 SDK**

### **操作准备**

已存在一台基于X86架构的Linux服务器。该服务器用于部署图片水印SDK。

### **步骤一：下载图片水印 SDK**

1. 登录办公安全平台控制台。
2. 在左侧导航栏，选择**数字水印服务** > **嵌入服务**。
3. 在**嵌入服务**页面，单击图片水印**操作**列**下载 SDK**。
将图片水印压缩包下载到本地。当前只支持Java语言。

下载的SDK压缩包中包含如下内容：

* watermark-normalimage-v1.0.12.jar：集成水印的SDK包，需要添加到Maven仓库。
* normalImageLinuxDemo：水印的Demo，您可以通过Demo进行体验。

4. 单击**AK/SK信息**列的图标，复制AK和SK信息并保存到本地。

### **步骤二：集成 SDK**

1. 添加jar包依赖（maven）。

2. 接口调用。

1. 初始化接口。

2. 图片添加水印到目标文件。

3. 图片添加水印到字节数组。

### **错误码**

**错误码**| **描述**
---|---
null_parameters| 存在为空的参数
wrong_parameters| embed错误参数
jvm_error| embed java虚拟机错误
jni_exception| JNI初始化出错（Office03版水印特有的错误），需检查POI引用是否冲突/出错、JDK版本、系统环境
wrong_fileFormat| 文件格式错误
imgDecodeError| 图片解码错误
imgSizeError| 图片大小错误
embedException| 嵌入过程出现异常
embedExceptionUnKnow| 嵌入未知错误
invalid_carrier| 不合法的载体或参数有误
embed_success| 嵌入成功
extract_success| 提取成功
extract_fail| 提取失败
extract_id_exceed| 提取
extract_exception| 提取异常
ossp_error_code_success| SDK功能执行正常
ossp_error_code_invalid_param| SDK加载使用了无效参数
ossp_error_code_fail_to_download_config| SDK下载配置失败
ossp_error_code_fail_to_read_config| SDK读取配置失败
ossp_error_code_invalid_config| SDK无效配置
ossp_error_code_unauthorized_device| 未授权设备
ossp_error_code_liscence_expired| 许可证过期
ossp_error_code_config_mismatch| SDK配置不匹配
ossp_error_code_unauthorized_api| SDK功能接口未授权
ossp_error_code_invalid_session_id| SDK无效sessionId
ossp_error_code_api_not_implemented| SDK调用接口未实现
ossp_error_code_unknown| SDK未知错误

## 提取暗水印信息

已获取嵌入暗水印信息的外泄图片。

### **步骤一：创建提取任务**

1. 登录办公安全平台控制台。
2. 在左侧导航栏，选择**数字水印服务** > **提取服务**。
3. 单击**创建提取任务**，在**创建提取服务**面板，参考如下说明配置提取文件。

**配置项**| **说明**
---|---
水印版本| 根据购买的水印版本选择。
水印类型| 选择图片水印。
嵌入水印信息位宽| 设置水印信息的位宽，位宽需要与透明水印底图的SDK位宽（默认为32位）保持一致。
上传待提取水印文件| 根据界面提示，上传获取到的泄露文件。

4. 单击**确定**。

创建成功后，会在提取服务页面显示创建的任务信息。

### **步骤二：查看提取结果**

水印任务创建完成，待提取成功后，查看提取结果，获取暗水印原文。

1. 在**提取服务**页面，单击**提取信息**列**展示**。
2. 在展开的信息中，您可以提取到暗水印原文（十进制数字）。

## **溯源定位泄露人员**

将提取的暗水印原文和您业务中使用的映射服务或者自定义的映射表进行对应，从而定位出具体的泄露人员。

例如，您提取的暗水印原文是123456，映射表中123456对应的是张三，则定位出泄露人员是员工张三。

## 相关文档

* 关于数字水印产品应用场景、产品能力、产品架构、购买渠道等内容。
* 如果您需要查看其他类型的水印服务。