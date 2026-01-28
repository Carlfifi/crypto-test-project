import requests
import time

# 目标：从一个免费、无需密钥的API获取多个主流币种价格
# 使用 CoinGecko 公开API

def fetch_crypto_price(coin_ids):
    """
        从CoinGecko获取加密货币价格
        :param coin_ids: 币种ID列表，例如 ['bitcoin', 'ethereum', 'solana']
        :return: 包含价格的字典，例如 {'bitcoin': 63000, 'ethereum': 3400}
        """
    # 将列表转换为API需要的字符串格式
    ids = ','.join((coin_ids))
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"

    print(f"正在请求: {url}")
    try:
        response =requests.get(url,timeout = 10)
        response.raise_for_status()

        data = response.json()
        print("API原始响应:", data)
        return data

    except requests.exceptions.Timeout:
        print("错误: 请求超时，请检查网络。")
        return None

    except requests.exceptions.HTTPError:
        print(f"HTTP错误: {e}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"请求异常: {e}")
        return None


if __name__=="__main__":
    # 1. 定义你想查询的币种列表
    coins_to_check = ['bitcoin', 'ethereum', 'solana']

    # 2. 调用函数获取价格
    price_data = fetch_crypto_price(coins_to_check)

    # 3. 格式化输出结果
    if price_data:
        print("\n" + "=" * 50)
        print("加密货币实时价格（USD）")
        print("=" * 50)
        timestamp = int(time.time())
        print(f"数据更新时间戳: {timestamp}")
        print("-" * 50)

        for coin_id in coins_to_check:
            usd_price = price_data.get(coin_id, {}).get('usd', 'N/A')
            # 美化输出，将coin_id首字母大写
            coin_name = coin_id.capitalize()
            print(f"{coin_name:>10} (${coin_id:^10}): ${usd_price:>12,.2f}")
        print("=" * 50)
    else:
        print("未能获取价格数据，请检查以上错误信息。")

