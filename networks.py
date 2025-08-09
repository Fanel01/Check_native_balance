class Networks:
    def __init__(self, rpc, name):
        self.rpc = rpc
        self.name = name



ethereum = Networks(
    rpc= 'https://eth.llamarpc.com',
    name= 'ETHEREUM',
)

arbitrum = Networks(
    rpc= 'https://arbitrum-one.public.blastapi.io',
    name= 'ARBITRUM',
)

base = Networks(
    rpc= 'https://base.llamarpc.com',
    name= 'BASE',
)

optimism = Networks(
    rpc= 'https://optimism.public.blockpi.network/v1/rpc/public',
    name= 'OPTIMISM',
)
