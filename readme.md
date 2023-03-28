# POTIONX

```markdown
一款基于 FastAPI 编写的脚手架
```

## 0x01. TechStack
```markdown
0. HTTPS
1. FastAPI
2. Sqlalchemy && MySQL && PostgreSQL && Redis
3. Pydantic
4. DynaConf
5. Loguru
6. Guvicorn && Uvicorn
```


## 0x02. 目录结构
```markdown
.
├── app
│   ├── constant            # 常量
│   ├── db                  # 数据库连接即进行 CRUD 前的前置操作
│   ├── handler             # 路由层
│   │   └── v1              # v0 v1 v2...
│   ├── middleware          # 中间件
│   ├── model               # 数据表
│   ├── schema              # 数据校验
│   └── util                # 通用
├── logs                    # 日志文件
├── config                  # 配置文件
├── config.py               # 对配置对象的前置操作
├── docker                  # dockerfile
├── docker-compose.yml      # docker-compose.yml
├── entrypoint.sh           # 入口文件
├── main.py                 # 入口文件
├── readme.md               # readme
├── requirements.txt        # pip
├── static                  # 静态文件
└── test                    # 测试用例
```


## 0x03. 通用的 用户权限 系统
```markdown

```


## 0x04. 支持 文件 && 环境变量 共同控制 项目配置
```markdown
1. 支持多种类型的配置文件
Potionx/config/config.json | yml | ini

2. 支持环境变量
1. `${POTIONX_ENV}` 
控制当前是 开发(development) 环境还是 正式(production) 环境。
2. `${POTIONX_REL_DB}`
控制当前使用的关系型数据库是 MySQL 还是 PostgreSQL

ps:
当 环境变量 与 配置文件 含有同名变量，以配置文件内容为准。
```

## 0x05. 统一的 JSON 返回格式 && 全局异常捕捉 && 自定义异常捕捉
```json
// format
{
    "code": int,
    "message": str,
    "data": Any
}
```

## 0x06. Log
```markdown
1. log 配置
config.py

2. 日志格式 && 有效期 
info.log.{time:YYYY-MM-DD} | 3 days
error.log.{time:YYYY-MM-DD} | 3 days
debug.log.{time:YYYY-MM-DD} | 1 days
```


## 0x07. Debug
```bash
docker-compose pull
docker-compose build
docker-compose up -d
```