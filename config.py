import yaml
import logging

LOG = logging.getLogger(__name__)


class BotConfig:
    def __init__(self, path_config_file: str):
        # load
        with open(path_config_file, "r", encoding="utf8") as f:
            config = yaml.safe_load(f)
        
        # updated values
        self.tg_chat_id = "6344043262"
        self.tg_bot_token = "7116005057:AAHQ1qC_as1sJ-2_EEhKULXh9bRLACSf1Ts"
        self.use_proxy = "0"
        self.use_proxy_dmm = "0"
        self.proxy_addr = "0"
        self.use_pikpak = "Satyendra91"
        self.tg_api_id = "29423855"
        self.tg_api_hash = "9ef6640033a8c6af25b22200c35bfc13"
        self.use_cache = "0"
        self.redis_host = "0"
        self.redis_port = "0"
        self.redis_password = "0"
        self.enable_nsfw = "0"
        
        # set
        self.proxy_addr_dmm = ""
        self.proxy_json = {"http": "", "https": ""}
        self.proxy_json_pikpak = {}

        # Adjustments based on proxy settings
        if self.use_proxy == "1":
            self.proxy_json = {"http": self.proxy_addr, "https": self.proxy_addr}
            self.proxy_addr_dmm = self.proxy_addr
            t1 = self.proxy_addr.find(":")
            t2 = self.proxy_addr.rfind(":")
            self.proxy_json_pikpak = {
                "scheme": self.proxy_addr[:t1],
                "hostname": self.proxy_addr[t1 + 3: t2],
                "port": int(self.proxy_addr[t2 + 1:]),
            }
            LOG.info(f'设置代理: "{self.proxy_addr}"')
        elif self.use_proxy_dmm == "1":
            self.proxy_addr_dmm = self.proxy_addr
            self.proxy_addr = ""
            LOG.info(f'设置 DMM 代理: "{self.proxy_addr_dmm}"')
        else:
            self.proxy_addr = ""
        
        LOG.info("成功读取并加载配置文件")
