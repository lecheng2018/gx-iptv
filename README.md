# 广西移动 IPv6 直播源

自动同步上游 [lizhaohai369/fork-iptv-m3u8](https://github.com/lizhaohai369/fork-iptv-m3u8) 的广西移动 IPv6 源，并转换为标准 m3u 格式。

## 使用

```
https://raw.githubusercontent.com/lecheng2018/gx-iptv/main/gxyd_ipv6.m3u
```

导入支持 m3u 的 IPTV 播放器即可（APTV、TiviMate、IPTV Pro、Kodi 等）。

## 更新频率

每 **6 小时**自动同步上游。

## 频道

- 央视全系列（CCTV1~CCTV17、CGTN 等）
- 各省卫视
- 广西本地台（南宁、柳州、桂林、北海、玉林等）
- NewTV 系列
- 咪咕 4K

## 技术栈

- Python 3 转换脚本
- GitHub Actions 定时同步
