# tool_reco
安全工具推荐集合，付费软件采用$标记
声明：本仓库中的代码和内容仅供学习和研究使用，不得用于任何商业目的。任何人或组织在使用时，应遵守相关法律法规，并尊重相关权利人的合法权益。
如果您是此项目的版权所有者并认为该项目侵犯了您的权益，请与我联系，我会尽快处理。

# 扫描器
1. **Nuclei**[https://github.com/projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)
   - 免费，开源，高速，自定义模板扫描器。
2. **XSStrike**[https://github.com/s0md3v/XSStrike](https://github.com/s0md3v/XSStrike)
   - xss漏洞扫描，可探测dom类型XSS
3. **xsser**[https://github.com/epsylon/xsser](https://github.com/epsylon/xsser)
   - 与xsstrike相似，kali自带

# 抓包工具
1. **windows抓包**
   - **wireshark**: [https://www.wireshark.org](https://www.wireshark.org)
   - **Fiddler**: [https://www.telerik.com/fiddler](https://www.telerik.com/fiddler)

# 应急响应
1. **流量在线分析PacketTotal**[https://lab.dynamite.ai/](https://lab.dynamite.ai/)
2. **火绒安全软件**[https://www.huorong.cn/](https://www.huorong.cn/)
   - 火绒剑进行安全排查，恶意软件行为分析十分好用。
4. **微软官方工具**[https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)
   - 微软官方工具，内含tcp_view,auto_run,process_exprole等重量级工具，十分好用。
   
# 远控实验工具
   开源远控工具，可用于恶意软件分析或者学习。
1. **windows远控**
   - **cowrie**: [https://github.com/cowrie/cowrie](https://github.com/cowrie/cowrie)
   - **chaos**: [https://github.com/jonnyhyman/Chaos](https://github.com/jonnyhyman/Chaos)


# Honeypot 蜜罐推荐

在网络安全中，蜜罐（Honeypot）是一种用于吸引和监视恶意攻击的工具。高阶玩家常常用蜜罐捕获0day利用程序。

1. **Cowrie**:
   - **类型**: 中互动 SSH 和 Telnet 蜜罐
   - **描述**: Cowrie 是用于 SSH 攻击的常见选择。它可以记录暴力连接尝试，捕获攻击者执行的 shell 交互，并可以配置为提供完整的 shell 或有限的 shell 环境。
   - **链接**: [https://github.com/cowrie/cowrie](https://github.com/cowrie/cowrie)

2. **Dionaea**:
   - **类型**: 低/中互动蜜罐
   - **描述**: Dionaea 旨在捕获恶意软件。它模拟易受攻击的服务，并可以捕获攻击者尝试部署的二进制文件。
   - **链接**: [https://github.com/DinoTools/dionaea](https://github.com/DinoTools/dionaea)

3. **Honeytrap**:
   - **类型**: 低/中互动蜜罐
   - **描述**: Honeytrap 可以监视针对 TCP 和 UDP 服务的攻击。它还可以模拟多种不同的服务，以欺骗攻击者。
   - **链接**: [https://github.com/armedpot/honeytrap](https://github.com/armedpot/honeytrap)

4. **MHN（Modern Honey Network）**:
   - **类型**: 蜜罐管理
   - **描述**: 虽然不是蜜罐本身，但是 MHN 是一个管理工具。MHN 提供了一个集中式服务器，用于管理、数据收集和可视化多个蜜罐。
   - **链接**: [https://github.com/threatstream/mhn](https://github.com/threatstream/mhn)

5. **Kippo**:
   - **类型**: 中互动 SSH 蜜罐
   - **描述**: 虽然 Cowrie 是 Kippo 的一个分支和改进，但 Kippo 本身仍然值得注意。它可以记录暴力连接尝试以及攻击者执行的 shell 交互。
   - **链接**: [https://github.com/desaster/kippo](https://github.com/desaster/kippo)

6. **T-Pot**:
   - **类型**: 多蜜罐平台
   - **描述**: T-Pot 是建立在 Elastic Stack（以前称为 ELK Stack）上的多蜜罐平台，集成了多个蜜罐在一个系统中，提供了全面的数据收集和可视化方式。
   - **链接**: [https://github.com/telekom-security/tpotce](https://github.com/telekom-security/tpotce)

7. **Snare/Tanner**:
   - **类型**: Web 蜜罐
   - **描述**: Snare 允许您克隆一个网站以用作诱饵，而 Tanner 处理结果并确定攻击类型。
   - **链接**: [Snare GitHub](https://github.com/mushorg/snare) 和 [Tanner GitHub](https://github.com/mushorg/tanner)

8. **Conpot**:
   - **类型**: ICS/SCADA 蜜罐
   - **描述**: Conpot 是一个低互动的工业控制系统蜜罐，旨在易于部署、修改和扩展。
   - **链接**: [https://github.com/mushorg/conpot](https://github.com/mushorg/conpot)



