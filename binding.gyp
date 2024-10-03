{
  "targets": [
    {
      "target_name": "crypt32",
      "sources": [
        "crypt32.cc"
      ],
      "dependencies": [
        "<!(node -p \"require('node-addon-api').targets\"):node_addon_api_except"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      "defines": [
        "NODE_API_SWALLOW_UNTHROWABLE_EXCEPTIONS"
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
