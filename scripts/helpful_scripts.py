from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    print(f"get_account network is {network.show_active()}")
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print(f"Network is {network.show_active()}")
        print(accounts[0], len(accounts))
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print(f"**************\nAccount={get_account()}\n****************")
    print("Deploying mocks!")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
    print("Mocks deployed!")
