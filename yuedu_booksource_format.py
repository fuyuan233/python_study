# Writer :fuyuan360
# Email  :fuyuan360@qq.com
import json
import re
from collections import defaultdict


def format_url(url) :
    """格式化URL，提取干净的域名部分"""
    if not isinstance(url, str) :
        return url

    match = re.match(r'^(?:https?://)?([^/#\s]+)(?:[/#].*)?$', url.strip())
    if match :
        return match.group(1)
    return url


def process_and_sort_json(input_file, output_file=None) :
    """
    处理JSON文件中的bookSourceUrl字段并排序，自动处理重复项

    :param input_file: 输入JSON文件路径
    :param output_file: 输出JSON文件路径(可选，默认覆盖原文件)
    :return: 处理成功返回True，否则返回False
    """
    # 如果没有指定输出文件，则覆盖原文件
    if output_file is None :
        output_file = input_file

    # 读取JSON文件
    try :
        with open(input_file, 'r', encoding='utf-8') as f :
            data = json.load(f)
    except FileNotFoundError :
        print(f"错误：文件不存在 - {input_file}")
        return False
    except json.JSONDecodeError :
        print(f"错误：文件不是有效的JSON格式 - {input_file}")
        return False
    except Exception as e :
        print(f"读取文件失败: {e}")
        return False

    # 检查数据是否为列表
    if not isinstance(data, list) :
        print("JSON数据不是列表格式，无法处理")
        return False

    # 处理数据并准备去重
    url_dict = defaultdict(list)
    for idx, item in enumerate(data) :
        if isinstance(item, dict) and 'bookSourceUrl' in item :
            formatted_url = format_url(item['bookSourceUrl'])
            item['bookSourceUrl'] = formatted_url
            item['_sort_key'] = formatted_url.lower() if isinstance(formatted_url, str) else ''
            # 计算字典的字符数长度作为完整度指标
            item['_length'] = len(json.dumps(item, ensure_ascii=False))
            url_dict[formatted_url].append((idx, item['_length']))
        else :
            # 对于没有bookSourceUrl的项，也添加到结果中
            url_dict[None].append((idx, 0))

    # 标记需要保留的条目（每组重复URL中字符数最多的）
    keep_indices = set()
    for url, items in url_dict.items() :
        if url is not None and len(items) > 1 :
            # 找出字符数最多的条目
            max_item = max(items, key=lambda x : x[1])
            print(f"发现重复URL: {url}，保留字符数最多的条目（长度: {max_item[1]}）")
            keep_indices.add(max_item[0])
        else :
            # 非重复项或没有bookSourceUrl的项全部保留
            for item in items :
                keep_indices.add(item[0])

    # 过滤数据，只保留标记的条目
    filtered_data = [data[i] for i in range(len(data)) if i in keep_indices]

    # 按排序键排序
    try :
        filtered_data.sort(key=lambda x : x.get('_sort_key', ''))
    except Exception as e :
        print(f"排序失败: {e}")
        return False

    # 移除临时字段
    for item in filtered_data :
        for field in ['_sort_key', '_length'] :
            if field in item :
                del item[field]

    # 写入处理后的数据
    try :
        with open(output_file, 'w', encoding='utf-8') as f :
            json.dump(filtered_data, f, ensure_ascii=False, indent=4)
        print(f"处理完成: 已格式化URL，处理了{len(data) - len(filtered_data)}个重复项，结果保存到: {output_file}")
        return True
    except Exception as e :
        print(f"写入文件失败: {e}")
        return False


# 使用示例
if __name__ == "__main__" :
    process_and_sort_json("./bookSource.json", "new_bookSource.json")