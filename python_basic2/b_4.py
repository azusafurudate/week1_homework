def main():
    # 3都府県のいくつかの駅名とある日の最高気温(℃)
    tenki_data = [
        {"todofuken": "東京都", "eki": "渋谷", "kion": 6.5},
        {"todofuken": "東京都", "eki": "池袋", "kion": 7.0},
        {"todofuken": "東京都", "eki": "新橋", "kion": 7.5},
        {"todofuken": "大阪府", "eki": "梅田", "kion": 8.2},
        {"todofuken": "大阪府", "eki": "大阪", "kion": 9.3},
        {"todofuken": "大阪府", "eki": "堺", "kion": 9.5},
        {"todofuken": "福岡県", "eki": "博多", "kion": 13.0},
        {"todofuken": "福岡県", "eki": "大宰府", "kion": 15.0},
    ]

    # Q1: 全国の平均気温
    kion_list = [d["kion"] for d in tenki_data]
    heikin_zenkoku = sum(kion_list) / len(kion_list)
    print(f"Q1 全国の平均気温: {heikin_zenkoku:.1f} ℃")

    # Q2: 大阪府の全駅名をカンマ区切りで
    osaka_eki_list = [d["eki"] for d in tenki_data if d["todofuken"] == "大阪府"]
    print("Q2 大阪府の駅:", ", ".join(osaka_eki_list))

    # Q3: 福岡県の平均気温
    fukuoka_kion_list = [d["kion"] for d in tenki_data if d["todofuken"] == "福岡県"]
    heikin_fukuoka = sum(fukuoka_kion_list) / len(fukuoka_kion_list)
    print(f"Q3 福岡県の平均気温: {heikin_fukuoka:.1f} ℃")


if __name__ == "__main__":
    main()
