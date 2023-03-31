import time

from member import Member


members = []
other_members_addresses = []
raft_port = 8008

for i in range(3):
    member_address = f"127.0.0.1:{raft_port}"
    if len(members) > 0:
        if len(members) != 2:
            leader.addNodeToCluster(member_address)
        member = Member(raft_port, other_members_addresses)
        if len(members) == 2:
            # leader.addNodeToCluster(member_address)
            pass
    else:
        member = Member(raft_port)
        leader = member
    members.append(member)
    other_members_addresses.append(member_address)
    raft_port = raft_port + 1

# Just a loop to keep the program running.
while True:
    time.sleep(30)
