{
  "targets": [
    {
      "target_name": "crypt32",
      "cflags!": [
        "-fno-exceptions"
      ],
      "cflags_cc!": [
        "-fno-exceptions"
      ],
      "sources": [
        "crypt32.cc"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      "defines": [
        "NAPI_DISABLE_CPP_EXCEPTIONS"
      ],
      "link_settings": {
        "libraries": ["-lcrypt32"]
      },
      'msvs_settings': {
        'VCCLCompilerTool': {
          'AdditionalOptions': [
            '/Qspectre',
            '/guard:cf',
            '/w34244',
            '/w34267',
            '/ZH:SHA_256',
            '/sdl'
          ]
        },
        'VCLinkerTool': {
          'AdditionalOptions': [
            '/guard:cf',
            '/CETCOMPAT',
            '/DYNAMICBASE'
          ]
        }
      }
    }
  ]
}
