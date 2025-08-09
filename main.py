from config import WALLETS_DIR
from client_web3 import ClientWeb3
from networks import ethereum, arbitrum, base,optimism
from utils.file_loader import file_reader


def main():
    chains = [ethereum, arbitrum, base, optimism]
    addresses = file_reader(WALLETS_DIR)
    for chain in chains:
        for address in addresses:
            client_w3 = ClientWeb3(chain, address)

            result = client_w3.check_native_balance()

            print(f'Address -{address}- have balance in -{chain.name}-: {result / 10**18}')


if __name__ == '__main__':
    main()


