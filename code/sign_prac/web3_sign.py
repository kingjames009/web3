from web3 import Web3, HTTPProvider
from eth_account.messages import encode_defunct

private_key = "05e457830802b04a140d58aaa269000000000000000000000000000000"
address = "0xa56a26AA80826c558B201af2C90fa9CA23620080"
rpc = 'https://rpc.ankr.com/eth'
w3 = Web3(HTTPProvider(rpc))

#打包信息
msg = Web3.solidity_keccak(['address','uint256'], [address,0])
print(f"消息：{msg.hex()}")
#构造可签名信息
message = encode_defunct(hexstr=msg.hex())
#签名
signed_message = w3.eth.account.sign_message(message, private_key=private_key)
print(f"签名：{signed_message['signature'].hex()}")