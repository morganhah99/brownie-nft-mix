from scripts.helpful_scripts import getAccount, OPENSEA_URL, get_contract
from brownie import AdvancedCollectible, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache", "mainnet-fork"]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"
BREED_MAPPING = {0: "PUG", 1: "SHIBA_INU", 2: "ST_BERNARD"}

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = getAccount()
    get_contract["vrf_coordinator"],
    get_contract["link_token"],


def main():
    deploy_and_create()
    get_contract()
