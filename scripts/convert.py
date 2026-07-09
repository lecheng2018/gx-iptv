#!/usr/bin/env python3
"""
广西移动 IPv6 直播源转换脚本
从 lizhaohai369/fork-iptv-m3u8 拉取原始 txt，转为标准 m3u 格式
"""
import urllib.request
import os
import sys

UPSTREAM_URL = (
    "https://raw.githubusercontent.com/lizhaohai369/fork-iptv-m3u8/main/"
    "%E5%B9%BF%E8%A5%BFV6.txt"
)
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "gxyd_ipv6.m3u")
EPG_URL = "https://epg.112114.xyz/pp.xml"


def fetch_source(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def convert(content: str) -> str:
    lines = content.strip().split("\n")
    lines = [l.strip() for l in lines if l.strip() and not l.strip().startswith("#")]

    m3u = []
    m3u.append("#EXTM3U x-tvg-url=\"{}\"".format(EPG_URL))
    m3u.append("# 广西移动 IPv6 直播源")
    m3u.append("# 上游: lizhaohai369/fork-iptv-m3u8")
    m3u.append("# 频道数: {}".format(len(lines)))
    m3u.append("")

    for line in lines:
        if "," not in line:
            continue
        idx = line.index(",")
        name = line[:idx].strip()
        url_val = line[idx + 1:].strip()
        if url_val:
            m3u.append('#EXTINF:-1 tvg-id="" tvg-name="{}" group-title="广西移动",{}'.format(name, name))
            m3u.append(url_val)

    m3u.append("")
    return "\n".join(m3u)


def main():
    print("🔄 正在从上游拉取源...")
    try:
        raw = fetch_source(UPSTREAM_URL)
    except Exception as e:
        print("❌ 拉取失败: {}".format(e), file=sys.stderr)
        sys.exit(1)

    print("✅ 拉取成功 ({} 条记录)".format(len([l for l in raw.split("\n") if l.strip() and not l.strip().startswith("#") and "," in l])))

    m3u_content = convert(raw)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(m3u_content)

    print("✅ 已生成: {}".format(OUTPUT_FILE))
    print("📺 频道数: {} (含多线路备选)".format(len([l for l in m3u_content.split("\n") if l.startswith("#EXTINF:")])))


if __name__ == "__main__":
    main()
