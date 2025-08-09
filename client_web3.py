from web3 import Web3


class ClientWeb3:
    def __init__(self, chain, address):
        self.w3 = Web3(Web3.HTTPProvider(chain.rpc))
        self.address = Web3.to_checksum_address(address)

    def check_native_balance(self):
        return self.w3.eth.get_balance(self.address)

