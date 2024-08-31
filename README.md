# （一个很酷的中文名）: CSGO

简介放在这里

# 部署

## 前置需求

- 现代 GNU/Linux 发行版 
  - 推荐：
    - Ubuntu 20.04 +
    - Debian 12
  - 不建议使用 CentOS 
- Python 3.10 
  - 暂不支持其他（更高或更低）版本
  - 可通过 conda 获取 Python 3.10 环境
- pip >= 19.3


## 安装依赖

### 使用系统自带 Python 3.10 环境

```bash
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 使用 Conda 构建 Python 3.10 环境

```bash
conda create -n sf python=3.10
conda activate sf
pip install -r requirements.txt
```

## 启动 Ray 集群

```bash
ray start --head --node-ip-address="ip" --port="port" --include-dashboard=False --disable-usage-stats
```

其中 `"ip"` 与 `"port"` 分别为此处 Ray 需要监听的 IP 地址与端口。

输出中显示 `"Ray runtime started."`，则说明Ray的主节点启动成功。

## 配置

### 修改 config.py

以下是一个两方部署时，`config.py` 的示例：

```python
cluster_config ={
    'parties': {
        'alice': {
            'address': 'ip:port',
            'listen_addr': '0.0.0.0:port'
        },
        'bob': {
            'address': 'ip:port',
            'listen_addr': '0.0.0.0:port'
        }, # 若有多于 2 方参与，则以此类推增加 party
    },
    'self_party': 'bob' # 将这里的 self_party 改为当前正在部署一方的 party
    # 如当前正在部署 'alice' 方，则将这里改为 'alice'，以此类推
}
```

# 使用

## 数据规范

此项目接受两种数据格式

这里写一下 orders 和 count 两种格式分别长啥样

然后往根目录下放几个示例

## 功能

### 生成测试数据

### 隐私求交

### 联邦学习

### 生成建议的授信额度
