const express = require('express')
const router = express.Router()
const utils = require('../utils')
const config = require('../config/admin.json')

router.get('/', function (req, res, next) {
  res.json({ title: 'No flag here' })
})

router.post('/register', async function (req, res, next) {
  const address = req.body.playerAddress
  const { contract, web3 } = utils.initWeb3()

  console.log('Ether request for ', address)
  try {
    const transactions = await web3.eth.getTransactionCount(config.ownerAddress)

    await contract.methods.registerPlayer(address).send({
      from: config.ownerAddress,
      value: 10000000000000000000,
      gas: 100000,
      nonce: transactions
    })
  } catch (e) {
    return res.status(422).json({ error: e.message })
  }

  res.json({ success: true })
})

module.exports = router
