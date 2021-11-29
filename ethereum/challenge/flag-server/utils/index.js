const Web3 = require('web3')
const abi = require('../config/Ethernaut.json').abi
const HDWalletProvider = require('@truffle/hdwallet-provider')
const { contractAddress, ownerKey, providerUrl } = require('../config/admin.json')

function initWeb3 () {
  const provider = new HDWalletProvider(ownerKey, providerUrl)
  const web3 = new Web3(provider)
  const contract = new web3.eth.Contract(abi, contractAddress)

  return {
    web3,
    contract
  }
}

module.exports = { initWeb3 }
