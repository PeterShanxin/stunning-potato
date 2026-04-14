import time
from echo_sdk import EchoPromptClient

# 1. 开发者初始化你的 SDK
client = EchoPromptClient(base_url="http://127.0.0.1:8000")

def run_customer_service_bot(user_message: str):
    print("🤖 正在处理用户消息:", user_message)
    
    # [演示亮点 1] 动态获取 Prompt，业务代码与提示词解耦！
    print("-> 正在通过 Echo SDK 获取最新的活跃提示词...")
    try:
        active_config = client.get_active_prompt(asset_name="customer_service_vqa")
        system_prompt = active_config.get("system_prompt")
        version_id = active_config.get("version_id")
        print(f"-> 成功加载版本 #{version_id} 的提示词: {system_prompt[:20]}...")
    except Exception as e:
        print("-> 获取失败，请确保资产 'customer_service_vqa' 存在且有激活的版本！\n错误:", e)
        return

    # 模拟调用大模型 (比如调用 OpenAI)
    start_time = time.time()
    print("-> 正在调用底层大模型 (模拟)...")
    time.sleep(1) # 模拟网络延迟
    mock_llm_response = f"您好！我是客服，关于您说的 '{user_message}'，请尝试重启设备。"
    latency = int((time.time() - start_time) * 1000)

    # [演示亮点 2] 自动留痕，一键完成 AI 监控与复盘记录
    print("-> 正在通过 Echo SDK 记录执行日志...")
    client.log_execution(
        asset_version_id=version_id,
        model_name="gpt-4o",
        input_variables={"user_input": user_message},
        llm_output=mock_llm_response,
        latency_ms=latency,
        token_usage=45
    )
    
    print("✅ 处理完成，日志已写入 CMS！机器人回复:", mock_llm_response)
    print("-" * 50)

if __name__ == "__main__":
    # 运行测试前，请确保你在前端页面中：
    # 1. 创建了一个 name 为 "customer_service_vqa" 的资产
    # 2. 为它创建了一个版本，并勾选了 "set_active"
    run_customer_service_bot("我的密码忘记了怎么办？")
