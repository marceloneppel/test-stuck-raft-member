import http.server
from typing import List

from pysyncobj import SyncObj, replicated, SyncObjConf

Handler = http.server.SimpleHTTPRequestHandler


class Member(SyncObj):
    def __init__(self, raft_port: int, other_members_addresses: List[str] = None):
        if other_members_addresses is None:
            other_members_addresses = []
        conf = SyncObjConf(dynamicMembershipChange=True)
        super(Member, self).__init__(f"127.0.0.1:{raft_port}", other_members_addresses, conf)
        self.__counter = 0
        self.__raft_port = raft_port

    @replicated
    def inc_counter(self):
        self.__counter += 1

    def get_counter(self) -> int:
        return self.__counter
