# 配置和执行数据脱敏  
更新时间：2025-06-10 13:28:07  

**重要** 本文中含有需要您注意的重要提示信息，忽略该信息可能对您的业务造成影响，请务必仔细阅读。  

数据安全中心DSC（Data Security Center）支持静态脱敏和动态脱敏。静态脱敏通过创建脱敏任务，指定目标数据资产，并依据脱敏规则匹配目标敏感字段，采用脱敏算法（如遮盖、加密或替换等）对指定字段进行处理，最终将脱敏后的数据保存至用户选择的目标位置。而动态脱敏则是通过调用ExecDatamask接口，依照脱敏规则对JSON格式数据中指定字段进行数据脱敏处理。  

## **选择脱敏方式**  

**脱敏方式**| **支持脱敏的数据源**| **应用场景**| **操作方式**  
---|---|---|---  
静态脱敏| * RDS表、PolarDB-X表、MaxCompute表、PolarDB表、OceanBase表、AnalyticDB-MySQL表、ECS自建数据库表。 * OSS Bucket中结构化TXT、CSV、XLSX和XLS格式文件。 * 本地计算机保存的结构化TXT、CSV、XLSX和XLS格式文件。 | 需要将目标数据源与其他用户共享，但不能泄露某些敏感字段数据的业务场景。使用静态脱敏方式，脱敏指定数据表或文件后，可将脱敏后数据另存到其他数据表或文件中，实现数据共享，且不会影响原始的数据。| 在DSC控制台，通过新增脱敏任务，设置脱敏数据、脱敏规则、脱敏后数据保存的目的地、执行任务周期等。  
动态脱敏| 自行构造符合以下JSON格式的数据，其中dataHeaderList定义数据的列名，dataList定义脱敏的数据，dataHeaderList中列名顺序和dataList中数据顺序必须一一对应。ruleList用于匹配脱敏规则，详细说明，请参见[ExecDatamask - 对数据进行动态脱敏](https://help.aliyun.com/zh/dsc/data-security-center/developer-reference/api-sddp-2019-01-03-execdatamask#main-107864)。  
```json
{
  "dataHeaderList": ["name", "age"],
  "dataList": [
    ["lily", 18],
    ["lucy", 17]
  ],
  "ruleList": [1002, null]
}
```  
| 脱敏方式更加灵活，可由您自行构造待脱敏的数据源。| 通过OpenAPI在线调试、阿里云SDK或自定义封装API的调用方式，调用接口[ExecDatamask - 对数据进行动态脱敏](https://help.aliyun.com/zh/dsc/data-security-center/developer-reference/api-sddp-2019-01-03-execdatamask#main-107864)进行开发与部署。具体内容，请参见[集成概览](https://help.aliyun.com/zh/dsc/data-security-center/developer-reference/integration-overview)。  

## 脱敏结果示例  
DSC提供的脱敏算法包含哈希脱敏、遮盖脱敏、替换脱敏、变换脱敏、加密脱敏和洗牌脱敏。不同脱敏算法脱敏后示例如下。  

**适用类型和典型场景**| **算法描述**| **算法配置示例**| **脱敏前数据示例**| **脱敏结果示例**  
---|---|---|---|---  
不可逆算法。支持常见的哈希算法，并支持偏移量（加盐值）配置。适用于密码或需要通过对比进行敏感数据确认的场景。 * 敏感类型：密钥类。 * 适用场景：数据存储。 | MD5| 加盐值为`测试`| 123456| d6f82c64df3dc34921d79e5f22e5d43a  

## 计费说明  
目前，仅**企业版** DSC实例支持使用数据脱敏功能。购买企业版实例后，即可使用数据脱敏功能。DSC采用包年包月模式计费，详细说明，请参见[计费概述](https://help.aliyun.com/zh/dsc/data-security-center/product-overview/overview)。使用静态脱敏时可能会包含额外计费。  

**脱敏方式**| **数据源**| **DSC 侧计费**| **额外计费**  
---|---|---|---  
静态脱敏| * RDS表、PolarDB-X表、MaxCompute表、PolarDB表、OceanBase表、AnalyticDB-MySQL表、ECS自建数据库表。 * OSS Bucket中结构化TXT、CSV、XLSX和XLS格式文件。 | 待脱敏数据资产需要授权接入DSC，会抵扣购买的**数据库防护实例数** 和**存储防护容量** 。| 如果您需要脱敏的云产品使用的是按量付费的方式，对应云产品会按照访问或写入数据量收取相应的费用。  

## 开通服务  
* 如果您当前账号未开通过DSC服务或仅开通免费版服务，您可以先开通7天免费试用的企业版实例或直接购买企业版DSC实例。具体内容，请参见[开通7天试用版](https://help.aliyun.com/zh/dsc/data-security-center/product-overview/apply-for-a-7-day-free-trial)和[购买数据安全中心](https://help.aliyun.com/zh/dsc/data-security-center/user-guide/purchase-dsc)。  
* 如果您已开通DSC免费版服务但不是企业版实例，您需要升级版本才能使用数据脱敏功能。升级操作，请参见[包年包月实例变配](https://help.aliyun.com/zh/dsc/data-security-center/product-overview/dsc-upgrade)。  

**重要** 如果使用**静态脱敏** ，相关数据资产需要先授权接入DSC，您需要确保已购买足够可用的数据库防护实例数和OSS防护量。  

## 静态脱敏  

### **功能说明**  
创建静态脱敏任务时，可以选择**已配置** 的**脱敏模板** 作为任务的**脱敏规则** ，也可以直接设置**目标敏感字段** 的**脱敏算法** 作为任务的**脱敏规则** 。脱敏模板配置，请参见[配置脱敏模板和算法](https://help.aliyun.com/zh/dsc/data-security-center/user-guide/configure-de-identification-templates-and-algorithms)。  

### 前提条件  
如果使用静态脱敏方式脱敏数据库或OSS文件，需要已完成DSC授权和接入待脱敏数据资产。具体操作，请参见：  
* [RDS表、PolarDB-X表、PolarDB表、OceanBase表、AnalyticDB-MySQL表的授权接入](https://help.aliyun.com/zh/dsc/data-security-center/user-guide/connect-to-database-instances)。  
* [MaxCompute数据的授权接入](https://help.aliyun.com/zh/dsc/data-security-center/user-guide/maxcompute-authorization)。  
* [ECS自建数据库的授权接入](https://help.aliyun.com/zh/dsc/data-security-center/user-guide/ecs-user-created-database-authorization)。  
* [OSS Bucket的授权接入](https://help.aliyun.com/zh/dsc/data-security-center/user-guide/unstructured-data-oss-authorization)。  

**重要** 如果需要将脱敏后数据存储到RDS表、PolarDB-X表、MaxCompute表、PolarDB表、OceanBase表、AnalyticDB-MySQL表、自建数据库表或OSS Bucket中，DSC必须授权接入目标数据资产，且使用具有读写权限的账号连接目标数据资产。对于RDS、PolarDB-X、PolarDB、OceanBase或AnalyticDB-MySQL数据库，需要选择账密连接方式接入DSC。  

### 新增脱敏任务  

**警告** 如果您在生产环境中直接对数据进行脱敏，数据库的性能可能会有所下降。  

通过新增脱敏任务，指定数据脱敏的范围和规则。  

1. 登录[数据安全中心控制台](https://yundun.console.aliyun.com/?p=sddp#/overview)。  
2. 在左侧导航栏，选择**风险治理** > **数据脱敏** 。  
3. 在**静态脱敏** 页签的**任务配置** 页签，单击**新增脱敏任务** 。  
4. 根据页面导航，完成数据脱敏任务配置。  

### **执行和查看脱敏任务**  
如果脱敏任务触发方式是**仅人工** ，必须手动启动脱敏任务。如果脱敏任务触发方式是**仅定时触发** ，仅支持通过设置的时间点定时自动启动脱敏任务。如果脱敏任务触发方式是**人工+定时触发** ，支持手动和自动启动脱敏任务。  

1. 在**静态脱敏** 页签的**任务配置** 页签，单击新创建的脱敏任务**操作** 列的**启动** ，执行脱敏任务。  
2. 在**静态脱敏** 页签，单击**任务状态** 子页签，查看脱敏任务的执行进度和状态。  

### 脱敏任务执行失败排查  
脱敏任务执行失败后，参考以下内容查看失败原因。  

**执行失败错误提示**| **错误原因**  
---|---  
找不到脱敏任务，有可能是因为任务已经被删除或者关闭| 脱敏任务可能被删除或被关闭（脱敏任务**操作** 列下的开关为关闭状态）。  

### 修改、删除脱敏任务  
等待执行或执行中的脱敏任务不支持修改或删除。  

* 修改脱敏任务  
需要调整脱敏任务的配置时，您可以单击目标脱敏任务**操作** 列的**修改** ，修改脱敏任务。  
* 删除脱敏任务  
**重要** 脱敏任务删除后不支持恢复，建议您谨慎操作。  
不再需要指定脱敏任务时，您可以单击目标脱敏任务**操作** 列的**删除** ，并在提示对话框中单击**确定** 。  

## 动态脱敏  

### **功能说明**  
动态脱敏任务必须依赖**已配置** 的**脱敏模板** 作为脱敏规则，对指定数据进行脱敏。您可以调用[ExecDatamask](https://help.aliyun.com/zh/dsc/data-security-center/developer-reference/api-sddp-2019-01-03-execdatamask#main-107864)接口，传入待脱敏数据（**Data** ）和脱敏模板ID（**TemplateId** ），然后按照**脱敏模板** 的**匹配方式** （**字段名称** 、**敏感类型** ），对**Data** 中**dataList** 的数据进行脱敏。  

### 使用限制  
您调用ExecDatamask接口对指定数据进行动态脱敏时，每次脱敏的数据（**Data** ）必须小于2 MB。  

### 查看动态脱敏接口调用记录  
1. 登录[数据安全中心控制台](https://yundun.console.aliyun.com/?p=sddp#/overview)。  
2. 在左侧导航栏，选择**风险治理** > **数据脱敏** 。  
3. 在**数据脱敏** 页面，单击**动态脱敏** 页签。  
4. 在**动态脱敏** 页面，查看ExecDatamask接口的调用记录。  

**说明** 如果您在调用接口时使用了相同的账号和IP地址，即使多次调用接口，操作记录只会保留一条，并记录**累计调用次数** 。  

## **使用静态脱敏实现数据共享示例**  
使用静态脱敏对某账号下源OSS Bucket中的结构化CSV格式文件中的敏感数据进行脱敏，然后将脱敏后的文件保存到同账号下的目标OSS Bucket，分享目标OSS Bucket给指定用户，实现数据的安全共享。具体操作，请参见[对OSS表格文件中的敏感数据进行脱敏](https://help.aliyun.com/zh/dsc/data-security-center/use-cases/oss-sensitive-data-desensitization)。