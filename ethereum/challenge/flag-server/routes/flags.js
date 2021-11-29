const util = require('ethereumjs-util')
// const Web3 = require('web3')
const crypto = require('crypto')
const express = require('express')
const utils = require('../utils')
const flags = require('../config/flags.json')
const router = express.Router()

const nonceCache = {}

router.get('/', function (req, res, next) {
  res.json({ title: 'ETH Flag Server' })
})

router.get('/pre-auth/:address', function (req, res) {
  console.log('pre-auth')
  const playerAddress = req.params.address.toLowerCase()
  const nonce = crypto.randomBytes(16).toString('base64')

  nonceCache[playerAddress] = nonce

  console.log(nonceCache)
  res.json({ nonce })
})

router.post('/', async function (req, res) {
  console.log('validate')
  const { contract } = utils.initWeb3()
  const player = req.body.msg.player.toLowerCase()
  const nonce = nonceCache[player]
  const msg = req.body.msgHash
  const msgBuffer = Buffer.from(msg.replace('0x', ''), 'hex')

  if (!nonce) return res.status(422).json({ error: 'Nonce not found, ensure to pre authenticate at /flags/pre-auth/<PLAYER_ADDRESS>' })
  if (nonce !== req.body.msg.nonce) return res.status(422).json({ error: 'Invalid Nonce' })

  // lots of nonsense to do as ecRecover doesn't work with Ganache
  const prefix = Buffer.from('\x19Ethereum Signed Message:\n')
  const prefixedMsg = util.keccak256(Buffer.concat([prefix, Buffer.from(String(msgBuffer.length)), msgBuffer]))
  const { v, r, s } = util.fromRpcSig(req.body.sig)
  const pubKey = util.ecrecover(prefixedMsg, v, r, s)
  const addrBuffer = util.pubToAddress(pubKey)
  const signatureAddress = util.bufferToHex(addrBuffer)

  console.log('sig address:', signatureAddress)

  if (signatureAddress !== player) {
    return res.status(401).json({ error: 'Invalid Address' })
  }

  // check contract to ensure level has been completed
  let completed
  try {
    completed = await contract.methods.verifyLevelInstanceCompletion(req.body.instanceAddress).call()
  } catch (e) {
    return res.status(422).json({ error: e.message })
  }

  if (!completed) {
    return res.status(400).json({ error: 'Challenge has not been completed' })
  }
  nonceCache[player] = null
  res.json({ flag: flags[req.body.msg.level] })
})

module.exports = router
