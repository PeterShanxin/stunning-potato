from setuptools import setup, find_packages

setup(
    name="echo-prompt",             # 🌟 投资人会看到的包名
    version="0.1.0",
    description="Official Python SDK for Echo Prompt CMS",
    author="Your Awesome Startup",
    packages=find_packages(),       # 自动发现 echo_sdk 文件夹
    install_requires=[
        "requests>=2.25.0",         # 自动帮你安装依赖的网络请求库
    ],
    python_requires=">=3.7",
)
