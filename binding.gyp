{
  "variables": {
    "arch": "<(target_arch)"
  },
  "targets": [
    {
      "target_name": "copy_fptr_libs",
      "type": "none",
      "copies": [
        {
          "destination": "<(PRODUCT_DIR)",
          "conditions": [
            ["OS=='win'", {
              "conditions": [
                ["arch=='ia32'", {
                  "files": [
                    "<(module_root_dir)/src/win-x86/dto/fptr10.dll",
                    "<(module_root_dir)/src/win-x86/dto/msvcp140.dll",
                    "<(module_root_dir)/src/win-x86/dto/fptr10.lib"
                  ]
                }],
                ["arch=='x64'", {
                  "files": [
                    "<(module_root_dir)/src/win-x64/dto/fptr10.dll",
                    "<(module_root_dir)/src/win-x64/dto/msvcp140.dll",
                    "<(module_root_dir)/src/win-x64/dto/fptr10.lib"
                  ]
                }]
              ]
            }],
            ["OS=='linux'", {
              "conditions": [
                ["arch=='ia32'", {
                  "files": [
                    "<(module_root_dir)/src/linux-x86/libfptr10.so",
                    "<(module_root_dir)/src/linux-x86/libudev.so.0",
                    "<(module_root_dir)/src/linux-x86/libusb-1.0.so.0"
                  ]
                }],
                ["arch=='x64'", {
                  "files": [
                    "<(module_root_dir)/src/linux-x64/libfptr10.so",
                    "<(module_root_dir)/src/linux-x64/libudev.so.0",
                    "<(module_root_dir)/src/linux-x64/libusb-1.0.so.0"
                  ]
                }],
                ["arch=='arm'", {
                  "files": [
                    "<(module_root_dir)/src/linux-armhf/libfptr10.so",
                    "<(module_root_dir)/src/linux-armhf/libudev.so.1",
                    "<(module_root_dir)/src/linux-armhf/libusb-1.0.so.0"
                  ]
                }],
                ["arch=='arm64'", {
                  "files": [
                    "<(module_root_dir)/src/linux-arm64/libfptr10.so",
                    "<(module_root_dir)/src/linux-arm64/libudev.so.1",
                    "<(module_root_dir)/src/linux-arm64/libusb-1.0.so.0"
                  ]
                }]
              ]
            }],
            ["OS=='mac'", {
              "conditions": [
                ["target_arch=='x64'", {
                  "files": [
                    "<(module_root_dir)/src/macos-x86_64/fptr10.framework"
                  ]
                }]
              ]
            }]
          ]
        },
        {
          "destination": "<(PRODUCT_DIR)/dto",
          "conditions": [
            ["OS=='win'", {
              "conditions": [
                ["arch=='ia32'", {
                  "files": [
                    "<(module_root_dir)/src/win-x86/dto/fptr10.dll",
                    "<(module_root_dir)/src/win-x86/dto/msvcp140.dll"
                  ]
                }],
                ["arch=='x64'", {
                  "files": [
                    "<(module_root_dir)/src/win-x64/dto/fptr10.dll",
                    "<(module_root_dir)/src/win-x64/dto/msvcp140.dll"
                  ]
                }]
              ]
            }]
          ]
        },
        {
          "destination": "<(PRODUCT_DIR)/dto-piot",
          "conditions": [
            ["OS=='win'", {
              "conditions": [
                ["arch=='ia32'", {
                  "files": [
                    "<(module_root_dir)/src/win-x86/dto-piot/fptr10.dll",
                    "<(module_root_dir)/src/win-x86/dto-piot/msvcp140.dll",
                    "<(module_root_dir)/src/win-x86/dto-piot/fptr10_bridge_grpc.dll",
                    "<(module_root_dir)/src/win-x86/dto-piot/platform_bridge_grpc.dll",
                    "<(module_root_dir)/src/win-x86/dto-piot/libeay32.dll",
                    "<(module_root_dir)/src/win-x86/dto-piot/ssleay32.dll"
                  ]
                }],
                ["arch=='x64'", {
                  "files": [
                    "<(module_root_dir)/src/win-x64/dto-piot/fptr10.dll",
                    "<(module_root_dir)/src/win-x64/dto-piot/msvcp140.dll",
                    "<(module_root_dir)/src/win-x64/dto-piot/fptr10_bridge_grpc.dll",
                    "<(module_root_dir)/src/win-x64/dto-piot/platform_bridge_grpc.dll",
                    "<(module_root_dir)/src/win-x64/dto-piot/libeay32.dll"
                  ]
                }]
              ]
            }]
          ]
        }
      ]
    },
    {
      "target_name": "node_atol_wrapper",
      "include_dirs": [
        "src",
        "<!(node -e \"require('nan')\")"
      ],
      "sources": [
        "src/index.cc",
        "src/fptr10.cc",
        "src/utils.cc",
        "src/json_worker.cc"
      ],
      "conditions": [
        ["OS=='linux'", {
          "link_settings": {
            "libraries": ["-lfptr10"],
            "ldflags": [
              "-L<(module_root_dir)/build/Release",
              "-Wl,-rpath,<(module_root_dir)/build/Release"
            ]
          }
        }],
        ["OS=='win'", {
          "link_settings": {
            "libraries": ["<(module_root_dir)/build/Release/fptr10.lib"]
          }
        }],
        ["OS=='mac'", {
          "link_settings": {
            "libraries": [
              "<(module_root_dir)/build/Release/fptr10.framework/Versions/A/fptr10"
            ],
            "ldflags": [
              "-Wl,-rpath,@loader_path"
            ]
          },
          "xcode_settings": {
            "OTHER_CPLUSPLUSFLAGS": [
              "-std=c++17",
              "-stdlib=libc++"
            ],
            "OTHER_LDFLAGS": [
              "-stdlib=libc++"
            ],
            "MACOSX_DEPLOYMENT_TARGET": "10.15"
          }
        }]
      ],
      "dependencies": ["copy_fptr_libs"]
    },
    {
      "target_name": "copy_node_to_variants",
      "type": "none",
      "dependencies": ["node_atol_wrapper"],
      "copies": [
        {
          "destination": "<(PRODUCT_DIR)/dto",
          "files": ["<(PRODUCT_DIR)/node_atol_wrapper.node"]
        },
        {
          "destination": "<(PRODUCT_DIR)/dto-piot",
          "files": ["<(PRODUCT_DIR)/node_atol_wrapper.node"]
        }
      ]
    }
  ]
}
