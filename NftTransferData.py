#! /usr/bin/env python3.7
import json
import os
import subprocess
import threading
import time

import cloudscraper


os.chdir(os.path.split(os.path.realpath(__file__))[0])


class NftJsonSpiser:
    @staticmethod
    def try_requests_api(need_event_type):
        scraper = cloudscraper.create_scraper()
        url = "https://api.opensea.io/api/v1/events"
        headers = {"Accept": "application/json", "X-API-KEY": "9745fb58805643f0a117d4bc043439cf"}
        for i in range(92080, 100000):
            next_cursor = ""
            download_json = []
            params = {"only_opensea": False, "asset_contract_address": "0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258"}
            params["token_id"] = i
            params["event_type"] = need_event_type
            while next_cursor is not None:
                if next_cursor != "":
                    params["cursor"] = next_cursor
                response = scraper.get(url, params=params, headers=headers, proxies={"https": "http://127.0.0.1:1080"})
                time.sleep(0.25)
                next_cursor = response.json().get("next")
                for asset_event in response.json().get("asset_events"):
                    download_json.append(asset_event)
            print(i)
            if download_json != []:
                savr_json_thread = SaveJsonThread(i, download_json)
                savr_json_thread.start()


class SaveJsonThread(threading.Thread):
    def __init__(self, flie_num: int, file_content: list):
        threading.Thread.__init__(self)
        self.flie_num = flie_num
        self.file_content = file_content

    def run(self) -> None:
        with open("./transferdata/{}.json".format(self.flie_num), "w") as f:
            f.write(json.dumps(self.file_content, indent=4, separators=(",", ": ")))
        # subprocess.call(["sz", "{}.json".format(self.flie_num)])
        # subprocess.call(["rm", "-f", "{}.json".format(self.flie_num)])


if __name__ == "__main__":
    # 爬虫
    NftJsonSpiser.try_requests_api("transfer")
