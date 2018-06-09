#coding:utf-8
#HadesCoin airdrop python script
#Python3-6-4
#Before use it ,pls read README.md
#   HadesCoin go to the moon
#  
#  $$    $$   $$$$$$   $$$$$$$$   $$$$$$$$$   $$$$$$$$  
#  $$    $$  $$    $$  $$     $$  $$          $$  
#  $$    $$  $$    $$  $$     $$  $$          $$   
#  $$$$$$$$  $$$$$$$$  $$     $$  $$$$$$$$$   $$$$$$$$  
#  $$    $$  $$    $$  $$     $$  $$                $$  
#  $$    $$  $$    $$  $$     $$  $$                $$  
#  $$    $$  $$    $$  $$$$$$$$   $$$$$$$$$   $$$$$$$$   
#
import os,sys,time,re,xlrd
from web3 import Web3, HTTPProvider
import rlp
from ethereum.transactions import Transaction
#web3 = Web3(HTTPProvider('http://127.0.0.1:8545')) #local eth wallet
web3 = Web3(HTTPProvider('https://mainnet.infura.io/'))
workbook=xlrd.open_workbook('sendethallto1.xlsx')
table=workbook.sheet_by_index(0)
nrows = table.nrows

if __name__ == '__main__':
	i=2
	toAddress=table.cell(1,0).value
	print("toAddr:",toAddress)
	gasLimit=table.cell(1,1).value
	gasPrice=table.cell(1,2).value
	ethValue=table.cell(1,3).value
	#print(fromAddress,privateKey,gasLimit,gasPrice,ethValue)
	#nrows=3
	sucess=0
	while i<nrows:
		i+=1
		fromAddress=table.cell(i,0).value
		privateKey=table.cell(i,1).value
		noNice=web3.eth.getTransactionCount(fromAddress)	
		print("fromAddress:",fromAddress)
		tx = Transaction(
							nonce=noNice,
							gasprice=web3.toInt(hexstr=gasPrice),
							startgas=web3.toInt(hexstr=gasLimit),
							to=toAddress,
							value=web3.toWei(ethValue,'ether'),
							data=b''
						)
		noNice+=1
		tx.sign(privateKey)
		raw_tx = rlp.encode(tx)
		raw_tx_hex = web3.toHex(raw_tx)
		txhash=""
		try:
			txhash=web3.eth.sendRawTransaction(raw_tx_hex)
		except Exception as e:
			print(e)

			continue
		sucess+=1
		print("sucess:",sucess)
		sucessstr=fromAddress+","+web3.toHex(txhash)+"\n"
		fbsucess.write(sucessstr)

		print("txhash:",web3.toHex(txhash))
		#break







