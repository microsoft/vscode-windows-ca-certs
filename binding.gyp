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
      "msvs_configuration_attributes": {
        "SpectreMitigation": "Spectre"
      },
      "msvs_settings": {
        "VCCLCompilerTool": {
          "AdditionalOptions": [
            "/guard:cf",
            "/we4244",
            "/we4267",
            "/ZH:SHA_256"
          ]
        },
        "VCLinkerTool": {
          "AdditionalOptions": [
            "/guard:cf"
          ]
        }
      }
    }
  ]
}
