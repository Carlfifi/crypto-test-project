# 模拟一个数字货币资产组合
# 1. 定义核心变量
trader_name = 'Tester'
btc_price = 6235.75  #假设的BTC当前价格
# 2. 使用字典创建资产组合（这是金融数据的关键结构

crypto_portfolio = {
    'BTC': {
        "holding": 0.85,  # 持有数量
        "buy_price": 58000.00,  # 买入均价
        "current_price": btc_price
    },
"ETH": {
        "holding": 5.2,
        "buy_price": 3200.00,
        "current_price": 3450.50
    },
"USDT": {
        "holding": 1000.0,
        "buy_price": 1.0,
        "current_price": 1.0
    }

}

# 3. 计算并打印每种资产的盈亏情况
print(f"交易员 {trader_name} 的资产组合分析报告")
print("=" * 40)

total_profit_loss = 0.0 # 总盈亏

for coin, info in crypto_portfolio.items(): # 遍历字典
    market_value = info['holding'] * info["current_price"]
    cost_basis = info["holding"] * info["buy_price"]
    profit_loss = market_value - cost_basis
    profit_loss_percent = (profit_loss / cost_basis) * 100 if cost_basis != 0 else 0

    total_profit_loss += profit_loss

    print(f"\n币种: {coin}")
    print(f"  持有数量: {info['holding']}")
    print(f"  当前市值: ${market_value:.2f}")
    print(f"  持仓成本: ${cost_basis:.2f}")
    print(f"  浮动盈亏: ${profit_loss:+.2f} ({profit_loss_percent:+.2f}%)")  # + 号表示正负

print("=" * 40)
print(f"组合总浮动盈亏: ${total_profit_loss:+.2f}")

# 在day1_portfolio.py文件末尾添加：
print("\n正在根据实时价格更新资产组合...")
# 这里暂时模拟从API获取的价格（明天我们会将两个文件连接起来）
latest_prices = {"BTC": 63420, "ETH": 3467.18, "SOL": 152.34}
for coin, info in crypto_portfolio.items():
    if coin in latest_prices:
        info["current_price"] = latest_prices[coin]
print("资产组合已使用最新价格更新。")