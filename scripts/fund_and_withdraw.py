from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entranceFee = fund_me.getEntranceFee()
    print(entranceFee)
    print(f"the current entrance fee is {entranceFee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entranceFee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
