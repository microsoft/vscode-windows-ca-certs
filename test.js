var assert = require('assert')
var forge = require('node-forge')

var asn1 = forge.asn1

nApi()

function assertCrt(blob) {
  var tree = asn1.fromDer(blob.toString('binary'))
  assert(tree.value.length)
}

function nApi() {
  if (!process.versions.napi) {
    console.log('! Skipping N-API bindings test...')
    return
  }

  console.log('Starting N-API connection...')
  crypt = require('bindings')('crypt32')
  var a = new crypt.Crypt32()

  var N = 0
  console.log('Fetching...')
  for (var blob; blob = a.next(); N++) {
    assertCrt(blob)
    assert(N < 1000)
  }

  console.log('Total:', N, '\t// N-API')

  console.log('Cleaning N-API...')
  a.done()
}
