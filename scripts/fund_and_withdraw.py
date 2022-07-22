from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    accoun = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(2 * entrance_fee)


def main():
    fund()
